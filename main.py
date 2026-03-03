import os

from agents.strategy import StrategyAgent
from agents.narrative import NarrativeAgent
from agents.visual import VisualAgent
from agents.image import ImageAgent
from design.typography import TypographyEngine

# =====================================================
# SELECT NICHE HERE
# Options: "ai_tools" | "couples_motivation" | "mens_motivation"
# =====================================================

NICHE = "mens_motivation"

# ---------------------------
# Load niche module
# ---------------------------

if NICHE == "ai_tools":
    from config.niches import ai_tools as niche_module
elif NICHE == "couples_motivation":
    from config.niches import couples_motivation as niche_module
else:
    from config.niches import mens_motivation as niche_module


if __name__ == "__main__":

    # ---------------------------
    # Initialize agents
    # ---------------------------

    strategy = StrategyAgent(niche_module)
    narrative = NarrativeAgent()
    visual = VisualAgent()
    image_agent = ImageAgent()

    # ---------------------------
    # Build blueprint
    # ---------------------------

    blueprint = strategy.build_blueprint()
    niche_type = blueprint["niche_type"]

    typography = TypographyEngine(niche_type=niche_type)

    # ---------------------------
    # Generate narrative text
    # ---------------------------

    enhanced_slides = narrative.enhance_blueprint(blueprint)

    print("\nGenerated Slides:\n")
    for slide in enhanced_slides:
        print(slide)

    # ---------------------------
    # Build image prompts
    # ---------------------------

    # For mens niches, pass blueprint slides (dicts with type info) so the
    # visual agent can route each slide to the correct visual pool.
    # enhanced_slides are plain strings after the narrative pass.
    visual_slides = (
        blueprint.get("slides", enhanced_slides)
        if niche_type == "mens"
        else enhanced_slides
    )

    prompts = visual.build_image_prompts(
        visual_slides,
        blueprint.get("visual_profile", {}),
        blueprint.get("visual_archetypes", {}),
        niche_type=niche_type
    )

    # ---------------------------
    # Prepare output directory
    # ---------------------------

    output_dir = f"output/{NICHE}"
    os.makedirs(output_dir, exist_ok=True)

    # =====================================================
    # AI TOOLS — FULL CAROUSEL
    # =====================================================

    if niche_type == "ai_tools":

        # 1️⃣ Hook slide — unique background
        hook_image_paths = image_agent.generate_images([prompts[0]])
        hook_background_path = hook_image_paths[0]
        hook_output_path = f"{output_dir}/slide_1.png"

        typography.add_text_overlay(
            hook_background_path,
            enhanced_slides[0],
            hook_output_path,
            is_hook=True
        )

        # 2️⃣ One shared rating background for all rating slides
        rating_image_paths = image_agent.generate_images([prompts[1]])
        rating_background_path = rating_image_paths[0]

        # 3️⃣ Rating slides — reuse same background
        for i, slide_text in enumerate(enhanced_slides[1:], start=2):
            output_path = f"{output_dir}/slide_{i}.png"
            typography.add_text_overlay(
                rating_background_path,
                slide_text,
                output_path
            )

        total = len(enhanced_slides)
        print(f"\nAI Tools Carousel — {total} slides:\n")
        for i in range(1, total + 1):
            print(f"{output_dir}/slide_{i}.png")

    # =====================================================
    # COUPLES / MENS — FULL CAROUSEL
    # =====================================================

    else:

        image_paths = image_agent.generate_images(prompts)
        final_paths = []

        for i, path in enumerate(image_paths):
            output_path = f"{output_dir}/slide_{i + 1}.png"
            typography.add_text_overlay(path, enhanced_slides[i], output_path)
            final_paths.append(output_path)

        print(f"\n{niche_type.capitalize()} Carousel — {len(final_paths)} slides:\n")
        for path in final_paths:
            print(path)
