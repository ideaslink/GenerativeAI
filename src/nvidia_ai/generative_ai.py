"""
Generative AI models - nvidia ai

__author__ = "vci"
__copyright__ = "Copyright 2026, vci"
__license__ = "MIT"
__version__ = "1.0.0.10"
__maintainer__ = "vci"
__email__ = "modernui.app@gmail.com"
__status__ = "development"
__reference__ = "vci"


"""

# from langchain_openai import ChatOpenAI
from openai import OpenAI
import requests
import json

class GenerativeAI:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def generate_text(self, prompt: str, model: str = "gpt-4.1", endpoint: str = "default") -> str:
        '''
        generate text using nvidia ai
        '''

        # # print(f"endpoint: {endpoint}" )
        # print(f"model: {model}" )
        # client = OpenAI(api_key=self.api_key, base_url=endpoint)
        # response = client.chat.completions.create(
        #     model=model,
        #     messages=[{"role": "user", "content": prompt}],
        #     max_tokens=12288,
        #     temperature=0.7
        # )

        # print(f"response: {response}")
        # return response.choices[0].message.content


        # by requests (tested successfully)
        response = requests.post(
            url= endpoint,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            },
            data=json.dumps({
                "model": model,
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": 12288,
                "temperature": 0.7
            })
        )
        print(f"response: {response}") 
        response_json = response.json()
        response_text = response_json["choices"][0]["message"]["content"]
        return response_text