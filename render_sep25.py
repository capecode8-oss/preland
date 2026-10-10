#!/usr/bin/env python3
"""Batch render 10 reels — Sep 25 2026"""

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
TOP_SAFE = 270

REELS = [
    {
        "id": "s25_r1",
        "clip": "32_7.mp4",
        "music": "1.mp3",
        "lines": [
            "I found a small hole in my hotel room wall in PRAGUE.",
            "A housekeeper walked in and went PALE.",
            "She told me what it was FOR.",
        ],
    },
    {
        "id": "s25_r2",
        "clip": "32_8.mp4",
        "music": "2.mp3",
        "lines": [
            "I ordered from the top of every menu for 23 COUNTRIES.",
            "A waiter in Tokyo FINALLY told me",
            "why restaurants put those dishes there.",
        ],
    },
    {
        "id": "s25_r3",
        "clip": "32_13.mp4",
        "music": "3.mp3",
        "lines": [
            "First-time cruisers: the buffet opens at 7 AM.",
            "DON'T be there at 7 AM.",
            "A ship's nurse told me what happens at 6:59.",
        ],
    },
    {
        "id": "s25_r4",
        "clip": "32_10.mp4",
        "music": "4.mp3",
        "lines": [
            "I paid $85 for TSA PreCheck for 6 YEARS.",
            "A TSA agent told me I'd been ELIGIBLE",
            "for the no-cost version the WHOLE TIME.",
        ],
    },
    {
        "id": "s25_r5",
        "clip": "32_3.mp4",
        "music": "5.mp3",
        "lines": [
            "A stranger asked to take my photo in ROME.",
            "I handed him my phone.",
            "He handed it back — and walked away with MY BAG.",
        ],
    },
    {
        "id": "s25_r6",
        "clip": "32_14.mp4",
        "music": "8.mp3",
        "lines": [
            "Experienced cruisers: DON'T book the balcony upfront.",
            "DON'T call customer service.",
            "DON'T pay the upgrade price. What they do costs $0.",
        ],
    },
    {
        "id": "s25_r7",
        "clip": "32_17.mp4",
        "music": "9.mp3",
        "lines": [
            "I paid €60 for a 10-minute taxi at EVERY cruise port.",
            "A crew member pulled me aside BEFORE I got off the ship.",
            "She told me the REAL price.",
        ],
    },
    {
        "id": "s25_r8",
        "clip": "32_15.mp4",
        "music": "10.mp3",
        "lines": [
            "I bought the drink package on every cruise for 9 YEARS.",
            "A bartender on my last ship told me",
            "I'd been paying for drinks I'D NEVER USE.",
        ],
    },
    {
        "id": "s25_r9",
        "clip": "32_16.mp4",
        "music": "11.mp3",
        "lines": [
            "I got seasick on EVERY cruise for 11 YEARS.",
            "A ship's doctor stopped me at the pharmacy counter.",
            "She said I'd been using the WRONG patch placement.",
        ],
    },
    {
        "id": "s25_r10",
        "clip": "31_1.mp4",
        "music": "12.mp3",
        "lines": [
            "I tipped at every restaurant abroad for 15 YEARS.",
            "A local in Portugal told me what it ACTUALLY MEANS",
            "when an American tips in Europe.",
        ],
    },
]


def wrap_line(text, font, max_width):
    dummy = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    words = text.split()
    visual_lines, current = [], ""
    for word in words:
        candidate = (current + " " + word).strip()
        if dummy.textlength(candidate, font=font) <= max_width:
            current = candidate
        else:
            if current:
                visual_lines.append(current)
            current = word
    if current:
        visual_lines.append(current)
    return visual_lines or [text]


def pick_font(lines, max_size=70, min_size=24):
    dummy = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    for size in range(max_size, min_size - 1, -1):
        font = ImageFont.truetype(FONT_PATH, size)
        visual_lines = []
        for l in lines:
            visual_lines.extend(wrap_line(l, font, MAX_TEXT_W))
        if not all(dummy.textlength(l, font=font) <= MAX_TEXT_W for l in visual_lines):
            continue
        line_heights = [int(font.getbbox(l)[3] - font.getbbox(l)[1]) for l in visual_lines]
        total_text_h = sum(line_heights) + LINE_GAP * (len(visual_lines) - 1)
        box_h = PAD_TOP + total_text_h + PAD_BOT
        if BOTTOM_ANCHOR - box_h >= TOP_SAFE:
            return font, size, visual_lines
    font = ImageFont.truetype(FONT_PATH, min_size)
    visual_lines = []
    for l in lines:
        visual_lines.extend(wrap_line(l, font, MAX_TEXT_W))
    return font, min_size, visual_lines


def preflight_check(lines):
    font, size, visual_lines = pick_font(lines)
    dummy = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    line_heights = [int(font.getbbox(l)[3] - font.getbbox(l)[1]) for l in visual_lines]
    total_text_h = sum(line_heights) + LINE_GAP * (len(visual_lines) - 1)
    box_h = PAD_TOP + total_text_h + PAD_BOT
    hook_y0 = BOTTOM_ANCHOR - box_h
    ok = True
    print(f"  [preflight] font={size}px | lines={len(visual_lines)} | hook_y0={hook_y0}px")
    for l in visual_lines:
        w = dummy.textlength(l, font=font)
        fits = w <= MAX_TEXT_W
        if not fits: ok = False
        print(f"    {'✅' if fits else '❌'} {int(w)}px — {l}")
    if hook_y0 < TOP_SAFE:
        ok = False
        print(f"  ❌ BOX TOO TALL: hook_y0={hook_y0} < {TOP_SAFE}")
    else:
        print(f"  ✅ Vertical fit: top at {hook_y0}px")
    return ok


def create_overlay_png(lines, out_path, width=1080, height=1920):
    font, size, visual_lines = pick_font(lines)
    dummy_draw = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    line_heights = [int(font.getbbox(l)[3] - font.getbbox(l)[1]) for l in visual_lines]
    total_text_h = sum(line_heights) + LINE_GAP * (len(visual_lines) - 1)
    box_h = PAD_TOP + total_text_h + PAD_BOT
    max_lw = max(dummy_draw.textlength(l, font=font) for l in visual_lines)
    box_w = min(MAX_BOX_W, int(max_lw) + 2 * PAD_X)
    hook_y0 = BOTTOM_ANCHOR - box_h
    box_x0 = CENTER_X - box_w // 2
    box_x1 = CENTER_X + box_w // 2
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    draw.rounded_rectangle([box_x0, hook_y0, box_x1, hook_y0 + box_h], radius=RADIUS, fill=(255, 255, 255, 255))
    y = hook_y0 + PAD_TOP
    for i, line in enumerate(visual_lines):
        lw = dummy_draw.textlength(line, font=font)
        x = CENTER_X - lw / 2
        draw.text((x, y), line, font=font, fill=(0, 0, 0, 255))
        y += line_heights[i] + (LINE_GAP if i < len(visual_lines) - 1 else 0)
    overlay.save(out_path)


def draw_overlay(bg_path, lines, out_path):
    img = Image.open(bg_path).convert("RGBA")
    img = img.resize((1080, 1920), Image.LANCZOS)
    font, size, visual_lines = pick_font(lines)
    dummy_draw = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    line_heights = [int(font.getbbox(l)[3] - font.getbbox(l)[1]) for l in visual_lines]
    total_text_h = sum(line_heights) + LINE_GAP * (len(visual_lines) - 1)
    box_h = PAD_TOP + total_text_h + PAD_BOT
    max_lw = max(dummy_draw.textlength(l, font=font) for l in visual_lines)
    box_w = min(MAX_BOX_W, int(max_lw) + 2 * PAD_X)
    hook_y0 = BOTTOM_ANCHOR - box_h
    box_x0 = CENTER_X - box_w // 2
    box_x1 = CENTER_X + box_w // 2
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    draw.rounded_rectangle([box_x0, hook_y0, box_x1, hook_y0 + box_h], radius=RADIUS, fill=(255, 255, 255, 255))
    y = hook_y0 + PAD_TOP
    for i, line in enumerate(visual_lines):
        lw = dummy_draw.textlength(line, font=font)
        x = CENTER_X - lw / 2
        draw.text((x, y), line, font=font, fill=(0, 0, 0, 255))
        y += line_heights[i] + (LINE_GAP if i < len(visual_lines) - 1 else 0)
    img = Image.alpha_composite(img, overlay).convert("RGB")
    img.save(out_path, quality=95)
    print(f"  Preview: {out_path}")


def render_reel(reel):
    rid = reel["id"]
    clip = os.path.join(FOOTAGE, reel["clip"])
    music = os.path.join(MUSIC_DIR, reel["music"])
    lines = reel["lines"]
    print(f"\n{'='*50}")
    print(f"{rid} | {reel['clip']} | {reel['music']}")
    if not preflight_check(lines):
        print(f"  ❌ PREFLIGHT FAILED — aborting {rid}")
        return False
    bg_path = f"/tmp/bg_{rid}.jpg"
    subprocess.run([FFMPEG, "-y", "-ss", "2", "-i", clip, "-vframes", "1",
                    "-vf", "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920",
                    bg_path], capture_output=True)
    preview_path = os.path.join(OUT_DIR, f"{rid}_preview.jpg")
    draw_overlay(bg_path, lines, preview_path)
    overlay_png = f"/tmp/overlay_{rid}.png"
    create_overlay_png(lines, overlay_png)

    mp4_path = os.path.join(OUT_DIR, f"{rid}.mp4")
    cmd = [FFMPEG, "-y",
           "-stream_loop", "-1", "-i", music,
           "-stream_loop", "-1", "-i", clip,
           "-i", overlay_png,
           "-filter_complex",
           "[1:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920[scaled];[scaled][2:v]overlay=0:0[out]",
           "-map", "[out]", "-map", "0:a",
           "-af", "volume=0.8",
           "-t", "5.0", "-frames:v", "150", "-r", "30",
           "-c:v", "libx264", "-c:a", "aac", "-b:a", "128k",
           "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p",
           mp4_path]
    result = subprocess.run(cmd, capture_output=True)
    if result.returncode == 0:
        size = os.path.getsize(mp4_path) / 1024 / 1024
        print(f"  ✅ MP4: {mp4_path} ({size:.1f}MB)")
    else:
        print(f"  ERROR: {result.stderr[-300:].decode()}")
        return False
    final_bg = f"/tmp/final_bg_{rid}.jpg"
    subprocess.run([FFMPEG, "-y", "-ss", "2", "-i", mp4_path, "-vframes", "1", final_bg], capture_output=True)
    draw_overlay(final_bg, lines, os.path.join(OUT_DIR, f"{rid}_final.jpg"))
    return True


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
    print(f"Done: {len(success)}/10 reels rendered")
    print(f"Output: {OUT_DIR}")
