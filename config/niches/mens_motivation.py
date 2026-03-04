# config/niches/mens_motivation.py

import random

NICHE_NAME = "Mens Motivation"
NICHE_TYPE = "mens"

VIRAL_MECHANICS = {
    "optimal_slide_count": 6,  # 1 hook + 5 goals
    "max_words_per_slide": 8,
    "final_slide_max_words": 4,
    "requires_save_trigger": True,
}

# =========================================================
# STRICT FITNESS STRUCTURE
# Every post includes:
# - 1 deadlift goal
# - 1 squat goal
# - 1 running goal
# - 1 cycling goal
# - 1 bodyweight goal
# =========================================================

ARCHETYPES = {

    # -------------------------------------------------
    # HOOKS
    # -------------------------------------------------

    "hook_templates": [
        "A strong man can do all of this.",
        "Physical standards worth training for.",
        "These numbers separate average from capable.",
        "What a fit man looks like in 2025.",
        "Train until these feel normal.",
        "The baseline every man should build toward.",
    ],

    # -------------------------------------------------
    # GOAL POOLS (STRICTLY SEPARATED)
    # -------------------------------------------------

    "deadlift_goals": [
        "Deadlift 1.8x your bodyweight.",
        "Trap bar deadlift 2x your bodyweight.",
        "Romanian deadlift 1.2x your bodyweight for 5 reps.",
        "Deadlift 180kg with clean form.",
    ],

    "squat_goals": [
        "Back squat 1.5x your bodyweight.",
        "Front squat your bodyweight for 5 reps.",
        "Pause squat 1.2x your bodyweight.",
        "Squat 140kg below parallel.",
    ],

    "running_goals": [
        "Run 5km under 25 minutes.",
        "Run 10km under 55 minutes.",
        "Sprint 100m under 13 seconds.",
        "Complete 5km without stopping.",
    ],

    "cycling_goals": [
        "Cycle 30km without stopping.",
        "Cycle 50km under 2 hours.",
        "Climb 500m elevation in one ride.",
        "Average 30km/h over 20km.",
    ],

    "bodyweight_goals": [
        "15 strict pull-ups in one set.",
        "5 controlled muscle-ups.",
        "30 push-ups with perfect form.",
        "Hold a plank for 2 minutes.",
        "10 pistol squats per leg.",
    ],

    # -------------------------------------------------
    # VISUAL ARCHETYPES (HIGHLY SPECIFIC)
    # -------------------------------------------------

    "visual_archetypes": {

        # HOOK VISUALS — physique display, not exercise execution
        "hook": [
            "well-built man in a cut-off sleeveless vest doing front double bicep flex in industrial gym, visible muscle definition, gym equipment blurred in background, direct overhead lighting",
            "muscular man in sleeveless gym vest standing facing locker room mirror in side chest pose, gym bag on bench, cool fluorescent lighting",
            "athletic man in cut-off tank top flexing lat spread on outdoor rooftop training area, overcast natural light, open sky above with strong headroom",
            "well-built man in sleeveless vest posing in gym doorway backlit by natural light, arms raised in relaxed flex, candid documentary feel",
        ],

        # DEADLIFT VISUALS
        "deadlift": [
            "man mid-pull on heavy barbell deadlift, bar just below knees, chalk dust in air, industrial gym",
            "low angle shot of man locking out deadlift, loaded barbell, focused expression, gym background visible",
            "man gripping barbell with chalked hands before heavy deadlift attempt, gritty gym floor",
            "trap bar deadlift at lockout, wide stance, raw effort visible, functional training space",
        ],

        # SQUAT VISUALS
        "squat": [
            "man in the bottom of a heavy back squat, barbell across shoulders, gym rack visible",
            "front squat with upright torso, elbows high, loaded barbell, clean gym background",
            "side view of deep squat below parallel, knees bent, controlled movement",
            "man re-racking heavy squat barbell after final rep, breathing hard",
        ],

        # RUNNING VISUALS
        "running": [
            "man running on open road at dawn, long empty street, cool overcast lighting",
            "man sprinting on track, motion blur in legs, empty stadium background",
            "side profile of man mid-stride during outdoor run, urban skyline distant",
            "man finishing hard run, hands on knees, breathing heavy, city park path",
        ],

        # CYCLING VISUALS
        "cycling": [
            "man cycling on open countryside road, low aerodynamic position, cool toned sky",
            "man riding road bike uphill, visible strain, wide landscape background",
            "side profile of cyclist pedaling hard on empty road, motion blur on wheels",
            "man standing on pedals climbing incline, dramatic open road environment",
        ],

        # BODYWEIGHT VISUALS
        "bodyweight": [
            "man performing strict pull-ups on outdoor bar, full extension, clear sky",
            "man mid-muscle-up transition above bar, outdoor calisthenics park",
            "man in perfect push-up position, straight body alignment, concrete ground",
            "man holding plank position on rooftop, city skyline background",
            "man performing pistol squat on outdoor platform, strong balance control",
        ],
    }
}