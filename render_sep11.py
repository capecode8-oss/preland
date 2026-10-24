#!/usr/bin/env python3
"""Render 5 reels for Sep 11 2026 batch"""

import subprocess, os, json
from PIL import Image, ImageDraw, ImageFont
from datetime import date

FFMPEG = "/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2"
FONT_PATH = "/usr/share/fonts/truetype/montserrat/Montserrat-BlackItalic.ttf"
MUSIC_DIR = "/home/user/preland/music"
FOOTAGE_DIR = "/home/user/preland/footage/travel"
OUT_DIR = "/home/user/preland/reels"
os.makedirs(OUT_DIR, exist_ok=True)

# Canvas / safe zone
W, H = 1080, 1920
BOTTOM_ANCHOR = 1520
MAX_TEXT_W = 760
PAD_X, PAD_TOP, PAD_BOTTOM = 32, 28, 28
LINE_GAP = 8
CENTER_X = 540
RADIUS = 18

REELS = [
    {
        "id": "sep11_r1_cruise_cabin",
        "clip": "32_13.mp4",
        "music": "17.mp3",
        "lines": [
            "Never Book A Cruise Cabin",
            "Below Deck 5.",
            "A Crew Member Warned Me.",
        ],
    },
    {
        "id": "sep11_r2_checked_bag",
        "clip": "32_9.mp4",
        "music": "18.mp3",
        "lines": [
            "Checked My Bag For Years.",
            "A TSA Agent Stopped Me.",
            "She Changed How I Fly.",
        ],
    },
    {
        "id": "sep11_r3_hotel_hack",
        "clip": "32_6.mp4",
        "music": "19.mp3",
        "lines": [
            "This Hotel Hack Feels Illegal.",
            "But It's Totally Allowed.",
            "I've Used It 12 Times.",
        ],
    },
    {
        "id": "sep11_r4_hot_drinks",
        "clip": "32_5.mp4",
        "music": "20.mp3",
        "lines": [
            "Never Order Hot Drinks",
            "On Any Flight.",
            "A Flight Attendant Told Me.",
        ],
    },
    {
        "id": "sep11_r5_customs",
        "clip": "32_18.mp4",
        "music": "21.mp3",
        "lines": [
            "Everyone Brings This On Trips.",
            "Customs Pulled Me Aside.",
            "I Don't Pack It Anymore.",
        ],
    },
]

def load_font(size):
    return ImageFont.truetype(FONT_PATH, size)

def measure_text(draw, text, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0]

def auto_font_size(draw, lines, max_w=MAX_TEXT_W, max_size=70, min_size=40):
    for size in range(max_size, min_size - 1, -1):
        font = load_font(size)
        if all(measure_text(draw, l, font) <= max_w for l in lines):
            return font, size
    return load_font(min_size), min_size

def render_overlay(lines, out_png):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    font, size = auto_font_size(draw, lines)
    print(f"  Font size: {size}px")

    line_heights = []
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        line_heights.append(bbox[3] - bbox[1])

    line_h = max(line_heights)
    box_h = PAD_TOP + len(lines) * line_h + (len(lines) - 1) * LINE_GAP + PAD_BOTTOM

    max_lw = max(measure_text(draw, l, font) for l in lines)
    box_w = min(860, max_lw + 2 * PAD_X)

    box_x0 = CENTER_X - box_w // 2
    box_y0 = BOTTOM_ANCHOR - box_h
    box_x1 = CENTER_X + box_w // 2
    box_y1 = BOTTOM_ANCHOR

    # Draw rounded rect
    draw.rounded_rectangle([box_x0, box_y0, box_x1, box_y1],
                            radius=RADIUS, fill=(255, 255, 255, 255))

    # Draw text lines
    y = box_y0 + PAD_TOP
    for line in lines:
        lw = measure_text(draw, line, font)
        x = CENTER_X - lw // 2
        draw.text((x, y), line, font=font, fill=(0, 0, 0, 255))
        y += line_h + LINE_GAP

    img.save(out_png)
    print(f"  Overlay saved: {out_png}")

def render_reel(reel):
    reel_id = reel["id"]
    clip_path = os.path.join(FOOTAGE_DIR, reel["clip"])
    music_path = os.path.join(MUSIC_DIR, reel["music"])
    out_mp4 = os.path.join(OUT_DIR, f"{reel_id}.mp4")
    overlay_png = f"/tmp/{reel_id}_overlay.png"
    preview_jpg = f"/tmp/{reel_id}_preview.jpg"

    print(f"\n{'='*50}")
    print(f"Rendering: {reel_id}")
    print(f"  Clip: {reel['clip']}  Music: {reel['music']}")

    # Step 1: render text overlay
    render_overlay(reel["lines"], overlay_png)

    # Step 2: ffmpeg — video + overlay + music
    cmd = [
        FFMPEG, "-y",
        "-stream_loop", "-1", "-i", music_path,
        "-stream_loop", "-1", "-i", clip_path,
        "-i", overlay_png,
        "-filter_complex",
        "[1:v]scale=1080:1920:force_original_aspect_ratio=increase,"
        "crop=1080:1920,setsar=1[bg];"
        "[bg][2:v]overlay=0:0[out]",
        "-map", "[out]",
        "-map", "0:a",
        "-af", "volume=0.8",
        "-t", "5.0",
        "-r", "30",
        "-frames:v", "150",
        "-c:v", "libx264",
        "-c:a", "aac",
        "-b:a", "128k",
        "-crf", "18",
        "-preset", "fast",
        "-pix_fmt", "yuv420p",
        out_mp4
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  ERROR: {result.stderr[-500:]}")
        return False

    print(f"  MP4 rendered: {out_mp4}")

    # Step 3: extract preview frame
    cmd_prev = [
        FFMPEG, "-y", "-ss", "2", "-i", out_mp4,
        "-vframes", "1", "-vf", "scale=540:960",
        preview_jpg
    ]
    subprocess.run(cmd_prev, capture_output=True)
    print(f"  Preview: {preview_jpg}")
    return True

if __name__ == "__main__":
    # Check font
    if not os.path.exists(FONT_PATH):
        print("Installing Montserrat...")
        os.system("apt-get install -y fonts-montserrat -q")

    success = []
    for reel in REELS:
        ok = render_reel(reel)
        if ok:
            success.append(reel["id"])

    print(f"\n\nDone: {len(success)}/{len(REELS)} rendered successfully")
    print("Rendered:", success)

    # Update music log
    log_path = "/home/user/preland/music/music_log.json"
    with open(log_path) as f:
        log = json.load(f)
    today = str(date.today())
    used_today = log.get(today, [])
    for r in REELS:
        if r["music"] not in used_today:
            used_today.append(r["music"])
    log[today] = used_today
    with open(log_path, "w") as f:
        json.dump(log, f, indent=2, ensure_ascii=False)
    print(f"Music log updated for {today}")
