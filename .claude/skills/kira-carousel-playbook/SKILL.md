---
name: kira-carousel-playbook
description: Rules for building Instagram carousels for @thekiramethod (7 slides, product GLOW). Use for EVERY carousel, together with the Hook Atlas standard in CLAUDE.md. Covers cover hook, strong second-hook slide 2, one consistent visual style, send-test, fact verification, caption, weekly review. If a rule here conflicts with a hard rule in CLAUDE.md (no "free", no hashtags, no price, no invented facts), CLAUDE.md wins.
---

# KIRA Carousel Playbook (v2026-10-18)

Full machine-readable rules: `playbook.json` in this folder (owner-supplied, read it before building).

## Where it sits in the pipeline
topic (donor outliers / Reddit radar) -> verify every fact by search -> hook (cover) -> slide 2 second hook -> slides 3-6 -> slide 7 CTA -> caption -> preview to owner -> Videotool (one post at a time) -> performance-tracker / weekly review.

## North star
DM sends per reach. Then saves per reach, completion, follows per reach, GLOW comments per reach. Likes are the weakest signal.

## Slide rules (7 slides by default, 1080x1350)
- S1 cover: strong scene/photo + long hook (20-40 words: setup + twist + open loop ending in ":" or arrow). Most visual effort goes here.
- S2 SECOND HOOK: must be strong and work without S1. A standalone sharp fact or scene, not "point #1".
- S3: strongest insight, no later than slide 3.
- S4: drop-off zone, mini-loop line + soft "SAVE THIS" prompt.
- S5: practice or payoff with a number or object.
- S6: turn toward the reader's own body/self-care (bridge, no product name yet).
- S7: CTA: name the product (THE GLOW HEALTH BUNDLE), name the code word, promise the DM. One main action.
- One idea per slide, max 20 words per slide, max 15 words per sentence, plain 8th-grade American English.
- Whatever the cover promises must be delivered. Open loop without payoff burns trust.

## ONE CONSISTENT VISUAL STYLE (owner requirement)
All slides 2-7 use the same template so the series is recognizable: beige background (252,249,245), Montserrat Black large dark text, one terracotta accent (180,110,60), same tag chips and progress dots, same margins. The cover is the only slide with a photo. Do not mix styles inside one carousel or across a batch. Rendering tool: `tools/carousel/gen_atlas_five.py`.

## Hook rules
- Send test: name the exact person who would receive it ("Jennifer DMs it to her sister"). If you cannot, rewrite.
- Formulas: credentialed source + quote + number + promise; scene + years + open loop; fact-hook object + number + gap + colon.
- NEVER: invented quotes or insiders, AI persona presented as a real professional to sell a product, AI scenes presented as real incidents (label reenactments), someone else's photo or story without license.
- Every number, study, quote and credential verified by search first. Use wording the source supports and add one honest-caveat line.

## Topics
Broad emotional topics beat lectures: family, marriage, mothers and grandmothers, scams, insiders, travel, money, age and shame, everyday objects. Body/science directly: max 1 in 5, only as story or verified fact-hook. Bridge: topic -> S6 turn -> GLOW on S7 and in caption. Track GLOW comments per reach by topic category; drop categories that do not convert. Never repeat the same format twice in a day or batch.

## Caption
1700-1900 chars (measure with len()). Order: second hook (differs from cover, under ~125 chars before the fold) -> context -> sourced facts -> honest note with limits -> bridge -> `📌 Save this before your next ...` -> GLOW CTA block exactly:
```
👇 HOW TO GET IT: 👇
• FOLLOW this account 🔒
• COMMENT GLOW below 💬
I'll send it straight to your DMs.
```
Forbidden: "free", hashtags, price, "link in bio" for GLOW, emoji on slide images.

## Production
- Image generation off unless the owner asks (cost). Use cover bank / footage frames / owner-supplied images.
- Create posts one at a time. After any timeout check getCarouselPosts before retrying. Published or scheduled posts cannot be edited or deleted via API, so review slides and caption BEFORE creating the post.
- Videotool needs 2-10 items per carousel: always 7 slides.
- One hour between posts unless the owner says otherwise.

## A/B test (run 2 weeks)
5 carousels with fully illustrated slides vs 5 with strong cover + simple template slides. Keep the cheaper format unless the expensive one wins sends per reach by at least 30%.

## Weekly review
Table: post | format | topic category | reach | sends | saves | follows | GLOW comments | completion. Rank by sends per reach, repeat the top format and category, drop categories with reach but no GLOW comments, update HYPOTHESIS items with our own data.

## Honesty contract
Separate facts, hypotheses and unknowns in every recommendation. Do not guess follower or sales outcomes. Challenge weak assumptions.
