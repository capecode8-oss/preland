---
name: kira-hooks
description: Write viral Instagram Reel hooks for @thekiramethod AND enforce face clearance on every clip. Use for every reel — hooks + face check are inseparable steps.
---

# KIRA Viral Hook Writer + Face Clearance

## PROVEN HOOKS — TOP 10 (memorize these as the gold standard)

These are the exact hooks that work. Every new hook must match this level:

```
1. She Found Lipstick In His Coat Pocket.
   It Was Her Shade. But Not Her Lipstick.
   ( She'd never owned that brand ↓ )

2. He Cried At Their Wedding Video.
   She Later Found Out Why.
   ( He wasn't thinking about her ↓ )

3. His Phone Showed 47 Missed Calls.
   All From The Same Unsaved Number.
   ( She called it back ↓ )

4. She Found A Birthday Card In His Drawer.
   It Wasn't Her Birthday.
   ( Her name wasn't in it ↓ )

5. He Forgot To Log Out On Her Laptop.
   She Wasn't Going To Look.
   ( She looked ↓ )

6. He Said The Trip Was For Work.
   She Found The Booking Confirmation.
   ( Two guests. One room. Her name wasn't on it ↓ )

7. Their Couple's Therapist Called Her Privately.
   She'd Never Spoken To Her Before.
   ( The therapist had heard his side ↓ )

8. He Came Home Smelling Like Her Perfume.
   She Doesn't Wear Perfume.
   ( She recognized the scent ↓ )

9. He Asked Her To Delete Find My Friends.
   Said It Felt Controlling.
   ( She checked his location first ↓ )

10. She Found A Second Set Of House Keys.
    They'd Never Made A Copy.
    ( The key still opened their front door ↓ )
```

---

## THE ALGORITHM — how every hook is built

**Line 1:** Specific physical object or action. Concrete. Real. ≤8 words.
- Object: lipstick, keys, card, phone, confirmation, receipt, perfume
- Action: found, called, checked, forgot, asked, cried

**Line 2:** The twist. Subverts what Line 1 set up. Creates the gap. ≤8 words.
- Formula: [subject] + [contradiction of expectation]
- "It Was Her Shade. But Not Her Lipstick." — same but different
- "She Wasn't Going To Look." — internal conflict
- "She Doesn't Wear Perfume." — impossibility
- "They'd Never Made A Copy." — logical contradiction

**CTA badge (parentheses):** One more detail that raises stakes even higher.
- Never explains everything — reveals just enough to make it unbearable not to read
- Short, punchy, specific
- Always ends with ↓
- Formula: ( [one concrete fact that changes everything] ↓ )

**The gap:** Reader knows WHAT happened (Line 1) + knows it's WRONG (Line 2) + the CTA tells them it gets WORSE → they MUST open caption

---

## STEP 1 — FACE CLEARANCE (always before text placement)

1. Extract 5 frames: t = 0.25, 1.25, 2.50, 3.75, 4.75s
2. View ALL 5 — find face bbox in each frame
3. UNION across all frames: face_top = min, face_bottom = max
4. forbidden_top = face_top − 70, forbidden_bottom = face_bottom + 70
5. Placement:
   - BELOW: hook_y0 ≥ forbidden_bottom AND cta_bottom ≤ 1600 ✅
   - ABOVE: hook_y0 ≥ 80 AND cta_bottom ≤ forbidden_top ✅
   - Neither fits → change clip
6. QA: center=540±2px, box_w≤1060px, cta_bottom≤1600px

**NEVER skip. NEVER use one frame. NEVER guess.**

---

## STEP 2 — OUTPUT FORMAT

```
Clip: 1_X
face_union: y=TOP–BOTTOM
forbidden_zone: y=FORBIDDEN_TOP–FORBIDDEN_BOTTOM
text_y: VALUE (ABOVE / BELOW)
QA: center=540 box_w=XXX cta_bottom=XXX ✅

hook_lines: [
    "Line 1.",
    "Line 2.",
]
cta_badge: "( Parenthetical detail ↓ )"
```

Always write 3–5 variants. User picks one. Then render.
