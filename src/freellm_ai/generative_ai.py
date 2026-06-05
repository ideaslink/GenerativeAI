"""
Generative AI models - freellm ai

__author__ = "vci"
__copyright__ = "Copyright 2026, vci"
__license__ = "MIT"
__version__ = "1.0.0.10"
__maintainer__ = "vci"
__email__ = "modernui.app@gmail.com"
__status__ = "development"
__reference__ = "vci"


"""

from openai import OpenAI
import requests
import json

class GenerativeAI:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def generate_text(self, url: str, prompt: str, model: str = "auto") -> str:
        '''
        generate text using freellm ai
        '''
        # use openai library to call ai model
        llm = OpenAI(base_url=url, api_key=self.api_key)
        resp = llm.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=12288,
            temperature=0.7
        )

        return resp.choices[0].message.content
