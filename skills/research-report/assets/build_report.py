#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""Wrap a finished markdown research report in the single-file HTML shell.

Usage: build_report.py report.md [-o report.html]

The markdown is embedded verbatim in the HTML (rendered client-side, and handed
back by the Export .md button), so the .md file stays the single source of truth.
"""
import argparse, pathlib, re, sys, webbrowser

TEMPLATE = pathlib.Path(__file__).with_name("report-template.html")


def build(md_path: pathlib.Path, out_path: pathlib.Path) -> pathlib.Path:
    md = md_path.read_text(encoding="utf-8")
    m = re.search(r"^#\s+(.+)$", md, re.M)
    title = m.group(1).strip() if m else md_path.stem.replace("_", " ").title()

    # </script> anywhere in the report would close the embedding block early.
    safe_md = md.replace("</script>", "<\\/script>")

    html = (TEMPLATE.read_text(encoding="utf-8")
            .replace("{{TITLE}}", title)
            .replace("{{FILENAME}}", md_path.name)
            .replace("{{MARKDOWN}}", safe_md))
    out_path.write_text(html, encoding="utf-8")
    return out_path


def demo():
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        p = pathlib.Path(d) / "t.md"
        p.write_text("# Hi\n\nclaim <sup>[A]</sup>\n\n<script>x</script>\n")
        out = build(p, p.with_suffix(".html"))
        h = out.read_text()
        assert "<title>Hi</title>" in h
        assert 'FILENAME = "t.md"' in h
        assert "<\\/script>" in h and "<script>x</script>" not in h
        assert h.count("{{") == 0
        print("ok")


if __name__ == "__main__":
    if "--demo" in sys.argv:
        demo(); sys.exit()
    ap = argparse.ArgumentParser()
    ap.add_argument("markdown", type=pathlib.Path)
    ap.add_argument("-o", "--out", type=pathlib.Path)
    ap.add_argument("--no-open", action="store_true", help="don't open in the browser")
    a = ap.parse_args()
    out = a.out or a.markdown.with_suffix(".html")
    print(build(a.markdown, out))
    if not a.no_open:
        webbrowser.open(out.resolve().as_uri())
