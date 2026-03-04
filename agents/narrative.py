from openai import OpenAI
from dotenv import load_dotenv
import os
import re
import random

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class NarrativeAgent:

    def enhance_blueprint(self, blueprint):

        niche_type = blueprint.get("niche_type", "mens")

        # ==================================================
        # COUPLES NICHE
        # ==================================================
        if niche_type == "couples":

            hook = blueprint["hook"]
            num_tips = blueprint["num_tips"]

            prompt = f"""
You are writing slides for a viral Instagram relationship carousel.

Generate exactly {num_tips} relationship principles, then one short closing line.

Rules:
- Each principle must be under 16 words.
- Tone: emotionally mature, calm, psychologically insightful.
- Avoid clichés and dramatic language.
- Aspirational, not preachy.
- Number each principle (1. 2. 3. etc).
- Final line: short emotional closing (max 6 words), no number.
- Return ONLY the numbered principles and the closing line, one per line.
- Do not include a hook or title line.

Generate now.
"""

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
            )

            content = response.choices[0].message.content.strip()

            gpt_lines = [
                re.sub(r'\([A-Za-z_]+\)\s*', '', line).strip()
                for line in content.split("\n")
                if line.strip()
            ]

            return [hook] + gpt_lines

        # ==================================================
        # AI TOOLS NICHE
        # ==================================================
                # ==================================================
        # AI TOOLS NICHE (DETERMINISTIC ENGINE)
        # ==================================================
        elif niche_type == "ai_tools":

            from config.niches import ai_tools as config

            identity = blueprint["identity"]
            institution = blueprint["institution"]

            # --------------------------------------
            # 1️⃣ Build Hook (Authority Frame)
            # --------------------------------------

            hook_template = random.choice(config.HOOK_TEMPLATES)

            hook_text = hook_template.format(
                identity=identity,
                institution=institution
            )

            slides_output = [hook_text.lower()]

            # --------------------------------------
            # 2️⃣ Select Tools (Closed Universe)
            # --------------------------------------

            num_tools = random.randint(
                config.STRUCTURE_RULES["min_items"],
                config.STRUCTURE_RULES["max_items"]
            )

            selected_tools = random.sample(config.TIP_LIBRARY, num_tools)

            # --------------------------------------
            # 3️⃣ Ranking Curve Logic
            # Weak → Mid → Strong → Strongest
            # --------------------------------------

            # Compute average rating potential for each tool
            tool_strength_map = []

            for tool in selected_tools:
                persona = config.TOOL_PERSONAS[tool]
                avg_strength = sum(persona["rating_range"]) / 2
                tool_strength_map.append((tool, avg_strength))

            # Sort ascending (weakest first, strongest last)
            tool_strength_map.sort(key=lambda x: x[1])

            ranked_tools = [t[0] for t in tool_strength_map]

            # --------------------------------------
            # 4️⃣ Build Slides with Deterministic Generator
            # --------------------------------------

            for idx, tool in enumerate(ranked_tools):
                slide_text = config.build_rating_slide(tool, idx + 1)
                slides_output.append(slide_text)

            return slides_output

                # ==================================================
        # MEN'S MOTIVATION — FITNESS ONLY (Deterministic)
        # ==================================================
        elif niche_type == "mens":

            slides = blueprint["slides"]

            # Slides already structured as:
            # hook + 6 goals
            # We simply return clean base_text values

            output = []

            for slide in slides:
                text = slide.get("base_text", slide.get("text", "")).strip()
                output.append(text)

            return output