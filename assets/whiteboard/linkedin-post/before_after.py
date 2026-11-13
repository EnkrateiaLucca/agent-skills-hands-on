# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow"]
# ///
"""Compose 1080x1350 BEFORE/AFTER images for the LinkedIn post."""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

S = Path(sys.argv[1])
SHOTS = Path.home() / "Pictures/Screenshots"
PAIRS = [  # (before screenshot, after frame index, caption)
    ("CleanShot 2026-11-05 at 10.39.22@2x.png", 6, "Progressive disclosure"),
    ("CleanShot 2026-11-05 at 10.38.47@2x.png", 4, "Context rot"),
    ("CleanShot 2026-11-05 at 10.39.52@2x.png", 8, "Prompting (2 sketches merged into 1)"),
    ("CleanShot 2026-11-05 at 10.38.20@2x.png", 2, "What fills the context window"),
]
W, H, M = 1080, 1350, 40
FONT = "/System/Library/Fonts/Avenir Next.ttc"
bold = lambda s: ImageFont.truetype(FONT, s, index=0)  # Avenir Next Bold
reg = lambda s: ImageFont.truetype(FONT, s, index=7)   # Avenir Next Regular


def fit(img, box_w, box_h):
    img = ImageOps.contain(img.convert("RGB"), (box_w, box_h), Image.LANCZOS)
    return img


def card(draw, canvas, img, y, h, label, color):
    draw.rounded_rectangle([M, y, W - M, y + h], 24, fill="#f8f9fa", outline=color, width=4)
    draw.rounded_rectangle([M + 24, y - 22, M + 24 + 34 + draw.textlength(label, bold(26)), y + 22],
                           22, fill=color)
    draw.text((M + 41, y - 17), label, font=bold(26), fill="white")
    im = fit(img, W - 2 * M - 16, h - 56)
    canvas.paste(im, ((W - im.width) // 2, y + 40 + (h - 60 - im.height) // 2))


for n, (before, idx, cap) in enumerate(PAIRS, 1):
    c = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(c)
    d.text((M, 30), cap, font=bold(42), fill="#1e1e1e")
    d.text((M, 88), f"{n}/{len(PAIRS)} · from hand sketch to class companion", font=reg(26), fill="#868e96")
    card(d, c, Image.open(SHOTS / before), 170, 470, "BEFORE · my sketch", "#868e96")
    d.polygon([(W // 2 - 26, 664), (W // 2 + 26, 664), (W // 2, 700)], fill="#1e1e1e")
    card(d, c, Image.open(S / f"after-{idx}.png"), 735, 585, "AFTER · rebuilt with Claude Code", "#2f9e44")
    c.save(S / f"linkedin-{n}.png")
    print(S / f"linkedin-{n}.png")
