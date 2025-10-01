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

from urllib import response
from google import genai
from google.genai import types
from google.genai.types import Part
from PIL import Image
from io import BytesIO
import os
import base64

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

        for part in response.candidates[0].content.parts:
            # print(f"part: {part}")
            if part.text:
                print(f"part text: {part.text}")
            elif part.inline_data is not None:
                img = Image.open(BytesIO(part.inline_data.data))
                img.save(output_path) # save image to output_path


        return f"number of images: {response.candidates.count}" # response.images.count

    def generate_image_edit(self, input_path: str, output_path: str, prompt: str, model: str = "gemini-2.5-flash-image-preview") -> str:
        """
            generate an edited image based on input image and prompt

            input_path: path to input image
            output_path: path to save output image            
            prompt: prompt for editing
            model: model to use
        
        """

        # # test: display the input 
        
        img = Image.open(input_path)
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        img_bytes = buffer.getvalue()

        image_orig = types.Part.from_bytes(data=img_bytes, mime_type="image/png") # Image.open(input_path)
        text_prompt = types.Part.from_text(text=prompt)
            
        # specify contents
        contents = [
            types.Content(
                role="user",
                parts=[
                    text_prompt,
                    image_orig
                ]
            )
        ]

        config = types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"],
            candidate_count=1,
            max_output_tokens=32768)
                
        response = self.genai_client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=config
        )

        # extract image
        cnt = 0
        for chunk in response:
            for part in chunk.candidates[0].content.parts:
                if part.inline_data:
                    image_bytes = part.inline_data.data
                    image = Image.open(BytesIO(image_bytes))
                    image.save(output_path)
                    image.show()  # Optional: display the image
                    cnt += 1

        return f"returned {cnt}" # response.images.count