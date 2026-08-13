# FIND VIRAL IDEAS — Command Reference

## What This Command Does

`FIND VIRAL IDEAS` is a research command for the KIRA Viral Research Agent. When you send this command, the agent runs a full cross-path research session covering all three discovery paths simultaneously and returns the top 20 candidates ranked by viral potential.

This command is defined and executed by the KIRA Viral Research Agent. It is not a script. It is an instruction to an AI agent that has loaded the full KIRA content system context.

---

## Files That Must Be Loaded

The following files must be loaded by the agent before executing this command. The agent loads them automatically during Mandatory Initialization. Do not skip any of them.

### Required (Mandatory Initialization)

| File | Path | Purpose |
|------|------|---------|
| KIRA_ACCOUNT_CONTEXT.md | `kira_pack/01_BRAND/KIRA_ACCOUNT_CONTEXT.md` | Master account context: brand, audience, voice, commercial goals |
| EVERGREEN_CURIOSITY_GAP.md | `kira_pack/02_CONTENT_SYSTEM/EVERGREEN_CURIOSITY_GAP.md` | Full curiosity gap framework, three discovery paths, output format, scoring |
| _SHARED_CONTEXT.md | `kira_pack/03_AGENTS/_SHARED_CONTEXT.md` | Shared agent context: cross-agent rules and conventions |
| viral_pattern_library.md | `kira_pack/02_CONTENT_SYSTEM/viral_pattern_library.md` | Pattern reference library |
| BROAD_REELS_TOPIC_AND_HOOK_SYSTEM.md | `kira_pack/02_CONTENT_SYSTEM/BROAD_REELS_TOPIC_AND_HOOK_SYSTEM.md` | Hook structures and topic territories |
| research_sources.md | `kira_pack/05_RESEARCH/research_sources.md` | Known research sources and prior research guidance |

### Loaded by Reference During Research

| File | Path | Purpose |
|------|------|---------|
| VIRAL_RESEARCH_AGENT.md | `kira_pack/03_AGENTS/VIRAL_RESEARCH_AGENT.md` | The agent's full operating rules and research workflow |

---

## Steps That Execute

When the KIRA Viral Research Agent receives `FIND VIRAL IDEAS`, it executes the following steps in order:

### Step 1 — Mandatory Initialization
Load all required files listed above. Confirm EVERGREEN_CURIOSITY_GAP.md is loaded. Confirm KIRA_ACCOUNT_CONTEXT.md is loaded. Do not begin research without both.

### Step 2 — Mode and Path Selection
Default mode: All three discovery paths run in parallel.
- **PATH A** — Current Winners: search for content with live momentum in the last 7 days
- **PATH B** — Old Proven Winners: search for historically viral mechanisms not yet executed in modern short-form video
- **PATH C** — Original Curiosity Derivatives: construct original curiosity-gap concepts from known mass-audience subject areas

Default search window: Last 7 days for PATH A. No date restriction for PATH B and PATH C.
Default market: English-speaking adults, primarily US and Canada.
Default candidate count: Top 20.

### Step 3 — Source Search
Search across all available sources. For PATH A: live platforms (Instagram, Reddit, YouTube Shorts, TikTok). For PATH B: date-filtered Google, Reddit history, Quora, archived infographics, old blogs. For PATH C: authoritative sources for factual foundation.

Sources from EVERGREEN_CURIOSITY_GAP.md Section 9 must be included for PATH B and C research:
- Old blogs (2008–2018)
- Old infographics (Pinterest, Google Images with date filters)
- Quora
- Science explainers and research summaries
- Travel communities and forums (FlyerTalk, TripAdvisor forums)
- Interest and professional forums

### Step 4 — Candidate Pool Assembly
Build a pool of at least 30 candidates before filtering to the final 20. Candidates must span at least two of the three discovery paths. Do not fill the top 20 with all PATH A candidates — represent the full discovery surface.

### Step 5 — Verification
For every candidate:
- Label all material claims: VERIFIED / CREDIBLE / UNVERIFIED / REJECTED
- Verify or discard engagement metrics (never invent numbers)
- Distinguish published date from event date
- Flag any safety, copyright, or factual integrity concerns

### Step 6 — Mechanism Extraction
For every candidate:
- Identify the topic donor, format donor, hook mechanism, retention mechanism, and reusable mechanism
- Confirm the reusable mechanism can be executed originally (not by copying the source)
- Assess AI Remake Opportunity (YES / NO)

### Step 7 — Scoring and Ranking
Score every candidate on all ten dimensions (0–10 each; curiosity gap 1–10):
1. Scroll stop
2. Curiosity gap
3. Mass appeal
4. Visual clarity
5. Rewatch potential
6. Comment potential
7. Share potential
8. Kira reaction fit
9. AI recreation potential
10. Fact verifiability

Apply ranking methodology from EVERGREEN_CURIOSITY_GAP.md Section 17:
- Dinner Table Test result is the primary filter
- Mass appeal is the second criterion
- Curiosity gap score is the most important scoring dimension
- Visual execution feasibility gates final ranking

### Step 8 — Full Output Production
Produce the Top 20 candidates using the full output format from EVERGREEN_CURIOSITY_GAP.md Section 16. Every candidate must include:
- PATH (A / B / C)
- AI Remake Opportunity flag
- Dinner Table Test result
- Screenshot Test result
- All ten score dimensions
- PRODUCT_PROXIMITY classification
- Performance mechanics activated (STOP / STAY / REWATCH / OPEN CAPTION / SAVE / SEND / COMMENT / FOLLOW)
- Recommended action

### Step 9 — Top Three Winners
After the ranked list, identify the three best immediate tests with 2–4 sentence explanations covering: Why now? Why mass audience? Why Kira? What is the core viral mechanism?

### Step 10 — Save Research Record
Save the completed run to `kira_pack/05_RESEARCH/viral_candidates/` using the non-overwriting filename convention:
- First run that day: `YYYY-MM-DD_viral_candidates.md`
- Second run: `YYYY-MM-DD_viral_candidates_02.md`
- Continue with zero-padded sequential suffixes

### Step 11 — Stop
Do not produce final captions, production hooks, Kira generation prompts, or any downstream content. Research is complete. Hand off to the appropriate production agent.

---

## How to Invoke

Type any of the following:

```
FIND VIRAL IDEAS
```

```
Find viral ideas
```

```
Find 20 viral candidates using all three discovery paths.
```

The agent will default to: 7-day window for PATH A, no date restriction for PATH B/C, English-speaking adults, US/Canada primary market, Top 20 output.

### Optional Modifiers

You may append modifiers to adjust the default run:

- `FIND VIRAL IDEAS — last 30 days` — expands PATH A window to 30 days
- `FIND VIRAL IDEAS — evergreen only` — PATH B and C only; no current viral search
- `FIND VIRAL IDEAS — current only` — PATH A only
- `FIND VIRAL IDEAS — relationships focus` — bias the candidate pool toward relationship and betrayal territory
- `FIND VIRAL IDEAS — travel focus` — bias the candidate pool toward airports, hotels, and travel insider knowledge
- `FIND VIRAL IDEAS — AI remake focus` — prioritize candidates with AI Remake Opportunity: YES

---

## What This Command Does NOT Do

- Does not write final Reels captions
- Does not produce Kira generation prompts
- Does not produce final hooks
- Does not publish to Instagram
- Does not generate content automatically — it researches and recommends

Downstream production is handled by separate agents after research is complete.

---

*Reference: KIRA CLOUD AGENT PACK 2026-08-09*
*Primary agent: VIRAL_RESEARCH_AGENT.md*
*Framework: EVERGREEN_CURIOSITY_GAP.md*
