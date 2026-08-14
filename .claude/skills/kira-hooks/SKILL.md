---
name: kira-hooks
description: Write viral Instagram Reel hooks for @thekiramethod AND enforce face clearance on every clip. Use for every reel — hooks + face check are inseparable steps.
---

# KIRA Viral Hook Writer + Face Clearance

## STEP 1 — FACE CLEARANCE (mandatory, always first)

Before writing any hook or placing any text, run this check on the chosen clip:

1. Extract 5 frames at t = 0.25, 1.25, 2.50, 3.75, 4.75s
2. Look at ALL 5 frames — find the face bounding box in each
3. Take the UNION (worst case across all frames):
   - face_top = minimum y of face top across all frames
   - face_bottom = maximum y of face bottom across all frames
4. Add 70px padding: forbidden_top = face_top − 70, forbidden_bottom = face_bottom + 70
5. Text placement rule:
   - ABOVE: hook_y0 ≥ 80 AND cta_bottom ≤ forbidden_top → place text in top zone
   - BELOW: hook_y0 ≥ forbidden_bottom AND cta_bottom ≤ 1600 → place text in bottom zone
   - NEITHER fits → pick a different clip, repeat from step 1
6. QA checklist before rendering:
   - center = 540px ± 2px ✅
   - box_w ≤ 1060px ✅
   - cta_bottom ≤ 1600px ✅
   - hook_y0 ≥ forbidden_bottom (or ≤ forbidden_top) ✅

**NEVER skip this. NEVER eyeball one frame. NEVER place text without running all 5 frames.**

---

## STEP 2 — HOOK FORMAT (curiosity gap)

**Structure: 2 lines + CTA badge in parentheses**

```
Line 1: The specific discovery / concrete detail
Line 2: The twist that flips expectation
( The detail that makes them NEED to read caption ↓ )
```

**Rules:**
- ≤ 8 words per line
- Concrete specific detail — not vague
- Line 2 SUBVERTS what Line 1 set up
- CTA badge in parentheses adds one more layer of intrigue
- NO arrows → in lines 1–2
- NO narrative sentences

**Proven examples (high performers):**
```
She Found A Second Phone In His Car.
The Messages Weren't From Another Woman.
( The last message was worse ↓ )
— 23.5K views

What He Found In Her Locked Desk Ended Their Marriage.
( read captions )
— 107K views
```

**Topic bank (infidelity/marriage/betrayal):**
- Second phone / work phone
- Hotel receipt / booking confirmation
- Location off / fake location
- Unsaved number / name saved wrong
- Second email / inbox
- Keys made without asking
- Anniversary card from someone else
- Lawyer/therapist contacted first
- Perfume that isn't hers
- Birthday card not for her
- Find My Friends / tracking
- Room booked for two
- Lipstick / wrong shade

---

## STEP 3 — OUTPUT FORMAT

Always output:

```
Clip: 1_X
face_union: y=TOP–BOTTOM
forbidden_zone: y=FORBIDDEN_TOP–FORBIDDEN_BOTTOM
text_y: VALUE (ABOVE or BELOW)
QA: center=540 box_w=XXX cta_bottom=XXX ✅

hook_lines: [
    "Line 1.",
    "Line 2.",
]
cta_badge: "( Parenthetical detail ↓ )"
```

Then show 3–5 variants so user can pick the strongest one.
