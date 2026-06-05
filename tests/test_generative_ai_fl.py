"""
unit tests for freellm ai

__author__ = "vci"
__copyright__ = "Copyright 2026, vci
__license++ = "MIT
__version__ = "1.0.0.10"
__maintainer__ = "vci"
__email__ = "modernui.app@gmail.com
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
from freellm_ai.generative_ai import GenerativeAI
from shared.vars import FREELLM_VARS

class TestGenerativeAI(unittest.TestCase):
    def setUp(self):
        pass

    # @unittest.skip("Skipping test that requires actual API call")
    def test_generative_ai(self):
        """
        test freellm generative ai - content generation
        """
        
        # print("openrouter api call") 
        model = "auto"
        url = "http://localhost:3001/v1"
        # prompt = "given raw food: shrimp (about 10 pieces), pasta, broccoli, and cheese, suggest a meal recipe with cooking instructions, and provide nutrition facts."
        prompt = "what can you infer from ‘Shakespeare in AI’? (max: 300 words)."
        generative_ai = GenerativeAI(api_key = os.getenv( FREELLM_VARS.get("API_KEY", "") ) )
        response = generative_ai.generate_text(url=url, prompt=prompt, model=model)

        print(f"response: {response}")
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()