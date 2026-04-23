"""
Generative AI models - ollama ai

__author__ = "vci"
__copyright__ = "Copyright 2026, vci"
__license__ = "MIT"
__version__ = "1.0.0.10"
__maintainer__ = "vci"
__email__ = "modernui.app@gmail.com"
__status__ = "development"
__reference__ = "vci"


"""

from langchain_openai import ChatOpenAI
import openai
from ollama import chat
import requests
import json
from PIL import Image
from io import BytesIO

class GenerativeAI:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        # self.url = "http://localhost:11434/api/chat" # default url for ollama ai

    def generate_text(self, prompt: str, model: str = "glm-5.1:cloud") -> str:
        '''
        generate text using ollama ai
        '''

        # # call ai model using langchain
        # llm = ChatOpenAI(model=model, base_url="http://localhost:11434/", api_key=self.api_key)
        # response = llm.invoke(prompt)
        # return response.content

        #  # use ollama library to call ai model (requires ollama running at localhost:11434)
        # response = chat(model=model, messages=[{"role": "user", "content": prompt}])
        # return response.message.content


        # # call ai model using langchain
        url = "http://localhost:11434/api/chat/" # default url for ollama ai
        # url = "https://api.ollama.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": model,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "stream": False
        }
        # print("payload:", payload)
        response = requests.post(url, headers=headers, json=payload)
        response_json = response.json()
        return response_json["message"]["content"]
        # return response_json["choices"][0]["message"]["content"]
