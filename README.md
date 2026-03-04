# AI Viral Carousel Content Engine

A modular, AI-powered Python system for generating niche-optimized TikTok carousel posts — with structured virality mechanics, psychological visual archetypes, and a scalable multi-niche architecture.

---

## Project Overview

This engine is not an image generator. It is a **structured content system** that encodes psychological triggers, visual persuasion logic, and narrative escalation into every slide — separately per niche.

Each niche has its own:
- Content structure and hook strategy
- Visual archetype pool
- Typography style
- Image composition doctrine

---

## Architecture

```
project_root/
│
├── main.py                        # Pipeline orchestrator
│
├── agents/
│   ├── strategy.py                # Blueprint builder — structure, hooks, goal pools
│   ├── narrative.py               # Text layer — deterministic or GPT depending on niche
│   ├── visual.py                  # Image prompt builder — routes by slide category
│   └── image.py                   # OpenAI image generation
│
├── design/
│   ├── layout.py                  # Shared visual constants (composition, lighting, color)
│   └── typography.py              # Niche-aware text overlay engine
│
├── config/
│   └── niches/
│       ├── mens_motivation.py
│       ├── couples_motivation.py
│       └── ai_tools.py
│
├── fonts/
│   ├── InterVariable.ttf
│   ├── Arial Bold.ttf
│   └── Arial.ttf
│
└── output/
    ├── mens_motivation/
    ├── couples_motivation/
    └── ai_tools/
```

---

## Execution Flow

```
StrategyAgent → NarrativeAgent → VisualAgent → ImageAgent → TypographyEngine
```

1. Load niche config
2. `StrategyAgent` builds a structured blueprint (slide types, hook, goal pools)
3. `NarrativeAgent` produces final slide text (deterministic or GPT)
4. `VisualAgent` converts slide metadata into image prompts, routed by category
5. `ImageAgent` generates images via OpenAI
6. `TypographyEngine` applies niche-specific text overlay and exports slides

---

## Niches

### Men's Motivation — Fully Deterministic

**Philosophy:** Every slide maps to a specific fitness category. No GPT involved.

- Hook picked from `hook_templates` pool
- 5 goals selected one-per-category: deadlift, squat, running, cycling, bodyweight
- Each slide gets a unique image matched to its category's visual archetype pool
- Hook slide uses a dedicated physique/flex visual pool (distinct from all exercise slides)
- **6 slides total, 6 unique images**

### Couples Motivation — Hybrid (GPT for tips only)

**Philosophy:** Hook is deterministic. Relationship principles and closing line are GPT-generated.

- Hook locked from curated `HOOK_TEMPLATES`, count X drawn randomly within bounds
- GPT generates exactly X numbered relationship principles + one short closing line
- Images follow a fixed cinematic scene sequence, independent of text content
- **Variable slide count, one unique image per slide**

### AI Tools Ranking — Fully Deterministic

**Philosophy:** Persona-driven authority content. A fictional student identity rates AI tools weak-to-strong.

- Identity (e.g. "CS student") and institution (e.g. "MIT") locked at blueprint stage
- Tools sampled from `TIP_LIBRARY`, sorted by average rating strength (weak → strong curve)
- **2 images only**: hook (elevator mirror selfie) + one shared campus workspace background
- All rating slides reuse the same background with different text overlays

---

## Agent Responsibilities

### `agents/strategy.py`
Builds the structural blueprint per niche. Defines slide types, picks hooks, samples from goal/tool pools, and returns a typed dict consumed by downstream agents.

### `agents/narrative.py`
- **Mens:** passthrough — reads `base_text` from blueprint slides as-is, no transformation
- **Couples:** calls GPT-4o-mini to generate tips and closing line; prepends hook in code
- **AI Tools:** calls `build_rating_slide()` per tool deterministically; no GPT

### `agents/visual.py`
Routes each slide's `category` field to the matching archetype pool in the niche config. For mens slides, each category (deadlift, squat, running, cycling, bodyweight, hook) maps to its own distinct scene list. Wraps scenes in shared layout/lighting/color/style constants from `design/layout.py`.

### `agents/image.py`
Sends prompts to the OpenAI image API and saves results to the output directory.

### `design/layout.py`
Defines shared visual doctrine applied to all mens slides:
- `MENS_FITNESS_LAYOUT` — composition, framing, headroom rules
- `MENS_FITNESS_COLOR` — cool-toned grading
- `MENS_FITNESS_LIGHTING` — moody, underexposed atmosphere
- `MENS_FITNESS_STYLE` — candid documentary feel, not influencer aesthetic

### `design/typography.py`
Niche-aware text overlay engine. Handles word wrapping, font scaling, vertical positioning, and stroke styling. Each niche has its own font, size, position, and rendering style.

| Niche | Font | Style |
|---|---|---|
| Men's Motivation | Inter Variable | White fill, black stroke, lower-center anchor |
| Couples Motivation | Inter Variable | White fill, soft drop shadow, mid-frame anchor |
| AI Tools | Arial Bold / Arial | White rounded boxes, top-anchored hook |

---

## Adding a New Niche

1. Create `config/niches/your_niche.py` — define hooks, content pools, visual archetypes
2. Add a branch in `agents/strategy.py` returning `niche_type` and blueprint structure
3. Add a branch in `agents/narrative.py` for text generation logic
4. Add a branch in `agents/visual.py` for image prompt construction
5. Add typography settings in `design/typography.py` if the style differs
6. Select the niche in `main.py`

No core engine rewrite required.

---

## Setup & Usage

**1. Install dependencies**
```bash
pip install -r requirements.txt
```

**2. Set environment variables**
```bash
# .env
OPENAI_API_KEY=your_key_here
```

**3. Select niche in `main.py`**
```python
NICHE = "mens_motivation"  # "couples_motivation" | "ai_tools"
```

**4. Run**
```bash
python main.py
```

Output slides are saved to `output/{niche}/slide_1.png`, `slide_2.png`, etc.

---

## Future Enhancements

- Face detection to prevent text overlap
- Contrast-aware typography adjustment
- A/B aesthetic testing across prompt variants
- Scene entropy tracking to avoid visual repetition
- Carousel-to-video animation export
- Web UI wrapper
- Cloud deployment
