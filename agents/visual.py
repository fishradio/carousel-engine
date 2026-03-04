# agents/visual.py

import random
from design.layout import (
    MENS_FITNESS_LAYOUT,
    MENS_FITNESS_COLOR,
    MENS_FITNESS_LIGHTING,
    MENS_FITNESS_STYLE,
)
class VisualAgent:

    def build_image_prompts(
        self,
        enhanced_slides,
        visual_profile,
        archetypes,
        niche_type="mens"
    ):

        prompts = []
        aesthetic = ", ".join(
            visual_profile.get("aesthetic_keywords", [])
        )

        # =====================================================
        # AI TOOLS NICHE — 2 IMAGE SYSTEM
        # =====================================================
        if niche_type == "ai_tools":

            # -------------------------------------------------
            # 1️⃣ HOOK IMAGE (Person / Authority Frame)
            # -------------------------------------------------

            hairstyle = random.choice(["buzzcut", "normal short hair", "wolf cut"])
            race = random.choice(["white caucasian", "african american"])

            hook_prompt = f"""
Ultra realistic iPhone mirror selfie.

Portrait orientation 4:5.
Wide vertical composition.
Zoomed-out perspective.

Modern metallic elevator interior.
Brushed steel walls.
Elevator seams and wall lines visible.
Environment must dominate the frame.

Vertical button panel fully visible on right side wall.
Brushed steel buttons with floor numbers engraved.
Some buttons slightly worn or yellowed from frequent use.
Door open and door close buttons clearly visible at the bottom of the panel.
One floor button faintly illuminated.

Small wall signage visible:
Maximum capacity label (e.g. "Max 1000 kg / 13 persons") affixed near the panel.
Annual inspection certificate sticker on the wall near the door.
Emergency phone cabinet or intercom panel mounted below the buttons.

Ceiling lights clearly visible at top.

Young {race} male computer science student with a confident expression on his face.
{hairstyle} hairstyle.
Casual oversized hoodie.
Backpack straps visible.
Holding iPhone naturally.

Camera positioned farther from mirror (1.5–2 meters away).
Full upper body visible including waist and both arms.
Loose framing, not a portrait crop.
Subject appears smaller within frame.

Camera slightly angled (not perfectly straight).
Very subtle tilt.
Not symmetrical.

Subject positioned slightly left of center.
Body shifted to one side.
Large empty elevator wall on opposite side.
Clear open upper wall space for text.

Subject occupies less than one third of total frame height.
At least half of the image must be visible elevator wall.
More environment than person.

Neutral expression.
Unposed.
Natural posture.

No cinematic lighting.
No dramatic shadows.
No shallow depth of field.
No professional photography feel.
Must look like casual elevator selfie.

Important:
Do NOT center subject.
Do NOT tightly crop.
Do NOT zoom in on face.
Do NOT let subject dominate frame.
Environment is primary visual element.

No text in image.
"""

            prompts.append(hook_prompt.strip())

            # -------------------------------------------------
            # 2️⃣ RATING BACKGROUND (Workspace)
            # -------------------------------------------------
            workspace_scene = random.choice([

    # CLASSROOM
    """
    University classroom during off-hours.
    Long shared desks.
    Plastic lecture chairs in rows.
    White painted brick walls.
    Cork board on wall.
    Fluorescent ceiling light panels visible.
    Empty academic atmosphere.
    """,

    # LIBRARY
    """
    Campus library study table.
    Tall bookshelves softly visible in background.
    Neutral overhead lighting.
    Other students faintly visible far away but not in focus.
    Quiet academic environment.
    """,

    # STUDY ROOM
    """
    Small campus study room.
    Whiteboard behind desk with faint marker residue.
    Group tables pushed together.
    Backpack resting on chair nearby.
    Slightly enclosed academic space.
    """,

    # DORM
    """
    Dorm study desk setup.
    Bed corner barely visible in background.
    Personal items around desk.
    Slight clutter.
    Indoor overhead lighting.
    Private student living space.
    """
])
         
            rating_prompt = f"""
Ultra realistic iPhone photo.

Portrait orientation 4:5.
Casual handheld shot.
Slightly imperfect framing.
Not symmetrical.
Not professionally composed.

{workspace_scene}

Fluorescent indoor lighting.
Slightly flat lighting.
No cinematic warmth.
No dramatic shadows.

Open laptop on desk with code editor visible.

Small student details present:
notebook with handwritten notes,
pen,
water bottle,
charger cable,
backpack partially visible,
earbuds case,
slightly messy desk,
sticky notes,
coffee cup or energy drink.

Laptop screen clearly visible but not staged.
Angle feels natural, like student quickly took photo while studying.

Environment feels lived-in.
Not aesthetic.
Not minimal.
Not luxury.
Not Pinterest style.

Slight grain allowed.
Slight motion softness allowed.

No shallow depth of field.
Everything realistically in focus.

No text in image.
"""

            # Only ONE rating image is generated
            prompts.append(rating_prompt.strip())

            return prompts

        # =====================================================
        # COUPLES NICHE — CINEMATIC DIRECTED SEQUENCING
        # =====================================================
        if niche_type == "couples":

            scene_sequence = [
                "cityscape_only",
                "hands_detail",
                "wide_silhouette",
                "interior_detail",
                "full_couple_once",
                "environment_memory",
                "cityscape_closure"
            ]

            for i, slide in enumerate(enhanced_slides):

                scene_type = scene_sequence[i % len(scene_sequence)]

                if scene_type == "cityscape_only":
                    scene = (
                        "Luxury high-rise window overlooking Manhattan skyline at night, "
                        "city lights glowing below, no people visible"
                    )

                elif scene_type == "hands_detail":
                    scene = (
                        "Close-up of couple holding hands while walking under streetlights at night, "
                        "only hands visible, urban background softly blurred"
                    )

                elif scene_type == "wide_silhouette":
                    scene = (
                        "Very wide cinematic shot of couple walking far away under city lights, "
                        "tiny silhouettes, strong negative space"
                    )

                elif scene_type == "interior_detail":
                    scene = (
                        "Cozy apartment balcony at night, wine glasses on table, "
                        "city skyline softly glowing in background"
                    )

                elif scene_type == "full_couple_once":
                    scene = (
                        "Soft side-profile of couple standing by large window at night, "
                        "subtle expressions, not centered"
                    )

                elif scene_type == "environment_memory":
                    scene = (
                        "Rain on window at night with blurred city lights beyond, "
                        "emotional memory aesthetic"
                    )

                elif scene_type == "cityscape_closure":
                    scene = (
                        "Massive panoramic night skyline, couple extremely small in lower frame"
                    )

                prompt = f"""
Ultra realistic cinematic photograph.
Portrait orientation 4:5.

Late night urban atmosphere.
Deep navy shadows with warm amber window lights.
Moody cinematic lighting.
Strong negative space.
Environment dominant composition.
Subjects placed in lower third when present.
No centered framing.
No stock-photo posing.
No bright smiling faces.
No direct eye contact with camera.
Only one slide shows both faces clearly.
Scene: {scene}.
No text in image.
"""

                prompts.append(prompt.strip())

            return prompts

        # =====================================================
        # MEN'S MOTIVATION — STRICT FITNESS
        # =====================================================
        if niche_type == "mens":

            # archetypes now equals visual_archetypes dict:
            # {
            #   "deadlift": [...],
            #   "squat": [...],
            #   "running": [...],
            #   "cycling": [...],
            #   "bodyweight": [...]
            # }

            for slide in enhanced_slides:

                category = slide.get("category")

                if category in archetypes:
                    scene = random.choice(archetypes[category])
                else:
                    # Hook slide → use dedicated physique/flex visuals
                    scene = random.choice(archetypes["hook"])

                prompt = f"""
Ultra realistic athletic photograph.

{MENS_FITNESS_LAYOUT}

{MENS_FITNESS_COLOR}

{MENS_FITNESS_LIGHTING}

{MENS_FITNESS_STYLE}

{scene}

No text in image.
"""

                prompts.append(prompt.strip())

            return prompts

        # =====================================================
        # FALLBACK (should not be reached for mens niches)
        # =====================================================
        for slide in enhanced_slides:

            archetype_category = random.choice(list(archetypes.keys()))
            environment = random.choice(archetypes[archetype_category])

            prompt = f"""
Cinematic ultra realistic photograph.
Portrait orientation 4:5.
Dark high-contrast aesthetic.
Single male subject.
{aesthetic}.
Scene: {environment}.
Low angle or strong depth perspective.
Negative space composition.
No text in image.
No clutter.
Moody atmosphere.
"""

            prompts.append(prompt.strip())

        return prompts
    