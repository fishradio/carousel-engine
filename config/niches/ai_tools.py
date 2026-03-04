# config/niches/ai_tools.py

import random

NICHE_NAME = "AI Tools Ranking"
NICHE_TYPE = "ai_tools"

# ---------------------------
# STRUCTURE RULES
# ---------------------------

STRUCTURE_RULES = {
    "min_items": 4,
    "max_items": 6,
    "include_anchor": False
}

# ---------------------------
# PERSONA LOCK (CRITICAL)
# ---------------------------

IDENTITIES = [
    "CS major",
    "comp sci major",
    "CS undergrad",
    "computer science student",
    "engineering student"
]

INSTITUTIONS = [
    "Harvard",
    "Stanford",
    "Princeton",
    "Yale",
    "Columbia",
    "MIT",
    "UPenn",
    "Cornell"
]

# ---------------------------
# HOOK TEMPLATE (BOTH REQUIRED)
# ---------------------------

HOOK_TEMPLATES = [
    "ranking AI tools that carried me as a {identity} @ {institution}",
    "AI tools I actually used as a {identity} @ {institution}",
    "ranking AI tools that got me through CS @ {institution}",
]

# ---------------------------
# CLOSED TOOL UNIVERSE
# ---------------------------

TIP_LIBRARY = [
    "ChatGPT",
    "Claude",
    "Cursor",
    "Replit",
    "Deepseek",
    "Lovable.dev",
    "Perplexity",
    "Phind",
    "Github Copilot"
]

# ---------------------------
# TOOL PERSONAS (CONTROLLED OUTPUT)
# ---------------------------

TOOL_PERSONAS = {

    "ChatGPT": {
        "rating_range": (2, 7),
        "strengths": [
            "good for understanding concepts and high level research",
            "solid for quick explanations, clean UI",
            "long context window helps in brainstorming for big projects",
            "great for writing clean summaries"
        ],
        "weaknesses": [
            "gets lost in complex builds",
            "hallucinates under pressure",
            "not reliable for projects with multiple integrations",
            "mid at actual implementation"
        ]
    },

    "Claude": {
        "rating_range": (6, 9),
        "strengths": [
            "handles long prompts way better than GPT",
            "thinks more clearly through edge cases",
            "more structured outputs",
            "better reasoning overall"
        ],
        "weaknesses": [
            "can be slower sometimes",
            "not as mainstream or creative as GPT",
            "UI could be better"
        ]
    },

    "Cursor": {
        "rating_range": (5, 9),
        "strengths": [
            "intuitive UI if you're into coding already",
            "great inline suggestions make things faster",
            "fast for quick edits",
            "feels tailor built for devs"
        ],
        "weaknesses": [
            "can crash during full builds",
            "breaks too often if handling long contexts",
            "little unstable on big projects"
        ]
    },

    "Replit": {
        "rating_range": (6, 8),
        "strengths": [
            "easy to spin up small and medium scale projects",
            "good for building quick prototypes",
            "saves a lot of setup time"
        ],
        "weaknesses": [
            "not ideal for large scale work",
            "limited compared to local dev",
            "performance can dip while handling larger contexts"
        ]
    },

    "Deepseek": {
        "rating_range": (5, 8),
        "strengths": [
            "handles long prompts well",
            "surprisingly solid for reasoning",
            "underrated tool (because it's chinese)"
        ],
        "weaknesses": [
            "not mainstream yet",
            "trust factor is lower than GPT and Claude",
            "less community support"
        ]
    },

    "Lovable.dev": {
        "rating_range": (8, 11),  # allow exaggerated viral rating
        "strengths": [
            "actually saved me in lot of projects",
            "builds the site from what i describe",
            "builds an app from what i describe",
            "carried most of my workload"
        ],
        "weaknesses": [
            "not perfect yet",
            "still needs manual cleanup",
            "breaks on edge cases"
        ]
    },

    "Perplexity": {
        "rating_range": (5, 8),
        "strengths": [
            "great for focused research, reliable citations",
            "fast answers with reliable sources",
            "good for structured outputs"
        ],
        "weaknesses": [
            "not built for heavy coding",
            "limited technical depth",
            "better for gathering info than full builds"
        ]
    },

    "Phind": {
        "rating_range": (6, 9),
        "strengths": [
            "solid dev focused answers",
            "good debugging help",
            "better than GPT for code sometimes"
        ],
        "weaknesses": [
            "not always consistent",
            "smaller ecosystem"
        ]
    },

    "Github Copilot": {
        "rating_range": (6, 9),
        "strengths": [
            "good autocomplete can speed up work",
            "fast inline suggestions that actually help",
            "saves a lot of typing time"
        ],
        "weaknesses": [
            "not smart for architecture",
            "just predicts next line without taking full context",
            "doesn't think as deeply"
        ]
    }
}

# ---------------------------
# CONTROVERSY LINES (LOW PROBABILITY)
# ---------------------------

CONTROVERSY_LINES = [
    "people hype this too much.",
    "lowkey overrated on tech twitter.",
    "only reason it’s not viral is cause mainstream people don’t know about it.",
    "everyone pretends they use this more than they do."
]

# ---------------------------
# RATING SLIDE BUILDER
# ---------------------------

def build_rating_slide(tool, rank):

    persona = TOOL_PERSONAS[tool]

    rating = random.randint(*persona["rating_range"])
    strength = random.choice(persona["strengths"])
    weakness = random.choice(persona["weaknesses"])

    text_blocks = [
        f"{rank}. {tool} ({rating}/10)",
        strength + ".",
        weakness + "."
    ]

    # 20% chance of controversy line
    if random.random() < 0.2:
        text_blocks.append(random.choice(CONTROVERSY_LINES))

    final_text = "\n\n".join(text_blocks)

    # enforce viral lowercase tone
    return final_text.lower()


# ---------------------------
# VISUAL PROFILE
# ---------------------------

VISUAL_PROFILE = {
    "mode": "ai_tools_real"
}

# ---------------------------
# TYPOGRAPHY PROFILE
# ---------------------------

TYPOGRAPHY_PROFILE = {
    "style": "boxed"
}