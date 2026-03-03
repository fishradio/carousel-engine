# agents/strategy.py

import random


class StrategyAgent:

    def __init__(self, niche_module):
        self.niche = niche_module

    def build_blueprint(self):

        # =====================================================
        # COUPLES NICHE (List + Anchor)
        # =====================================================
        if self.niche.NICHE_NAME == "Couples Motivation":

            rules = self.niche.STRUCTURE_RULES
            X = random.randint(rules["min_items"], rules["max_items"])

            hook_template = random.choice(self.niche.HOOK_TEMPLATES)
            hook = hook_template.replace("{X}", str(X))

            slides = []

            # Slide 1 → Hook
            slides.append({
                "type": "hook",
                "text": hook
            })

            # Slides 2–X → Tips
            tips = random.sample(self.niche.TIP_LIBRARY, X)

            for i, tip in enumerate(tips):
                slides.append({
                    "type": "tip",
                    "text": f"{i+1}. {tip}"
                })

            # Final Slide → Anchor (only couples use this)
            if rules.get("include_anchor", True):
                anchor = random.choice(self.niche.ANCHOR_QUOTES)
                slides.append({
                    "type": "anchor",
                    "text": anchor
                })

            return {
                "niche_type": "couples",
                "slides": slides
            }

        # =====================================================
        # AI TOOLS NICHE (Persona + Ranking)
        # =====================================================
        elif self.niche.NICHE_NAME == "AI Tools Ranking":

            rules = self.niche.STRUCTURE_RULES
            X = random.randint(rules["min_items"], rules["max_items"])

            # Persona lock
            identity = random.choice(self.niche.IDENTITIES)
            institution = random.choice(self.niche.INSTITUTIONS)

            hook_template = random.choice(self.niche.HOOK_TEMPLATES)

            hook = hook_template.format(
                identity=identity,
                institution=institution
            )

            slides = []

            # Slide 1 → Hook
            slides.append({
                "type": "hook",
                "text": hook
            })

            # Slides 2–X → Tools (NO numbering here)
            tools = random.sample(self.niche.TIP_LIBRARY, X)

            for tool in tools:
                slides.append({
                    "type": "tool",
                    "text": tool
                })

            return {
                "niche_type": "ai_tools",
                "slides": slides,
                "identity": identity,
                "institution": institution
            }

                # =====================================================
        # MEN'S MOTIVATION (Strict Fitness System)
        # =====================================================
        elif self.niche.NICHE_NAME == "Mens Motivation":

            archetypes = self.niche.ARCHETYPES

            # -------------------------------------------------
            # HOOK
            # -------------------------------------------------

            hook = random.choice(archetypes["hook_templates"])

            # -------------------------------------------------
            # STRICT GOAL STRUCTURE
            # 1 deadlift
            # 1 squat
            # 1 running
            # 1 cycling
            # 1 bodyweight
            # -------------------------------------------------

            slides = [
                {"type": "hook", "base_text": hook},

                {
                    "type": "goal",
                    "category": "deadlift",
                    "base_text": random.choice(archetypes["deadlift_goals"]),
                },

                {
                    "type": "goal",
                    "category": "squat",
                    "base_text": random.choice(archetypes["squat_goals"]),
                },

                {
                    "type": "goal",
                    "category": "running",
                    "base_text": random.choice(archetypes["running_goals"]),
                },

                {
                    "type": "goal",
                    "category": "cycling",
                    "base_text": random.choice(archetypes["cycling_goals"]),
                },

                {
                    "type": "goal",
                    "category": "bodyweight",
                    "base_text": random.choice(archetypes["bodyweight_goals"]),
                },
            ]

            return {
                "niche_type": "mens",  # KEEP THIS
                "slides": slides,
                "viral_mechanics": self.niche.VIRAL_MECHANICS,
                "visual_archetypes": archetypes["visual_archetypes"],
            }