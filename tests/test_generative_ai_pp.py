"""
unit tests for openrouter perplexity ai

__author__ = "vci"
__copyright__ = "Copyright 2025, vci
__license++ = "MIT
__version__ = "1.0.0.10"
__maintainer__ = "vci"
__email__ = "contact@hsharp.com"
__status__ = "development"
__reference__ = "vci"

"""

import unittest
import os
import sys
# Adjust the path to include the src directory to avoid import headache
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
if src_path not in sys.path:
    sys.path.insert(0, src_path)
from shared.vars import PERPLEXITY_VARS
from perplexity_ai.generative_ai import GenerativeAI


class TestGenerativeAI(unittest.TestCase):
    def setUp(self):
        pass

    # @unittest.skip("Skipping test that requires actual API call")
    def test_generative_ai(self):
        """
        test perplexity generative ai - content generation
        """
        
        # # print("openrouter api call")
        model = "sonar"
        prompt = "given raw food: shrimp (about 10 pieces), pasta, broccoli, and cheese, " \
        "suggest a meal recipe with cooking instructions, and provide nutrition facts (along with % of daily value)."
        # Modify the prompt to request JSON format for recipe and nutritional facts
        prompt = (
            f"{prompt}\n\n"
            "Please provide the response in JSON format with the following structure:\n"
            "{\n"
            "  \"recipe\": \"<recipe name>\",\n"
            "  \"ingredients\": [\"<ingredient 1>\", \"<ingredient 2>\", ...],\n"
            "  \"steps\": [\"<step 1>\", \"<step 2>\", ...],\n"
            "  \"nutritional_facts\": {\n"
            "    \"calories\": \"<calories>\",\n"
            "    \"protein\": \"<protein>\",\n"
            "    \"fat\": \"<fat>\",\n"
            "    \"carbohydrates\": \"<carbohydrates>\"\n"
            "  }\n"
            "}"
        )
        # prompt = "what can you infer from ‘Shakespeare in AI’? (max: 300 words)."

        generative_ai = GenerativeAI(api_key = os.getenv( PERPLEXITY_VARS.get("API_KEY", "") ) )
        response = generative_ai.generate_text(prompt=prompt, model=model)

        print(response)
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()