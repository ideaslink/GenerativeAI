"""
unit tests for google generative ai

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
from google_ai.generative_ai import GenerativeAI
from shared.vars import GCP_VARS

class TestGenerativeAI(unittest.TestCase):
    def setUp(self):
        pass

    def test_generative_ai(self):
        """
        test google generative ai - content generation
        """
        
        # print("calling gemini api")
        generative_ai = GenerativeAI(api_key = os.getenv( GCP_VARS.get("API_KEY", "") ) )
        response = generative_ai.generate_text(prompt="what can you infer from ‘Shakespeare in AI’? (max: 300 words).", model="gemini-2.5-flash")

        print(response)
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)

    def tearDown(self):
        pass
        # sys.path.pop(0)

if __name__ == '__main__':
    unittest.main()