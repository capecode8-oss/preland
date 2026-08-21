#!/usr/bin/env python3
"""
SOLID BOX render — one continuous white rectangle for all hook lines.
Position: bottom area but ABOVE Instagram UI chrome (~200px from bottom).
BOTTOM_ANCHOR = 1680 (Instagram UI starts ~1700px)
"""
import subprocess, os, random, glob
from PIL import Image, ImageDraw, ImageFont

MUSIC_DIR = "/home/user/preland/music"

FFMPEG = "/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2"
FONT_PATH = "/tmp/montserrat_extract/usr/share/fonts/truetype/montserrat/Montserrat-BlackItalic.ttf"
FOOTAGE = "/home/user/preland/footage"
RENDERED = "/home/user/preland/footage/rendered"

W, H = 1080, 1920
CENTER_X = 540
MAX_BOX_W = 860         # HARD LIMIT — никогда не менять
MAX_TEXT_W = 760        # MAX_BOX_W - PAD_X*2 - 36px safety margin
PAD_X = 32
PAD_TOP = 28
PAD_BOTTOM = 28
LINE_GAP = 8
FILL = (255, 255, 255, 248)
RADIUS = 18
BOTTOM_ANCHOR = 1550


def wrap_lines(lines, fnt):
    """Auto-wrap any line that exceeds MAX_TEXT_W."""
    result = []
    for line in lines:
        if fnt.getlength(line) <= MAX_TEXT_W:
            result.append(line)
        else:
            # split into words and wrap
            words = line.split()
            current = ""
            for w in words:
                test = (current + " " + w).strip()
                if fnt.getlength(test) <= MAX_TEXT_W:
                    current = test
                else:
                    if current:
                        result.append(current)
                    current = w
            if current:
                result.append(current)
    return result


def auto_font(lines, max_size=70, min_size=50):
    for size in range(max_size, min_size - 1, -1):
        fnt = ImageFont.truetype(FONT_PATH, size)
        wrapped = wrap_lines(lines, fnt)
        if all(fnt.getlength(l) <= MAX_TEXT_W for l in wrapped):
            return fnt, size, wrapped
    fnt = ImageFont.truetype(FONT_PATH, min_size)
    return fnt, min_size, wrap_lines(lines, fnt)


def render_overlay(lines, cta=None):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # --- SOLID BOX for hook lines ---
    fnt, size, lines = auto_font(lines)
    line_h = size
    total_text_h = len(lines) * line_h + (len(lines) - 1) * LINE_GAP
    box_h = PAD_TOP + total_text_h + PAD_BOTTOM

    # Determine box width = widest line + padding (HARD LIMIT MAX_BOX_W)
    max_tw = max(fnt.getlength(l) for l in lines)
    box_w = min(max_tw + PAD_X * 2, MAX_BOX_W)
    bx = CENTER_X - box_w / 2

    # Position: bottom of box at BOTTOM_ANCHOR
    # If there's a CTA badge, leave room for it below
    if cta:
        cta_fnt = ImageFont.truetype(FONT_PATH, 40)
        cta_h = 40 + 20 * 2  # font + pad
        cta_gap = 14
        hook_box_bottom = BOTTOM_ANCHOR - cta_gap - cta_h
    else:
        hook_box_bottom = BOTTOM_ANCHOR

    hook_y0 = hook_box_bottom - box_h

    print(f"  Font: {size}px | box: {box_w:.0f}x{box_h}px")
    print(f"  hook_y0: {hook_y0:.0f}px | hook_box_bottom: {hook_box_bottom:.0f}px")

    # Draw ONE solid rounded rectangle
    draw.rounded_rectangle([bx, hook_y0, bx + box_w, hook_box_bottom], radius=RADIUS, fill=FILL)

    # Draw each line of text inside the box
    y_text = hook_y0 + PAD_TOP
    for line in lines:
        tw = fnt.getlength(line)
        draw.text((CENTER_X - tw / 2, y_text), line, font=fnt, fill=(0, 0, 0, 255))
        y_text += line_h + LINE_GAP

    # --- Optional CTA badge (separate small box below) ---
    if cta:
        cta_fnt = ImageFont.truetype(FONT_PATH, 40)
        ctw = cta_fnt.getlength(cta)
        cbw = min(ctw + PAD_X * 2, MAX_BOX_W)
        cbh = 40 + 20 * 2
        cbx = CENTER_X - cbw / 2
        cta_y = hook_box_bottom + cta_gap
        draw.rounded_rectangle([cbx, cta_y, cbx + cbw, cta_y + cbh], radius=RADIUS, fill=FILL)
        draw.text((CENTER_X - ctw / 2, cta_y + 20), cta, font=cta_fnt, fill=(0, 0, 0, 255))
        print(f"  cta_bottom: {cta_y + cbh:.0f}px")
    else:
        print(f"  cta_bottom (= hook_bottom): {hook_box_bottom:.0f}px")

    return img


def render_reel(clip_name, slug, lines, cta=None, date="2026-08-20"):
    clip = f"{FOOTAGE}/{clip_name}.mp4"
    out_mp4 = f"{RENDERED}/{date}_{slug}.mp4"
    out_jpg = f"{RENDERED}/{date}_{slug}.jpg"

    overlay = render_overlay(lines, cta)
    overlay_path = f"/tmp/{slug}_solid_overlay.png"
    overlay.save(overlay_path)

    cmd = [
        FFMPEG, "-y",
        "-stream_loop", "-1", "-i", clip,
        "-i", overlay_path,
        "-filter_complex",
        "[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30[bg];"
        "[1:v]scale=1080:1920[ov];"
        "[bg][ov]overlay=0:0",
        "-t", "5.000",
        "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p",
        "-an", "-crf", "18", "-preset", "fast",
        "-frames:v", "150",
        out_mp4
    ]
    r = subprocess.run(cmd, capture_output=True)
    if r.returncode != 0:
        print(f"  ERROR: {r.stderr.decode()[-300:]}")
        return False

    subprocess.run([FFMPEG, "-y", "-i", out_mp4, "-vframes", "1", "-ss", "0.5", out_jpg], capture_output=True)
    mb = os.path.getsize(out_mp4) / 1024 / 1024
    print(f"  ✅ {slug} ({mb:.1f}MB)")
    return True


def render_reel_youtube(clip_name, slug, lines, music_path, cta=None, date="2026-08-21"):
    """Render YouTube Short — same as render_reel but with audio mixed in."""
    clip = f"{FOOTAGE}/{clip_name}.mp4"
    out_mp4 = f"{RENDERED}/{date}_{slug}_yt.mp4"
    out_jpg = f"{RENDERED}/{date}_{slug}_yt.jpg"

    overlay = render_overlay(lines, cta)
    overlay_path = f"/tmp/{slug}_yt_overlay.png"
    overlay.save(overlay_path)

    cmd = [
        FFMPEG, "-y",
        "-stream_loop", "-1", "-i", clip,
        "-i", overlay_path,
        "-stream_loop", "-1", "-i", music_path,
        "-filter_complex",
        "[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30[bg];"
        "[1:v]scale=1080:1920[ov];"
        "[bg][ov]overlay=0:0[outv]",
        "-map", "[outv]", "-map", "2:a",
        "-t", "5.000",
        "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-crf", "18", "-preset", "fast",
        "-frames:v", "150",
        out_mp4
    ]
    r = subprocess.run(cmd, capture_output=True)
    if r.returncode != 0:
        print(f"  ERROR: {r.stderr.decode()[-300:]}")
        return False

    subprocess.run([FFMPEG, "-y", "-i", out_mp4, "-vframes", "1", "-ss", "0.5", out_jpg], capture_output=True)
    mb = os.path.getsize(out_mp4) / 1024 / 1024
    track = os.path.basename(music_path)
    print(f"  ✅ {slug}_yt ({mb:.1f}MB) | 🎵 {track}")
    return True


def pick_music_for_batch(n):
    """Pick n unique random tracks from MUSIC_DIR for one day's batch."""
    tracks = sorted(glob.glob(f"{MUSIC_DIR}/*.mp3"))
    if len(tracks) < n:
        tracks = tracks * (n // len(tracks) + 1)
    return random.sample(tracks, n)


# ── BATCH Aug 20 ────────────────────────────────────────────
reels = [
    {
        "clip": "1_2", "slug": "luggage-theft-window",
        "lines": ["I watched a man take my bag", "off the belt before I could get there.", "He knew exactly how long I had."],
        "cta": None,
    },
    {
        "clip": "1_3", "slug": "window-seat-xrays",
        "lines": ["Window Seat Gives You", "2 Chest X-Rays Per Flight."],
        "cta": "( What pilots actually do ↓ )",
    },
    {
        "clip": "1_4", "slug": "fa-greeting-screening",
        "lines": ["Flight Attendants Greet You", "To Screen You. Not Be Nice."],
        "cta": "( What they're actually checking ↓ )",
    },
    {
        "clip": "1_5", "slug": "airport-thief-target",
        "lines": ["Airport thieves don't want your passport.", "A security officer told me", "what they actually take — and when."],
        "cta": None,
    },
    {
        "clip": "1_6", "slug": "doctor-radiation-story",
        "lines": ["My doctor told me to stop", "booking window seats after", "seeing my bloodwork."],
        "cta": None,
    },
]

for i, r in enumerate(reels, 1):
    print(f"\nReel {i}/5 — {r['slug']}")
    render_reel(r["clip"], r["slug"], r["lines"], r.get("cta"))

print("\n=== DONE ===")
