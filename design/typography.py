# design/typography.py

from PIL import Image, ImageDraw, ImageFont
import textwrap


class TypographyEngine:

    def __init__(self, niche_type="mens"):

        self.niche_type = niche_type

        if niche_type == "couples":
            self.font_path = "fonts/InterVariable.ttf"
        elif niche_type == "ai_tools":
            self.title_font_path = "fonts/Arial Bold.ttf"
            self.body_font_path = "fonts/Arial.ttf"
        else:
            self.font_path = "fonts/InterVariable.ttf"

    def add_text_overlay(self, image_path, text, output_path, is_hook=False):

        image = Image.open(image_path).convert("RGBA")
        width, height = image.size
        draw = ImageDraw.Draw(image)

        # =====================================================
        # AI TOOLS STYLE (NEW — DOES NOT TOUCH OTHER NICHES)
        # =====================================================

        if self.niche_type == "ai_tools":

            if is_hook:

                font_size = int(height * 0.04)
                font = ImageFont.truetype(self.title_font_path, font_size)

                max_width_ratio = 0.80
                line_spacing = 10

                # Word wrap
                words = text.split()
                lines = []
                current_line = ""

                for word in words:
                    test_line = f"{current_line} {word}".strip()
                    bbox = draw.textbbox((0, 0), test_line, font=font)
                    if bbox[2] - bbox[0] <= width * max_width_ratio:
                        current_line = test_line
                    else:
                        lines.append(current_line)
                        current_line = word

                lines.append(current_line)
                wrapped_text = "\n".join(lines)

                bbox = draw.multiline_textbbox(
                    (0, 0), wrapped_text, font=font, spacing=line_spacing
                )
                text_w = bbox[2] - bbox[0]

                x = (width - text_w) / 2
                y = height * 0.06

                draw.multiline_text(
                    (x, y),
                    wrapped_text,
                    font=font,
                    fill=(255, 255, 255),
                    stroke_width=5,
                    stroke_fill=(0, 0, 0),
                    align="center",
                    spacing=line_spacing
                )

                image.save(output_path)
                return

            blocks = [b.strip() for b in text.split("\n\n") if b.strip()]

            title_font = ImageFont.truetype(
                self.title_font_path, int(height * 0.042)
            )
            body_font = ImageFont.truetype(
                self.body_font_path, int(height * 0.038)
            )

            current_y = int(height * 0.15)

            for i, block in enumerate(blocks):

                font = title_font if i == 0 else body_font

                wrapped = textwrap.fill(block, width=28)

                bbox = draw.multiline_textbbox(
                    (0, 0), wrapped, font=font, spacing=4
                )
                text_w = bbox[2] - bbox[0]
                text_h = bbox[3] - bbox[1]

                padding_x = 35
                padding_y = 16

                box_w = text_w + padding_x * 2
                box_h = text_h + padding_y * 2

                x = (width - box_w) // 2
                y = current_y

                # White rounded box
                draw.rounded_rectangle(
                    [x, y, x + box_w, y + box_h],
                    radius=22,
                    fill=(255, 255, 255, 255)
                )

                # Text
                draw.multiline_text(
                    (x + box_w / 2, y + box_h / 2),
                    wrapped,
                    fill=(0, 0, 0),
                    font=font,
                    spacing=4,
                    anchor="mm",
                    align="center"
                )

                current_y += box_h + 35

            image.save(output_path)
            return

        # =====================================================
        # EXISTING NICHE SETTINGS (UNCHANGED)
        # =====================================================

        if self.niche_type == "couples":

            font_size = int(height * 0.032)
            max_width_ratio = 0.70
            y_position = 0.47
            line_spacing = 4
            text = text

        else:  # men's motivation

            font_size = int(height * 0.032)
            max_width_ratio = 0.80
            y_position = 0.55
            line_spacing = 5

        font = ImageFont.truetype(self.font_path, font_size)

        # =====================================================
        # WORD WRAP (UNCHANGED)
        # =====================================================

        words = text.split()
        lines = []
        current_line = ""

        for word in words:
            test_line = f"{current_line} {word}".strip()
            bbox = draw.textbbox((0, 0), test_line, font=font)
            if bbox[2] - bbox[0] <= width * max_width_ratio:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word

        lines.append(current_line)
        wrapped_text = "\n".join(lines)

        x = width / 2
        y = height * y_position

        # =====================================================
        # COUPLES STYLE (UNCHANGED)
        # =====================================================

        if self.niche_type == "couples":

            shadow_color = (0, 0, 0, 170)

            for offset in [(0, 4), (0, 5), (0, 6)]:
                draw.multiline_text(
                    (x + offset[0], y + offset[1]),
                    wrapped_text,
                    font=font,
                    fill=shadow_color,
                    anchor="mm",
                    align="center",
                    spacing=line_spacing
                )

            draw.multiline_text(
                (x, y),
                wrapped_text,
                font=font,
                fill=(255, 255, 255, 255),
                anchor="mm",
                align="center",
                spacing=line_spacing
            )

        # =====================================================
        # MEN'S STYLE (UNCHANGED)
        # =====================================================

        else:

            draw.multiline_text(
                (x, y),
                wrapped_text,
                font=font,
                fill="white",
                stroke_width=3,
                stroke_fill="black",
                anchor="mm",
                align="center",
                spacing=line_spacing
            )

        image.save(output_path)