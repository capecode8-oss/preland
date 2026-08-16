from PIL import Image, ImageDraw, ImageFont
import subprocess, os

FFMPEG = "/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2"
FONT_PATH = "/tmp/montserrat_extract/usr/share/fonts/truetype/montserrat/Montserrat-BlackItalic.ttf"
BASE = "/root/.claude/uploads/3731ce9a-1afe-5ba6-8dc5-3a76d04601bb"
CANVAS_W, CANVAS_H = 1080, 1920
CENTER_X = 540
PAD_X, PAD_Y = 32, 22
RADIUS, BOX_GAP = 14, 20
MAX_BOX_W = 860
MAX_TEXT_W = MAX_BOX_W - PAD_X * 2
FILL = (255, 255, 255, 245)
TEXT_COLOR = (0, 0, 0, 255)

# Aug 18 — 6 reels: 07:00, 10:00, 13:00, 16:00, 19:00, 22:00 NY
reels = [
    {
        "name": "aug18_1",
        "footage": f"{BASE}/01a70f0f-1_2.mp4",
        "face_union": (80, 700),
        "text_y": 1060,
        "hook_lines": [
            "I Stored Spices Wrong.",
            "150× Less Potency.",
        ],
        "cta_badge": "( Light and heat destroy them ↓ )",
    },
    {
        "name": "aug18_2",
        "footage": f"{BASE}/633d85fc-1_3.mp4",
        "face_union": (180, 820),
        "text_y": 1060,
        "hook_lines": [
            "I Almost Got Fined.",
            "One Form. One Box.",
        ],
        "cta_badge": "( Customs agents catch this daily ↓ )",
    },
    {
        "name": "aug18_3",
        "footage": f"{BASE}/db6cf4cd-1_4.mp4",
        "face_union": (290, 900),
        "text_y": 1060,
        "hook_lines": [
            "I Drank Coffee Wrong.",
            "Years Lost.",
        ],
        "cta_badge": "( The cortisol window most people miss ↓ )",
    },
    {
        "name": "aug18_4",
        "footage": f"{BASE}/926d4a6f-1_5.mp4",
        "face_union": (150, 810),
        "text_y": 1060,
        "hook_lines": [
            "Baggage Claim. 90-Second Window.",
            "Thieves Know It.",
        ],
        "cta_badge": "( They grab yours before you reach the belt ↓ )",
    },
    {
        "name": "aug18_5",
        "footage": f"{BASE}/a1f44b2e-1_10.mp4",
        "face_union": (100, 820),
        "text_y": 1060,
        "hook_lines": [
            "I Ordered A Special Meal.",
            "Served First. Better Food.",
        ],
        "cta_badge": "( Anyone can order it. 24 hours before ↓ )",
    },
    {
        "name": "aug18_6",
        "footage": f"{BASE}/c38c1dde-1_16.mp4",
        "face_union": (200, 840),
        "text_y": 1060,
        "hook_lines": [
            "I Paid $40 Insurance.",
            "Card Already Covered It.",
        ],
        "cta_badge": "( Most people pay twice for the same coverage ↓ )",
    },
]


def auto_font(path, max_size, max_width, text_lines):
    size = max_size
    while size > 24:
        f = ImageFont.truetype(path, size)
        if max(f.getbbox(l)[2] - f.getbbox(l)[0] for l in text_lines) <= max_width:
            return f, size
        size -= 1
    return ImageFont.truetype(path, 24), 24


def wrap_text(font, text, max_width):
    words = text.split()
    lines, current = [], []
    for word in words:
        test = " ".join(current + [word])
        if font.getbbox(test)[2] - font.getbbox(test)[0] <= max_width:
            current.append(word)
        else:
            if current:
                lines.append(" ".join(current))
            current = [word]
    if current:
        lines.append(" ".join(current))
    return lines


def make_overlay(r):
    img = Image.new("RGBA", (CANVAS_W, CANVAS_H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    font, fsize = auto_font(FONT_PATH, 100, MAX_TEXT_W, r["hook_lines"])
    cta_font = ImageFont.truetype(FONT_PATH, fsize)
    cta_lines = wrap_text(cta_font, r["cta_badge"], MAX_TEXT_W)

    line_dims = [(font.getbbox(l)[2] - font.getbbox(l)[0], font.getbbox(l)[3] - font.getbbox(l)[1]) for l in r["hook_lines"]]
    max_text_w = max(w for w, h in line_dims)
    line_h = max(h for w, h in line_dims)
    n = len(r["hook_lines"])
    box_w = min(max_text_w + PAD_X * 2, MAX_BOX_W)
    box_h = n * line_h + (n - 1) * 10 + PAD_Y * 2

    cta_line_dims = [(cta_font.getbbox(l)[2] - cta_font.getbbox(l)[0], cta_font.getbbox(l)[3] - cta_font.getbbox(l)[1]) for l in cta_lines]
    cta_max_w = max(w for w, h in cta_line_dims)
    cta_line_h = max(h for w, h in cta_line_dims)
    nc = len(cta_lines)
    cta_box_w = min(cta_max_w + PAD_X * 2, MAX_BOX_W)
    cta_box_h = nc * cta_line_h + (nc - 1) * 8 + PAD_Y * 2

    hook_y0 = r["text_y"]
    hook_y1 = hook_y0 + box_h
    cta_y0 = hook_y1 + BOX_GAP
    cta_y1 = cta_y0 + cta_box_h

    ft, fb = r["face_union"]
    forbidden_bottom = min(1920, fb + 70)
    assert hook_y0 >= forbidden_bottom, f"FACE OVERLAP {r['name']}: hook_y0={hook_y0} < {forbidden_bottom}"
    assert cta_y1 <= 1536, f"CTA too low {r['name']}: {cta_y1}"

    print(f"  {r['name']}: font={fsize}px hook_y0={hook_y0} cta_bottom={cta_y1} box_w={box_w} face_clear=✅")

    bx0 = CENTER_X - box_w // 2
    bx1 = CENTER_X + box_w // 2
    draw.rounded_rectangle([bx0, hook_y0, bx1, hook_y1], radius=RADIUS, fill=FILL)
    ty = hook_y0 + PAD_Y
    for line, (lw, lh) in zip(r["hook_lines"], line_dims):
        draw.text((CENTER_X - lw // 2, ty), line, font=font, fill=TEXT_COLOR)
        ty += lh + 10

    cx0 = CENTER_X - cta_box_w // 2
    cx1 = CENTER_X + cta_box_w // 2
    draw.rounded_rectangle([cx0, cta_y0, cx1, cta_y1], radius=RADIUS, fill=FILL)
    ty = cta_y0 + PAD_Y
    for line, (lw, lh) in zip(cta_lines, cta_line_dims):
        draw.text((CENTER_X - lw // 2, ty), line, font=cta_font, fill=TEXT_COLOR)
        ty += lh + 8

    return img


out_dir = "/home/user/preland"
os.makedirs(out_dir, exist_ok=True)

for r in reels:
    overlay_path = f"/tmp/{r['name']}_overlay.png"
    out_path = os.path.join(out_dir, r["name"] + ".mp4")
    make_overlay(r).save(overlay_path)
    cmd = [
        FFMPEG, "-y",
        "-stream_loop", "-1", "-i", r["footage"],
        "-i", overlay_path,
        "-filter_complex",
        "[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setpts=PTS-STARTPTS,fps=30[bg];"
        "[1:v]scale=1080:1920[ov];"
        "[bg][ov]overlay=0:0[out]",
        "-map", "[out]", "-vframes", "150",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "fast", "-crf", "18",
        "-an", out_path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"  ERROR {r['name']}:", res.stderr[-500:])
    else:
        print(f"  → {out_path} ({os.path.getsize(out_path) / 1024 / 1024:.1f}MB)")
