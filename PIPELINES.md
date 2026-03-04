# Generation Pipelines

How each niche moves through Strategy → Narrative → Visual → Image.

---

## AI Tools Ranking

**Philosophy:** Persona-driven authority content. A fictional student identity rates AI tools in a weak-to-strong ranking curve. Fully deterministic — no GPT.

### Strategy
- Locks a random identity (e.g. "CS student") and institution (e.g. "MIT")
- Picks a random count X of tools within min/max bounds
- Samples X tools from `TIP_LIBRARY`
- Returns: `{ niche_type, slides, identity, institution }`

### Narrative
- Ignores blueprint slides entirely
- Rebuilds hook from template + identity + institution
- Sorts tools by average rating strength (weak → strong curve)
- Calls `build_rating_slide()` per tool — no GPT involved
- Returns: `[hook, tool_1, tool_2, ..., tool_X]`

### Visual
- Generates **2 images only**, regardless of slide count
  - Image 1 — Hook: elevator mirror selfie (student persona)
  - Image 2 — Rating background: campus workspace (shared across all tool slides)

### Output
- Hook → unique image + `is_hook=True` typography
- All tool slides → same shared background, different text overlays

---

## Mens Motivation

**Philosophy:** Fully deterministic, no GPT. Every slide maps to a specific fitness category with a tightly matched visual archetype.

### Strategy
- Picks a hook from `hook_templates`
- Picks one goal from each of 5 strictly separated pools: `deadlift_goals`, `squat_goals`, `running_goals`, `cycling_goals`, `bodyweight_goals`
- Returns: `{ niche_type, slides (dicts with type + category + base_text), viral_mechanics, visual_archetypes }`

### Narrative
- No GPT, no text transformation
- Reads `base_text` from each slide dict and returns it as-is
- Returns: `[hook, deadlift_goal, squat_goal, running_goal, cycling_goal, bodyweight_goal]`

### Visual
- Receives the original blueprint slides (dicts with category info), not the narrative strings
- Routes each slide's `category` directly to its matching archetype pool:
  - `deadlift` → deadlift gym scenes
  - `squat` → squat/pressing gym scenes
  - `running` → outdoor road/track scenes
  - `cycling` → outdoor road/hill scenes
  - `bodyweight` → calisthenics/bar scenes
  - hook (no category) → falls back to `deadlift` pool
- Generates one unique image per slide (6 total)

### Output
- All 6 slides get unique images matched to their fitness category

---

## Couples Motivation

**Philosophy:** Hybrid. Hook is deterministic from a curated library. Tips and closing line are GPT-generated. Background aesthetic is fully pre-designed and independent of text content.

### Strategy
- Picks a random count X of tips within min/max bounds
- Picks a hook from `HOOK_TEMPLATES`, fills in X
- Returns: `{ niche_type, hook (string), num_tips (int) }`
- Does not generate any tip content — that is entirely GPT's job

### Narrative
- Pulls hook directly from blueprint — no GPT for the hook
- Sends GPT a prompt asking for exactly `num_tips` numbered relationship principles + one short closing line
- Prepends hook to GPT output in code (GPT cannot drop or alter it)
- Returns: `[hook] + gpt_lines`

### Visual
- Completely independent of text — background/text coupling is intentionally loose
- Uses a fixed `scene_sequence` cycling through 7 cinematic types:
  `cityscape_only → hands_detail → wide_silhouette → interior_detail → full_couple_once → environment_memory → cityscape_closure`
- Generates one unique image per slide

### Output
- All slides get unique images on a fixed cinematic sequence

---

## Summary

|  | AI Tools | Mens Motivation | Couples Motivation |
|--|--|--|--|
| **Hook source** | Deterministic (template + identity) | Deterministic (hook_templates pool) | Deterministic (HOOK_TEMPLATES pool) |
| **Tip/goal source** | Deterministic (build_rating_slide) | Deterministic (5 goal pools) | GPT-generated |
| **GPT used** | No | No | Yes — tips + closing line only |
| **Images per carousel** | 2 (hook + 1 shared background) | 6 (one per slide) | Variable (one per slide) |
| **Visual routing** | Fixed scenes per image type | Category-matched per slide | Fixed sequence, text-independent |
| **Slide count** | Variable (X tools + hook) | Fixed (6) | Variable (X tips + hook + closing) |
