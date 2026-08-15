---
name: kira-hooks
description: Write viral Instagram Reel hooks for @thekiramethod in competitor style (maks.motivator format) AND enforce face clearance on every clip. Use for every reel — hooks + face check are inseparable steps.
---

# KIRA Hook Writer — Competitor Format (maks.motivator style)

## NICHE PIVOT — NEW DIRECTION

**STOP**: relationship drama / cheating / "She found..." hooks — DELETED.  
**NEW**: Travel hacks, life hacks, food facts, health warnings, money traps. Universal topics only.

**Why**: shares are weighted 3–5× higher than likes by Instagram algorithm.  
Relationship drama = nobody shares. Travel hack = everyone forwards to a friend.

---

## GOLD STANDARD — TOP COMPETITOR HOOKS (memorize)

These are the exact style to match. Study the structure, not the topic:

```
1. "Never Do This While Waiting for Your Luggage"
   → 1.9M views. Short. Direct command. Creates fear of mistake.

2. "My friend lost $14,000 at customs for money he earned legally.
   One question on a form cost him everything."
   → 900K views. First person. Specific number. Real consequence.

3. "Hotel charged me $40 for a 'missing' towel I never touched.
   One reply killed it in 5 minutes. 👇"
   → 378K views. Personal experience. Injustice. Actionable payoff.

4. "Ever notice how flight crews always walk through the airport
   in a tight single-file line? I asked a flight attendant why.
   This is what she told me."
   → 253K views. Observation everyone has had. Answer withheld.

5. "One spice sitting in your kitchen right now could be doing
   150 times less for your brain than it should be.
   The reason is how much you're actually using."
   → 14.2K views. Universal (kitchen). Specific number. Fear of doing it wrong.

6. "A local stopped me before I stepped onto a beach in Bali.
   What she told me next is why tourists get pulled out to sea there every year."
   → Personal story. Fear of death. Hyper-specific location.
```

---

## THE ALGORITHM — how every hook is built

### HOOK TYPE (choose one per reel)

**Type A — Personal Warning** ("I did X. Then I found out...")
- First person. Real consequence. Reader thinks: "this could be me."
- Best for: hotel tricks, airport hacks, money traps, customs, scams

**Type B — Insider Secret** ("Ever notice X? Here's why...")
- Observation everyone has made but never questioned.
- Best for: flight crew behavior, airport design, food facts, body hacks

**Type C — Specific Fear** ("Never do X." / "Stop doing X.")
- Direct command. Short. Creates immediate anxiety about current behavior.
- Best for: luggage belt, phone habits, health warnings, travel mistakes

**Type D — Specific Number Shock** ("My friend lost $14,000..." / "150 times less...")
- Concrete number changes everything. Reader recalibrates their world.
- Best for: fees, fines, health stats, food quantities, time/money

---

## HOOK STRUCTURE

**Line 1:** The setup. Specific, real, first-person or second-person.
- Use "I", "my friend", "A local told me", "Ever notice" — NOT "She", "He"
- Include a specific number, place, or object when possible
- ≤12 words

**Line 2 (optional):** The gap. What happened that makes no sense yet.
- Subverts expectation from Line 1
- ≤10 words

**CTA badge:** Hides the payoff. Forces caption read.
- Formula: ( [one concrete detail that raises stakes even higher] ↓ )
- Never explains everything
- Always ends with ↓

---

## TOPIC BANK — use these, rotate weekly

### TRAVEL
- Airport luggage belt theft window (thieves operate in 90-second window)
- Hotel hidden rate / "rack rate" (say two words at check-in)
- Hotel towel charge disputes (one email kills the charge)
- EU flight delay compensation €250–€600 (most passengers never claim)
- Window seat radiation (equivalent to chest X-rays on long flights)
- Airline food order hack (special meals served first, better quality)
- Customs declaration mistakes (wrong checkbox = confiscation)
- Gate volunteer bump ($400–$800 + hotel for raising hand)
- Flight crew single-file walking (protocol reason)
- Cruise cabin location (mid-ship deck 3 = no seasickness)
- Airport priority lane trick (business lounge day pass = $40)

### FOOD & HEALTH
- Spice storage mistake (light/heat degrades potency 150×)
- Blue Zone breakfast (Sardinia/Okinawa longevity foods)
- Earbuds + busy streets (3× hearing loss risk per doctor research)
- Body clock meals (eating same food at wrong time = 40% worse effect)
- Supermarket layout psychology (perimeter = real food, center = traps)

### MONEY TRAPS
- Hotel "missing" towel charge (dispute process)
- Rental car insurance overlap (credit card already covers it)
- Airport currency exchange (worst rate in the building — use ATM inside)
- Roaming charges hack (buy eSIM before landing = 90% cheaper)

---

## SELF-TEST BEFORE WRITING (mandatory — apply every time)

Ask yourself as a viewer scrolling at 11pm:

1. **Would I stop scrolling?** If no → rewrite.
2. **Would I send this to a friend?** If no → wrong topic or too niche.
3. **Does it make me feel like I'm missing something I should know?** If no → no fear of loss, rewrite.
4. **Is there a concrete number or specific detail?** Vague = weak. Add specificity.
5. **Is it first person or direct address ("you")?** Third person ("she/he") = weaker. Rewrite.

---

## STEP 1 — FACE CLEARANCE (always before text placement)

1. Extract 5 frames: t = 0.25, 1.25, 2.50, 3.75, 4.75s
2. View ALL 5 — find face bbox in each frame
3. UNION across all frames: face_top = min, face_bottom = max
4. forbidden_top = face_top − 70, forbidden_bottom = face_bottom + 70
5. Placement:
   - BELOW: hook_y0 ≥ forbidden_bottom AND cta_bottom ≤ 1536 ✅
   - ABOVE: hook_y0 ≥ 80 AND cta_bottom ≤ forbidden_top ✅
   - Neither fits → change clip
6. QA: center=540±2px, box_w≤860px, cta_bottom≤1536px

**NEVER skip. NEVER use one frame. NEVER guess.**

---

## RENDER SPECS

- Font: Montserrat-BlackItalic, auto_font max_size=100px (target 60–80px)
- Hook box: white FILL=(255,255,255,245), RADIUS=14, PAD_X=32, PAD_Y=22
- CTA box: same style, BOX_GAP=20px below hook box
- Canvas: 1080×1920, CENTER_X=540, MAX_BOX_W=860px
- Duration: 150 frames = 5s at 30fps (loop shorter clips)

---

## STEP 2 — OUTPUT FORMAT

```
Topic: [what this reel is about]
Type: [A / B / C / D]
Clip: [filename]
face_union: y=TOP–BOTTOM
forbidden_zone: y=FORBIDDEN_TOP–FORBIDDEN_BOTTOM
text_y: VALUE (ABOVE / BELOW)
QA: center=540 box_w=XXX cta_bottom=XXX ✅

hook_lines: [
    "Line 1.",
    "Line 2.",          ← optional
]
cta_badge: "( Detail that hides the payoff ↓ )"
```

Always write 3–5 variants. Self-test each one. User picks one. Then render.
Show JPG preview before scheduling. Always.
