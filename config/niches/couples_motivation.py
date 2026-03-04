# config/niches/couples_motivation.py

import random

NICHE_NAME = "Couples Motivation"
NICHE_TYPE = "list"

# ----------------------------
# STRUCTURE RULES
# ----------------------------

STRUCTURE_RULES = {
    "min_items": 5,
    "max_items": 8,
    "hook_word_limit": 12,
    "tip_min_words": 8,
    "tip_max_words": 16,
    "anchor_max_words": 8
}

# ----------------------------
# HOOK LIBRARY
# ----------------------------

HOOK_TEMPLATES = [
    "{X} things a man should always do in a relationship",
    "{X} things a woman should always do in a relationship",
    "{X} habits strong couples follow",
    "{X} rules for a healthy relationship",
    "{X} signs you found the right person"
]

# ----------------------------
# ANCHOR QUOTES
# ----------------------------

ANCHOR_QUOTES = [
    "Love is built daily.",
    "Choose each other.",
    "Loyalty is attractive.",
    "Protect what you prayed for.",
    "Healthy love feels safe.",
    "Grow together.",
    "Real love is intentional."
]
# ----------------------------
# VISUAL SYSTEM
# ----------------------------

VISUAL_PROFILE = {
    "aesthetic_keywords": [
        "warm golden hour lighting",
        "soft cinematic shadows",
        "intimate emotional atmosphere",
        "natural skin tones",
        "romantic color palette",
        "subtle depth of field"
    ]
}

VISUAL_ARCHETYPES = {
    "wide_silhouette": [
        "very wide cinematic shot of tiny couple silhouette walking into sunset",
        "small couple figures walking along beach at golden hour, horizon dominant",
        "tiny couple walking through open field at dusk, landscape dominant"
    ],

    "hand_detail": [
        "close shot of two hands interlocked while walking, shallow depth of field",
        "holding hands while running, only hands visible in frame",
        "fingers intertwined in warm sunset lighting"
    ],

    "environment_memory": [
        "city skyline at dusk with two small figures sitting together",
        "empty rooftop at golden hour with two tiny silhouettes at edge",
        "wide cityscape at night with couple as small silhouettes"
    ],

    "cozy_detail": [
        "legs intertwined on couch, soft warm indoor lighting",
        "woman’s head resting on shoulder, cropped frame no faces visible",
        "back view of couple sitting close together on balcony at sunset"
    ]
}