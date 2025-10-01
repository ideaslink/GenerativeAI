"""
Generative AI models - openrouter ai

__author__ = "vci"
__copyright__ = "Copyright 2025, vci"
__license__ = "MIT"
__version__ = "1.0.0.10"
__maintainer__ = "vci"
__email__ = "modernui.app@gmail.com"
__status__ = "development"
__reference__ = "vci"


"""

# from google import genai
# from google.genai import types
# from google.genai.types import Part
import requests
import json
from PIL import Image
from io import BytesIO

class GenerativeAI:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        # self.genai_client = genai.Client(api_key=self.api_key)

    def generate_text(self, prompt: str, model: str = "deepseek/deepseek-chat-v3.1:free") -> str:
        response = requests.post(
            url=f"https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            },
            data=json.dumps({
                "model": model,
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": 4096,
                "temperature": 0.7
            })
        )
        print(f"response: {response}") 
        response_json = response.json()
        response_text = response_json["choices"][0]["message"]["content"]
        return response_text
    
    # def generate_image(self, output_path: str, prompt: str, model: str = "gemini-2.5-flash") -> str:
    #     # config = types.GenerateImagesConfig(
    #     #     response_modalities=["TEXT", "IMAGE"],
    #     #     candidate_count=1)
            
    #     config = types.GenerateContentConfig(
    #         response_modalities=["TEXT", "IMAGE"],
    #         candidate_count=1)

    #     response = self.genai_client.models.generate_content(
    #         model=model,
    #         contents=prompt,
    #         config=config
    #     )

    #     for part in response.candidates[0].content.parts:
    #         print(f"part: {part}")
    #         if part.text:
    #             print(f"part text: {part.text}")
    #         elif part.inline_data is not None:
    #             img = Image.open(BytesIO(part.inline_data.data))
    #             img.save(output_path) # save image to output_path

    #     return f"number of images: {response.candidates.count}" # response.images.count