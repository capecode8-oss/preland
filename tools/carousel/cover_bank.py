#!/usr/bin/env python3
"""Cover bank: frames from our own footage (one recurring character), one soft color grade, rotation without repeats.

  python3 tools/carousel/cover_bank.py build            # (re)render assets/covers/*.jpg + manifest.json
  python3 tools/carousel/cover_bank.py list [product]   # show bank with last-used dates
  python3 tools/carousel/cover_bank.py pick safety airport   # preview what the next pick would be (does not log)
"""
import json, shutil, subprocess, sys, tempfile, datetime
from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[2]
FOOTAGE = ROOT / "footage"
OUT = ROOT / "assets" / "covers"
MANIFEST = OUT / "manifest.json"
MANIFEST_GEN = OUT / "manifest_gen.json"
USAGE = OUT / "usage_log.json"
W, H = 1080, 1350

# id, clip (relative to footage/), t seconds, products, tags, top offset (crop from top of the 9:16 frame)
SPECS = [
    # airport / plane
    ("airport_wait_1", "travel/32_1", 2, ["safety"], ["airport", "waiting"], 120),
    ("airport_wait_2", "travel/32_4", 2, ["safety"], ["airport", "waiting"], 120),
    ("airport_walk_1", "travel/32_9", 2, ["safety"], ["airport", "walking"], 120),
    ("airport_walk_2", "travel/32_11", 2, ["safety"], ["airport", "walking"], 120),
    ("airport_exit", "travel/32_12", 2, ["safety"], ["airport", "exit", "taxi"], 120),
    ("baggage_1", "travel/32_18", 2, ["safety"], ["airport", "baggage"], 120),
    ("baggage_2", "travel/1_5", 2, ["safety"], ["airport", "baggage"], 120),
    ("airport_escalator", "travel/1_29", 2, ["safety"], ["airport", "happy"], 60),
    ("plane_window_1", "travel/32_5", 2, ["safety"], ["plane", "window"], 120),
    ("plane_sleeping", "travel/1_10", 2, ["safety", "glow"], ["plane", "sleep", "tired"], 60),
    ("plane_window_2", "travel/1_27", 2, ["safety", "glow"], ["plane", "tired"], 60),
    # hotel
    ("hotel_reception", "travel/32_6", 2, ["safety"], ["hotel", "reception"], 120),
    ("hotel_room", "travel/32_7", 2, ["safety", "glow"], ["hotel", "bedroom", "sleep"], 60),
    ("hotel_phone_night", "travel/custom_insurance", 2, ["safety", "glow"], ["hotel", "phone", "worried"], 60),
    # cruise
    ("cruise_cabin", "travel/32_13", 2, ["safety"], ["cruise", "cabin"], 120),
    ("cruise_evening", "travel/32_14", 2, ["safety"], ["cruise", "deck"], 120),
    ("cruise_terrace", "travel/32_15", 2, ["safety"], ["cruise", "cafe"], 120),
    ("cruise_rail", "travel/32_16", 2, ["safety"], ["cruise", "railing"], 120),
    ("cruise_port", "travel/32_17", 2, ["safety"], ["cruise", "port"], 120),
    # taxi / car
    ("taxi_1", "travel/31_1", 2, ["safety"], ["taxi", "car"], 60),
    ("taxi_2", "travel/31_3", 2, ["safety", "glow"], ["taxi", "tired", "worried"], 60),
    ("car_coast", "general/1_14", 2, ["safety"], ["car", "driving"], 60),
    ("car_smile", "general/1_16", 2, ["safety"], ["car", "driving"], 60),
    ("car_night", "general/1_15", 2, ["safety"], ["car", "driving", "night"], 60),
    ("rental_counter", "travel/custom_rental", 2, ["safety"], ["rental", "paperwork"], 60),
    # street / places
    ("street_tokyo", "travel/1_4", 2, ["safety"], ["street", "crowd"], 120),
    ("street_night", "travel/1_24", 2, ["safety"], ["street", "night"], 60),
    ("market", "general/1_28", 2, ["safety"], ["street", "market", "crowd"], 120),
    ("cafe_tokyo", "travel/32_8", 2, ["safety", "glow"], ["cafe", "thinking"], 60),
    ("moto_ride", "travel/1_6", 2, ["safety"], ["street", "happy"], 60),
    ("restaurant_bill", "travel/custom_restaurant", 2, ["safety"], ["restaurant", "money", "bill"], 60),
    ("pharmacy", "travel/custom_pharmacy", 2, ["safety", "glow"], ["pharmacy", "reading", "worried"], 60),
    ("atm_hands_1", "travel/custom_atm_1", 2, ["safety"], ["atm", "money", "hands"], 120),
    ("atm_hands_2", "travel/custom_atm_2", 2, ["safety"], ["atm", "money", "hands"], 120),
    ("customs_pov", "travel/custom_customs", 2, ["safety"], ["customs", "passport", "pov"], 120),
    ("selfie_rio", "travel/32_3", 2, ["safety"], ["selfie", "happy", "view"], 60),
    ("selfie_canyon", "general/1_23", 2, ["safety"], ["selfie", "happy", "view"], 60),
    ("vacation_beach", "general/1_30", 2, ["safety", "glow"], ["beach", "happy"], 60),
    ("vacation_sunset", "general/1_26", 2, ["safety", "glow"], ["sunset", "calm"], 60),
    # GLOW: faces and everyday
    ("face_2", "general/face_2", 1, ["glow"], ["face", "serious", "indoor"], 260),
    ("face_3", "general/face_3", 1, ["glow"], ["face", "serious", "garden"], 300),
    ("face_5", "general/face_5", 1, ["glow"], ["face", "serious", "brick"], 100),
    ("train_eyes_closed", "general/31_2", 2, ["glow"], ["train", "tired", "eyes-closed"], 60),
    ("subway_reading", "general/32_2", 2, ["glow"], ["subway", "calm", "reading"], 60),
    ("eating_pasta_1", "general/1_2", 2, ["glow"], ["food", "eating", "happy"], 60),
    ("eating_pasta_2", "general/1_8", 2, ["glow"], ["food", "eating", "happy"], 60),
]


def _ffmpeg():
    ff = shutil.which("ffmpeg")
    if ff:
        return ff
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


def grade(im):
    """One soft warm tone for the whole bank so the grid looks like one account."""
    r, g, b = im.split()
    r = r.point(lambda v: min(255, int(v * 1.04 + 2)))
    b = b.point(lambda v: int(v * 0.95))
    im = Image.merge("RGB", (r, g, b))
    im = ImageEnhance.Color(im).enhance(0.94)
    return ImageEnhance.Contrast(im).enhance(1.03)


def build():
    OUT.mkdir(parents=True, exist_ok=True)
    ff = _ffmpeg()
    manifest = []
    for cid, clip, t, products, tags, top in SPECS:
        src = FOOTAGE / f"{clip}.mp4"
        if not src.exists():
            print("missing", src)
            continue
        tmp = tempfile.mktemp(suffix=".jpg")
        subprocess.run([ff, "-y", "-loglevel", "error", "-ss", str(t), "-i", str(src), "-vframes", "1", tmp], check=True)
        im = Image.open(tmp).convert("RGB")
        sc = max(W / im.width, H / im.height)
        im = im.resize((int(im.width * sc) + 1, int(im.height * sc) + 1))
        tp = max(0, min(top, im.height - H))
        lf = (im.width - W) // 2
        im = grade(im.crop((lf, tp, lf + W, tp + H)))
        im.save(OUT / f"{cid}.jpg", quality=92)
        manifest.append(dict(id=cid, file=f"{cid}.jpg", source=f"footage/{clip}.mp4@{t}s", products=products, tags=tags))
    MANIFEST.write_text(json.dumps(manifest, indent=1), encoding="utf-8")
    print(len(manifest), "covers ->", OUT)


def _load(p, default):
    try:
        return json.loads(Path(p).read_text())
    except Exception:
        return default


def pick(product, tags=None, log=True, avoid_days=14, exclude_tags=None, only_id=None):
    """Least recently used cover for the product; prefers tag matches; never reuses within avoid_days while others exist."""
    manifest = _load(MANIFEST, []) + _load(MANIFEST_GEN, [])
    usage = _load(USAGE, {})
    pool = list(manifest) if product in ("any", "all") else [m for m in manifest if product in m["products"]]
    if only_id:
        pool = [m for m in manifest if m["id"] == only_id] or pool
    elif exclude_tags:
        pool = [m for m in pool if not set(exclude_tags) & set(m["tags"])] or pool
    if tags:
        tagged = [m for m in pool if set(tags) & set(m["tags"])]
        pool = tagged or pool
    if not pool:
        raise SystemExit(f"no covers for product={product}")
    today = datetime.date.today()

    def age(m):
        last = usage.get(m["id"])
        return (today - datetime.date.fromisoformat(last)).days if last else 10**6

    fresh = [m for m in pool if age(m) >= avoid_days] or pool
    choice = max(fresh, key=age)
    if log:
        usage[choice["id"]] = today.isoformat()
        USAGE.write_text(json.dumps(usage, indent=1), encoding="utf-8")
    return OUT / choice["file"], choice


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "list"
    if cmd == "build":
        build()
    elif cmd == "list":
        usage = _load(USAGE, {})
        for m in _load(MANIFEST, []) + _load(MANIFEST_GEN, []):
            if len(sys.argv) > 2 and sys.argv[2] not in m["products"]:
                continue
            print(f"{m['id']:<20} {','.join(m['products']):<12} {','.join(m['tags']):<34} last={usage.get(m['id'], '-')}")
    elif cmd == "pick":
        path, m = pick(sys.argv[2], sys.argv[3:] or None, log=False)
        print(path, m["tags"])
