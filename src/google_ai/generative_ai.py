"""
Generative AI module for Google Cloud AI Platform

__author__ = "vci"
__copyright__ = "Copyright 2025, vci"
__license__ = "MIT"
__version__ = "1.0.0.10"
__maintainer__ = "vci"
__email__ = "modernui.app@gmail.com"
__status__ = "development"
__reference__ = "vci"


"""

from google import genai
from google.genai import types
from google.genai.types import Part
from PIL import Image
from io import BytesIO

class GenerativeAI:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.genai_client = genai.Client(api_key=self.api_key)

    def generate_text(self, prompt: str, model: str = "gemini-2.5-flash") -> str:
        response = self.genai_client.models.generate_content(
            model=model,
            contents=prompt,
            config={
                "max_output_tokens": 2048
            }   
        )
        return response.text
    
    def generate_image(self, output_path: str, prompt: str, model: str = "gemini-2.5-flash") -> str:
        # config = types.GenerateImagesConfig(
        #     response_modalities=["TEXT", "IMAGE"],
        #     candidate_count=1)
            
        config = types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"],
            candidate_count=1)
        
        # config = types.GenerateImagesConfig(
        #     output_mime_type="image/png",
        #     number_of_images=1)
                
        response = self.genai_client.models.generate_content(
            model=model,
            contents=prompt,
            config=config
        )
        
        # response = self.genai_client.models.generate_images(
        #     model=model,
        #     prompt=prompt,
        #     config=config
        # )

        # print(f"response len: {response.images.count}") # print response)
        
        # for i, img in enumerate(response.images):
        #     with open(output_path, "wb") as f:
        #         f.write(img.data)

        for part in response.candidates[0].content.parts:
            print(f"part: {part}")
            if part.text:
                print(f"part text: {part.text}")
            elif part.inline_data is not None:
                img = Image.open(BytesIO(part.inline_data.data))
                img.save(output_path) # save image to output_path

        # for part in response.candidates[0].content.parts:
        #     if part.inline.data is not None:
        #         img = Image.open(BytesIO(part.inline.data))
        #         img.save(output_path)

        return f"number of images: {response.candidates.count}" # response.images.count