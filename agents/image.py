from openai import OpenAI
from dotenv import load_dotenv
import os
import base64

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class ImageAgent:
    def generate_images(self, prompts):
        import base64

        output_paths = []

        for i, prompt in enumerate(prompts):
            result = client.images.generate(
                model="gpt-image-1",
                prompt=prompt,
                size="1024x1536"
            )

            image_base64 = result.data[0].b64_json
            image_bytes = base64.b64decode(image_base64)

            output_path = f"output/slide_{i+1}.png"

            with open(output_path, "wb") as f:
                f.write(image_bytes)

            output_paths.append(output_path)

        return output_paths