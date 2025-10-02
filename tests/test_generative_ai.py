"""
unit tests for generative ai

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

    @unittest.skip("Skipping test that requires actual API call")
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

    @unittest.skip("Skipping test that requires actual API call")
    def test_generative_image(self):
        """
        test google generative ai - image generation
        """
        
        # print("calling gemini api")
        generative_ai = GenerativeAI(api_key = os.getenv( GCP_VARS.get("API_KEY", "") ) )
        output_path = "../_assets/ai_gcp_image.png"
        response = generative_ai.generate_image(output_path=output_path, prompt="generate an image: a logo for AI Frontiers.", model="gemini-2.5-flash-image-preview")

        # print(response)
        self.assertTrue(os.path.exists(output_path))

    # @unittest.skip("Skipping test that requires actual API call")
    def test_generative_image_edit(self):
        """
        test google generative ai - image editing
        """
        
        # print("calling gemini api")
        generative_ai = GenerativeAI(api_key = os.getenv( GCP_VARS.get("API_KEY", "") ) )
        input_path = "../_assets/ai_gcp_image_original.png" # 
        # input_path = "https://images.pexels.com/photos/2071873/pexels-photo-2071873.jpeg" # "https://cdn.pixabay.com/photo/2022/03/27/11/23/cat-7094808_1280.jpg"
        # input_path = "https://cdn.pixabay.com/photo/2023/05/02/14/15/british-shorthair-7965411_1280.jpg" 
        output_path = "../_assets/ai_gcp_image_edited.png"
        response = generative_ai.generate_image_edit(input_path=input_path, output_path=output_path, prompt="edit the image to add a tie to the cat. make the cat sit near a swimming pool.", model="gemini-2.5-flash-image-preview")

        print(response)
        self.assertTrue(os.path.exists(output_path))


    def tearDown(self):
        pass
        # sys.path.pop(0)

if __name__ == '__main__':
    unittest.main()