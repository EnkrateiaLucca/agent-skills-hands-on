# /// script
# requires-python = ">=3.11"
# dependencies = ["playwright>=1.45", "pillow>=10"]
# ///
"""Render every scene of a scene-deck at its final step and flag layout problems.

uv run snapshot.py deck.html [--out DIR] [--all-steps]

Writes one PNG per scene (or per step with --all-steps) plus contact.png (a grid of
all shots), then prints console errors and elements that spill outside their scene.
Uses the installed Google Chrome, so no browser download is needed.
"""
import argparse
import pathlib
import sys

from PIL import Image
from playwright.sync_api import sync_playwright

OVERFLOW_JS = """(si) => {
  const sc = document.querySelectorAll('.scene')[si], bad = [];
  for (const e of sc.querySelectorAll('*')) {
    if (e.closest('defs,pattern,filter,.gone')) continue;
    const r = e.getBoundingClientRect(), cs = getComputedStyle(e);
    if (!r.width || !r.height || cs.visibility === 'hidden') continue;
    // content box is x 90-1510, y 64-736; allow a little bleed, and let .src sit in the bottom padding
    if (r.right > 1525 || r.left < 75 || r.top < 40 || r.bottom > (e.closest('.src') ? 795 : 750))
      bad.push(`${e.tagName.toLowerCase()}${e.getAttribute('class') ? '.' + e.getAttribute('class').split(' ')[0] : ''} `
        + `"${(e.textContent || '').trim().slice(0, 40)}" box=(${r.left|0},${r.top|0})-(${r.right|0},${r.bottom|0})`);
  }
  return bad.slice(0, 8);
}"""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("deck")
    ap.add_argument("--out", default=None)
    ap.add_argument("--all-steps", action="store_true")
    a = ap.parse_args()
    deck = pathlib.Path(a.deck).resolve()
    out = pathlib.Path(a.out or deck.parent / f"{deck.stem}-shots")
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("*.png"):
        old.unlink()

    errors, shots, problems = [], [], 0
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome")
        page = browser.new_page(viewport={"width": 1600, "height": 900})
        page.on("console", lambda m: m.type == "error" and errors.append(m.text))
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.goto(deck.as_uri())
        page.wait_for_timeout(800)
        steps = page.evaluate("deck.steps")  # [[sceneIdx, localStep], ...]
        print(f"{len(steps)} steps · {len(set(s for s, _ in steps))} scenes · "
              f"{len(page.evaluate('deck.chapters'))} chapters")
        targets = range(len(steps)) if a.all_steps else [
            i for i, (s, _) in enumerate(steps) if i + 1 == len(steps) or steps[i + 1][0] != s]
        for g in targets:
            s, k = steps[g]
            page.evaluate(f"deck.go({g}, false)")
            page.wait_for_timeout(1500)  # let draw-on transitions finish
            f = out / f"step{g:03d}_scene{s:02d}_k{k}.png"
            page.screenshot(path=str(f))
            shots.append(f)
            bad = page.evaluate(OVERFLOW_JS, s)
            if bad:
                problems += 1
                print(f"\nscene {s} (step {g}) spills outside the scene box:")
                for b in bad:
                    print("   ", b)
        browser.close()

    cols, w, h = 4, 400, 225
    sheet = Image.new("RGB", (cols * w, -(-len(shots) // cols) * h), "white")
    for i, f in enumerate(shots):
        sheet.paste(Image.open(f).convert("RGB").resize((w, h)), ((i % cols) * w, (i // cols) * h))
    sheet.save(out / "contact.png")

    print(f"\n{len(shots)} shots -> {out}  (contact.png = grid)")
    print("console errors:", errors or "none")
    if errors or problems:
        sys.exit(1)


if __name__ == "__main__":
    main()
