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
            "good for concepts",
            "solid for quick explanations",
            "helps when i'm stuck",
            "great for summaries"
        ],
        "weaknesses": [
            "gets lost in real builds",
            "hallucinates under pressure",
            "not reliable for full projects",
            "mid at actual implementation"
        ]
    },

    "Claude": {
        "rating_range": (6, 9),
        "strengths": [
            "handles long prompts better than GPT",
            "thinks more clearly through edge cases",
            "more structured outputs",
            "better reasoning overall"
        ],
        "weaknesses": [
            "slower sometimes",
            "not as mainstream",
            "UI could be better"
        ]
    },

    "Cursor": {
        "rating_range": (5, 9),
        "strengths": [
            "clean UI",
            "great inline suggestions",
            "fast for quick edits",
            "feels built for devs"
        ],
        "weaknesses": [
            "crashes on full builds",
            "breaks too often",
            "unstable on big projects"
        ]
    },

    "Replit": {
        "rating_range": (6, 8),
        "strengths": [
            "easy to spin up projects",
            "good for quick prototypes",
            "saves setup time"
        ],
        "weaknesses": [
            "not ideal for large scale work",
            "limited compared to local dev",
            "performance dips sometimes"
        ]
    },

    "Deepseek": {
        "rating_range": (5, 8),
        "strengths": [
            "handles long prompts well",
            "surprisingly solid for reasoning",
            "underrated tool"
        ],
        "weaknesses": [
            "not mainstream yet",
            "trust factor is lower",
            "less community support"
        ]
    },

    "Lovable.dev": {
        "rating_range": (8, 11),  # allow exaggerated viral rating
        "strengths": [
            "actually saved me",
            "builds the site from what i describe",
            "carried most of my workload"
        ],
        "weaknesses": [
            "not perfect",
            "still needs manual cleanup",
            "breaks on edge cases"
        ]
    },

    "Perplexity": {
        "rating_range": (5, 8),
        "strengths": [
            "great for research",
            "fast answers with sources",
            "good for quick context"
        ],
        "weaknesses": [
            "not for heavy coding",
            "limited depth",
            "better for info than builds"
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
            "good autocomplete",
            "fast inline suggestions",
            "saves typing time"
        ],
        "weaknesses": [
            "not smart for architecture",
            "just predicts next line",
            "doesn't think deeply"
        ]
    }
}

# ---------------------------
# CONTROVERSY LINES (LOW PROBABILITY)
# ---------------------------

CONTROVERSY_LINES = [
    "people hype this too much.",
    "lowkey overrated on twitter.",
    "only reason it’s not viral is cause people don’t know about it.",
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