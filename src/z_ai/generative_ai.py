"""
Generative AI models -nvidia ai

__author__ = "vci"
__copyright__ = "Copyright 2026, vci"
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
from openai import OpenAI
import requests
import json
from PIL import Image
from io import BytesIO

class GenerativeAI:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def generate_text(self, prompt: str, model: str = "z-ai/glm4.7") -> str:
        """
        Generate text using the specified model and prompt.
        Args:
            prompt (str): The input prompt for text generation.
            model (str): The model to use for text generation. Default is "Z-ai/glm4.7".
        Returns:
            str: The generated text response from the model.
        """

        # print(f"API Key: {self.api_key}")

        # direct api key call without using the openai client library
        url = "https://integrate.api.nvidia.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": model,
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(url, headers=headers, json=payload)

        # print(response.json())

        # client = OpenAI(
        #     base_url = "https://integrate.api.nvidia.com/v1",
        #     api_key = self.api_key
        # )

        # completion = client.chat.completions.create(
        #     model=model,
        #     messages=[{"role":"user","content":prompt}],
        #     temperature=1,
        #     top_p=1,
        #     max_tokens=16384,
        #     extra_body={"chat_template_kwargs":{"enable_thinking":True,"clear_thinking":False}},
        #     stream=False
        # )

        # response = ""
        # response = completion.choices[0].message.content
   
        ## when stream=True, we need to iterate through the stream to get the full response
        # for chunk in completion:
        #     if not getattr(chunk, "choices", None):
        #         continue
        #     if len(chunk.choices) == 0 or getattr(chunk.choices[0], "delta", None) is None:
        #         continue
        #     delta = chunk.choices[0].delta
        #     if getattr(delta, "content", None) is not None:
        #         response += delta.content

        response = response.json()["choices"][0]["message"]["content"]
        return response
    
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