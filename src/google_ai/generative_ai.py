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
    
