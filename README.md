AI Viral Carousel Content Engine

A modular, AI-powered Python system for generating high-quality, niche-optimized Instagram carousel posts with consistent branding, structured virality mechanics, and scalable multi-niche architecture.

🚀 Project Vision

This project is a multi-agent content generation engine designed to:

Generate viral-style Instagram carousel posts

Support multiple niches (e.g., Men’s Motivation, Couples Motivation)

Separate structure, narrative, visuals, and typography into modular layers

Encode psychological archetypes into both text and imagery

Scale into a content factory

This is not just an image generator — it is a structured aesthetic system.

🧠 Core Objectives

Build a modular multi-niche architecture

Separate narrative psychology from visual psychology

Generate image prompts aligned with layout constraints

Apply niche-aware typography styling

Ensure deterministic visual sequencing

Maintain scalability for future niches

Demonstrate strong AI + systems design capability

🏗 High-Level Architecture
project_root/
│
├── main.py
│
├── agents/
│   ├── strategy.py
│   ├── narrative.py
│   ├── visual.py
│   └── image.py
│
├── design/
│   └── typography.py
│
├── config/
│   └── niches/
│       ├── mens_motivation.py
│       └── couples_motivation.py
│
├── fonts/
│   ├── BebasNeue-Regular.ttf
│   └── Montserrat-VariableFont_wght.ttf
│
└── output/
🔄 Execution Flow

main.py orchestrates the full pipeline:

StrategyAgent 
    → NarrativeAgent 
        → VisualAgent 
            → ImageAgent 
                → TypographyEngine
Step-by-step:

Load niche configuration

Build structural blueprint

Enhance narrative via AI

Generate image prompts

Generate images via OpenAI

Apply typography styling

Save final carousel slides

📁 Folder & File Responsibilities
agents/strategy.py

Role: Structural blueprint generator

Defines slide structure

Handles niche branching

Controls rule count for list-based niches

Returns structured blueprint dictionary

Couples (List-Based)

Dynamic rule count

Hook + numbered tips + anchor

Men’s (Escalation-Based)

Predefined narrative arc

Identity → pain → power → closure

agents/narrative.py

Role: AI text enhancement layer

Couples Mode

Generates dynamic rule count

Ensures headline matches rule count

Produces numbered relationship principles

Adds short emotional closing line

Enforces word limits

Men’s Mode

Rewrites escalation narrative

Intensifies emotional tension

Maintains slide order

Applies word constraints

This layer encodes psychological persuasion logic.

agents/visual.py

Role: Converts slides into image prompts

Couples Mode

Deterministic visual rhythm

Environment-dominant composition

Tiny silhouettes

Memory-style framing

Strong negative space

Avoids face-centric imagery

Men’s Mode

Dark cinematic aesthetic

Single dominant subject

Low-angle framing

High contrast, moody tone

This layer encodes visual psychology.

agents/image.py

Role: Image generation layer

Sends prompts to OpenAI image API

Receives generated images

Saves images in output directory

Maintains naming consistency

This layer handles AI image generation.

design/typography.py

Role: Niche-aware typography styling engine

Men’s Style

Font: Bebas Neue

All caps

Strong outline stroke

High contrast

Aggressive composition

Couples Style

Font: Montserrat

Sentence case

Soft vignette

Subtle shadow

Editorial warmth

Center alignment

Handles:

Word wrapping

Font scaling

Alignment

Styling

Export

This layer defines brand identity.

config/niches/

Each niche module defines:

NICHE_TYPE

STRUCTURE_RULES

HOOK_TEMPLATES

TIP_LIBRARY

ANCHOR_QUOTES

VISUAL_PROFILE

VISUAL_ARCHETYPES

This isolates:

Tone

Emotional direction

Structural constraints

Image mood

Adding a new niche requires only creating a new config file.

🔥 Implemented Niches
1. Men’s Motivation

Escalation narrative structure

Psychological dominance themes

Dark cinematic aesthetic

Identity-driven tension build

Philosophy:

The subject is the hero.

2. Couples Motivation

Structured list format

Dynamic rule counts

Aspirational intimacy

Landscape-dominant imagery

Memory-based framing

Philosophy:

The environment is the hero.

🎯 System Innovations

Niche-aware branching architecture

Deterministic visual sequencing

Psychological archetype encoding

Typography profiles per niche

Blueprint abstraction layer

Visual logic separated from narrative logic

Modular design for infinite expansion

📈 Scalability Design

To add a new niche:

Create new file in config/niches/

Define structure rules

Define visual archetypes

Define visual profile

Return correct niche_type in strategy

Add typography style if required

No core engine rewrite required.

⚙️ Current Engineering Challenges

Avoiding AI-generated stock faces

Maintaining aspirational projection

Matching rule count to headline

Preventing visual repetition

Ensuring typography readability on warm tones

Enforcing environment-dominant framing

🔮 Future Enhancements

Face detection to prevent text overlap

Contrast-aware typography adjustment

Carousel-to-video animation engine

A/B aesthetic testing

Scene entropy tracking

Multi-language support

Web UI wrapper

Cloud deployment

🧠 System Philosophy

This engine is not just generating content.

It is encoding:

Psychological triggers

Visual persuasion

Structured narrative escalation

Brand-consistent aesthetic identity

Each niche behaves differently because each niche sells a different emotional fantasy.

🏁 How to Run

Set your OpenAI API key in .env

Choose niche in main.py

Run:

python main.py

Generated slides will appear in:

/output
