#!/usr/bin/env python3
"""B-roll story reel: long first-person text directly on darkened footage, strict 5.0 s loop, with music.

Format (owner decision Oct 16 2026): the reel is always exactly 5.0 s and loops; viewers read the long text
over several loops. No white plate. Text sits inside the Instagram safe zone.

Usage:
  python3 tools/reels/story_reel.py preview            # writes preview JPGs for every reel in REELS
  python3 tools/reels/story_reel.py render [id ...]    # renders final MP4s into output/
"""
import json
import random
import subprocess
import sys
from datetime import date
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
FFMPEG = "/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2"
FONT = "/usr/share/fonts/truetype/montserrat/Montserrat-Medium.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/montserrat/Montserrat-Bold.ttf"
OUT = ROOT / "output"
W, H = 1080, 1920
TOP_SAFE, BOTTOM_ANCHOR = 270, 1520
MAX_W = 820          # inside the 108px side margins
SIZE, LINE_H = 44, 62
CLIPS = ROOT / "footage" / "general"

REELS = [
    {"id": "fact_lottery", "clip": "1_16.mp4", "lines": [
        "Sweden studied lottery winners.",
        "",
        "Men who won got married more often.",
        "They had more children.",
        "",
        "Women who won were more likely to divorce, at least for a while.",
        "",
        "Researchers say the money didn't end those marriages.",
        "It sped up the ones already ending."]},
    {"id": "fact_liar", "clip": "face_4.mp4", "lines": [
        "You think you can spot a liar.",
        "",
        "Researchers combined 206 studies.",
        "People caught lies 54% of the time.",
        "A coin flip is 50%.",
        "",
        "We spot the truth 61% of the time.",
        "We catch a lie 47% of the time."]},
    {"id": "fact_widow", "clip": "31_2.mp4", "lines": [
        "After a spouse dies, the one left behind is more likely to die too.",
        "",
        "In 373,189 older couples,",
        "the risk was 30% to 90% higher in the first three months.",
        "",
        "About 15% higher after that.",
        "",
        "Scientists call it the widowhood effect."]},
    {"id": "fact_graydivorce", "clip": "32_2.mp4", "lines": [
        "Divorce is falling in America.",
        "Except after 50.",
        "",
        "Between 1990 and 2010,",
        "divorce among people 50 and older roughly doubled.",
        "",
        "From about 5 to 10 per 1,000 married people."]},
]


def wrap(draw, text, font):
    if not text:
        return [""]
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= MAX_W:
            cur = t
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    return lines


def overlay(frame, lines):
    """Darken the frame, add a bottom gradient, draw centered text. Returns RGB image."""
    img = frame.convert("RGB").resize((W, H))
    dark = Image.new("RGBA", (W, H), (0, 0, 0, 120))          # uniform dim
    grad = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(grad)
    GH = 1100
    for i in range(GH):
        gd.rectangle([(0, H - GH + i), (W, H - GH + i + 1)], fill=(0, 0, 0, int(150 * (i / GH) ** 1.2)))
    img = Image.alpha_composite(Image.alpha_composite(img.convert("RGBA"), dark), grad)
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT, SIZE)
    rows = []
    for ln in lines:
        rows += wrap(d, ln, font)
    total = sum(LINE_H if r else LINE_H // 2 for r in rows)
    y = min(BOTTOM_ANCHOR - total, BOTTOM_ANCHOR)
    assert y >= TOP_SAFE, f"text too tall: starts at {y}"
    for r in rows:
        if r:
            x = (W - d.textlength(r, font=font)) / 2
            d.text((x + 2, y + 3), r, font=font, fill=(0, 0, 0, 170))   # soft shadow
            d.text((x, y), r, font=font, fill=(255, 255, 255, 245))
            y += LINE_H
        else:
            y += LINE_H // 2
    return img.convert("RGB")


def frame_from(clip, t=2.0):
    tmp = Path("/tmp/_story_frame.jpg")
    subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-ss", str(t), "-i", str(CLIPS / clip),
                    "-vframes", "1", "-vf", f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}", str(tmp)], check=True)
    return Image.open(tmp)


def pick_music():
    log_path = ROOT / "music" / "music_log.json"
    log = json.loads(log_path.read_text()) if log_path.exists() else {}
    recent = set()
    for d, tracks in log.items():
        try:
            if (date.today() - date.fromisoformat(d)).days <= 1:
                recent |= set(tracks)
        except ValueError:
            continue  # e.g. "_comment" keys
    pool = [f"{i}.mp3" for i in range(1, 31) if f"{i}.mp3" not in recent] or [f"{i}.mp3" for i in range(1, 31)]
    track = random.choice(pool)
    log.setdefault(date.today().isoformat(), []).append(track)
    log_path.write_text(json.dumps(log, indent=2))
    return track


def render(reel):
    OUT.mkdir(exist_ok=True)
    png = OUT / f"{reel['id']}_text.png"
    # transparent text layer is cheaper to composite over moving video: build overlay on a blank frame
    base = Image.new("RGB", (W, H), (0, 0, 0))
    full = overlay(base, reel["lines"])
    # For video we need dim + text over the moving footage: dim via ffmpeg, text as PNG with alpha.
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    font = ImageFont.truetype(FONT, SIZE)
    rows = []
    for ln in reel["lines"]:
        rows += wrap(d, ln, font)
    total = sum(LINE_H if r else LINE_H // 2 for r in rows)
    y = BOTTOM_ANCHOR - total
    for r in rows:
        if r:
            x = (W - d.textlength(r, font=font)) / 2
            d.text((x + 2, y + 3), r, font=font, fill=(0, 0, 0, 170))
            d.text((x, y), r, font=font, fill=(255, 255, 255, 245))
            y += LINE_H
        else:
            y += LINE_H // 2
    grad = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(grad)
    GH = 1100
    for i in range(GH):
        gd.rectangle([(0, H - GH + i), (W, H - GH + i + 1)], fill=(0, 0, 0, int(150 * (i / GH) ** 1.2)))
    layer = Image.alpha_composite(grad, layer)
    layer.save(png)
    music = pick_music()
    out = OUT / f"{reel['id']}.mp4"
    cmd = [FFMPEG, "-y", "-loglevel", "error",
           "-stream_loop", "-1", "-i", str(ROOT / "music" / music),
           "-stream_loop", "-1", "-i", str(CLIPS / reel["clip"]),
           "-i", str(png),
           "-filter_complex",
           f"[1:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},eq=brightness=-0.18[bg];[bg][2:v]overlay=0:0[v]",
           "-map", "[v]", "-map", "0:a", "-af", "volume=0.8",
           "-c:v", "libx264", "-c:a", "aac", "-b:a", "128k",
           "-t", "5.0", "-frames:v", "150", "-r", "30", "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p", str(out)]
    subprocess.run(cmd, check=True)
    print("rendered", out, "music", music)
    return out


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "preview"
    ids = set(sys.argv[2:])
    for reel in REELS:
        if ids and reel["id"] not in ids:
            continue
        if mode == "preview":
            OUT.mkdir(exist_ok=True)
            p = OUT / f"{reel['id']}_preview.jpg"
            overlay(frame_from(reel["clip"]), reel["lines"]).save(p, quality=92)
            print("preview", p)
        else:
            render(reel)


if __name__ == "__main__":
    main()
