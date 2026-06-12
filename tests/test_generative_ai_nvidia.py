import unittest
import os
import sys
# Adjust the path to include the src directory to avoid import headache
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
if src_path not in sys.path:
    sys.path.insert(0, src_path)
from nvidia_ai.generative_ai import GenerativeAI
from shared.vars import NVIDIA_VARS

class TestGenerativeAI(unittest.TestCase):
    def setUp(self):
        pass

    # @unittest.skip("Skipping test that requires actual API call")
    def test_generative_ai(self):
        """
        test nvidia generative ai - content generation
        """
        
        # print("nvidia api call") 
        model="nvidia/nemotron-3-ultra-550b-a55b"
        endpoint = "https://integrate.api.nvidia.com/v1/chat/completions" # "https://api.navy/v1/chat/completions"
        # prompt = "given raw food: shrimp (about 10 pieces), pasta, broccoli, and cheese, suggest a meal recipe with cooking instructions, and provide nutrition facts."
        prompt = "what can you infer from ‘Shakespeare in AI’? (max: 300 words)."
        generative_ai = GenerativeAI(api_key = os.getenv( NVIDIA_VARS.get("API_KEY", "") ) )
        response = generative_ai.generate_text(prompt=prompt, model=model, endpoint=endpoint)

        print(f"response: {response}")
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()