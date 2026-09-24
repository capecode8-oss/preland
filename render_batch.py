#!/usr/bin/env python3
"""Batch render 5 reels — Sep 24 2026"""

import os, json, subprocess
from PIL import Image, ImageDraw, ImageFont
from datetime import date

FFMPEG = "/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2"
FONT_PATH = "/usr/share/fonts/truetype/montserrat/Montserrat-BlackItalic.ttf"
FOOTAGE = "/home/user/preland/footage/travel"
MUSIC_DIR = "/home/user/preland/music"
OUT_DIR = "/home/user/preland/output"
os.makedirs(OUT_DIR, exist_ok=True)

BOTTOM_ANCHOR = 1520
MAX_TEXT_W = 760
MAX_BOX_W = 860
CENTER_X = 540
PAD_X = 32
PAD_TOP = 28
PAD_BOT = 28
LINE_GAP = 8
RADIUS = 18

REELS = [
    {
        "id": "reel1",
        "clip": "32_5.mp4",
        "music": "25.mp3",
        "lines": [
            "I ordered coffee on every flight for 10 YEARS.",
            "A flight attendant STOPPED ME mid-sip.",
            "The water tank hadn't been cleaned in 6 MONTHS.",
        ],
    },
    {
        "id": "reel2",
        "clip": "32_9.mp4",
        "music": "30.mp3",
        "lines": [
            "I watched the person ahead of me PAY $65",
            "for the SAME BAG I carried on for FREE.",
            "Same size. Same airline. Same gate.",
        ],
    },
    {
        "id": "reel3",
        "clip": "32_1.mp4",
        "music": "6.mp3",
        "lines": [
            "Airlines OWE YOU up to $1,550 IN CASH",
            "if they bump you involuntarily.",
            "Most people accept $50 in vouchers and say THANK YOU.",
        ],
    },
    {
        "id": "reel4",
        "clip": "32_18.mp4",
        "music": "7.mp3",
        "lines": [
            "I watched someone walk away with a bag",
            "that WASN'T THEIRS at baggage claim in Madrid.",
            "He was GONE before the owner reached the belt.",
        ],
    },
    {
        "id": "reel5",
        "clip": "32_12.mp4",
        "music": "19.mp3",
        "lines": [
            "The driver waiting at arrivals with my name on a sign",
            "had a meter running at AIRPORT RATE — 3× THE NORMAL PRICE.",
            "I didn't know that was even LEGAL.",
        ],
    },
]


def auto_font(lines, max_size=70, min_size=36):
    for size in range(max_size, min_size - 1, -1):
        font = ImageFont.truetype(FONT_PATH, size)
        dummy = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
        if all(dummy.textlength(l, font=font) <= MAX_TEXT_W for l in lines):
            return font, size
    return ImageFont.truetype(FONT_PATH, min_size), min_size


def draw_overlay(bg_path, lines, out_path):
    img = Image.open(bg_path).convert("RGBA")
    img = img.resize((1080, 1920), Image.LANCZOS)

    font, size = auto_font(lines)
    dummy_draw = ImageDraw.Draw(Image.new("RGBA", (1, 1)))

    line_heights = [int(font.getbbox(l)[3] - font.getbbox(l)[1]) for l in lines]
    total_text_h = sum(line_heights) + LINE_GAP * (len(lines) - 1)
    box_h = PAD_TOP + total_text_h + PAD_BOT

    max_lw = max(dummy_draw.textlength(l, font=font) for l in lines)
    box_w = min(MAX_BOX_W, int(max_lw) + 2 * PAD_X)

    hook_y0 = BOTTOM_ANCHOR - box_h
    box_x0 = CENTER_X - box_w // 2
    box_x1 = CENTER_X + box_w // 2

    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    draw.rounded_rectangle(
        [box_x0, hook_y0, box_x1, hook_y0 + box_h],
        radius=RADIUS,
        fill=(255, 255, 255, 255),
    )

    y = hook_y0 + PAD_TOP
    for i, line in enumerate(lines):
        lw = dummy_draw.textlength(line, font=font)
        x = CENTER_X - lw / 2
        draw.text((x, y), line, font=font, fill=(0, 0, 0, 255))
        y += line_heights[i] + (LINE_GAP if i < len(lines) - 1 else 0)

    img = Image.alpha_composite(img, overlay).convert("RGB")
    img.save(out_path, quality=95)
    print(f"  Preview saved: {out_path}")


def render_reel(reel):
    rid = reel["id"]
    clip = os.path.join(FOOTAGE, reel["clip"])
    music = os.path.join(MUSIC_DIR, reel["music"])
    lines = reel["lines"]

    print(f"\n{'='*50}")
    print(f"Rendering {rid} | {reel['clip']} | {reel['music']}")

    # Extract frame for preview
    bg_path = f"/tmp/bg_{rid}.jpg"
    subprocess.run([
        FFMPEG, "-y", "-ss", "2", "-i", clip,
        "-vframes", "1",
        "-vf", "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920",
        bg_path
    ], capture_output=True)

    # Draw overlay preview
    preview_path = os.path.join(OUT_DIR, f"{rid}_preview.jpg")
    draw_overlay(bg_path, lines, preview_path)

    # Render final MP4
    mp4_path = os.path.join(OUT_DIR, f"{rid}.mp4")
    cmd = [
        FFMPEG, "-y",
        "-stream_loop", "-1", "-i", music,
        "-stream_loop", "-1", "-i", clip,
        "-map", "1:v", "-map", "0:a",
        "-af", "volume=0.8",
        "-vf", "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920",
        "-t", "5.0", "-frames:v", "150", "-r", "30",
        "-c:v", "libx264", "-c:a", "aac", "-b:a", "128k",
        "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p",
        mp4_path
    ]
    result = subprocess.run(cmd, capture_output=True)
    if result.returncode == 0:
        print(f"  MP4 rendered: {mp4_path}")
    else:
        print(f"  ERROR: {result.stderr[-300:].decode()}")
        return False

    # Draw overlay on final frame for final preview JPG
    final_bg = f"/tmp/final_bg_{rid}.jpg"
    subprocess.run([
        FFMPEG, "-y", "-ss", "2", "-i", mp4_path,
        "-vframes", "1", final_bg
    ], capture_output=True)
    final_preview = os.path.join(OUT_DIR, f"{rid}_final.jpg")
    draw_overlay(final_bg, lines, final_preview)

    return True


# Update music log
def update_music_log(reels):
    log_path = os.path.join(MUSIC_DIR, "music_log.json")
    log = json.load(open(log_path)) if os.path.exists(log_path) else {}
    today = str(date.today())
    log.setdefault(today, [])
    for r in reels:
        if r["music"] not in log[today]:
            log[today].append(r["music"])
    json.dump(log, open(log_path, "w"), indent=2)
    print(f"\nMusic log updated: {[r['music'] for r in reels]}")


if __name__ == "__main__":
    success = []
    for reel in REELS:
        ok = render_reel(reel)
        if ok:
            success.append(reel["id"])

    update_music_log(REELS)
    print(f"\n{'='*50}")
    print(f"Done: {len(success)}/5 reels rendered")
    print(f"Output: {OUT_DIR}")
