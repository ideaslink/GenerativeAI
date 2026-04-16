"""
unit tests for ollama ai generative ai

__author__ = "vci"
__copyright__ = "Copyright 2026, vci
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
from ollama_ai.generative_ai import GenerativeAI
from shared.vars import OLLAMA_VARS

class TestGenerativeAI(unittest.TestCase):
    def setUp(self):
        pass

    # @unittest.skip("Skipping test that requires actual API call")
    def test_generative_ai(self):
        """
        test ollama ai generative ai - content generation
        """
        
        # print("openrouter api call")
        model = "gemma4:31b-cloud" # f"glm-5.1:cloud"
        # prompt = "given raw food: shrimp (about 10 pieces), pasta, broccoli, and cheese, suggest a meal recipe with cooking instructions, and provide nutrition facts."
        prompt= """
        You are a nutrition-expert meal planner. 

            Inventory: 2 items of Apples, 2 lbs of Chicken Breast, 2 gallon of Milk, 2 items of Salmon Fillets, 3 lbs of Broccoli, 5 lbs of Beef sirloin , 500 g of Bacon , 2 lbs of Shrimp , 3 lbs of Chicken wings, 5 items of Tomato. 

            Current Preferences: Italian. 

            Generate a full 7-day meal plan (Monday-Sunday). 

            Rules: 

            1. Every meal MUST primarily use the provided Inventory items. 

            2. You may assume basic staples are available: salt, black pepper, olive oil, water, and sugar. 

            3. Do NOT suggest recipes requiring major ingredients NOT in the inventory. 

            4. Output MUST be valid JSON matching this schema: { "week": [{ "day": "Monday", "breakfast": { "title": "Scrambled Eggs", "calories": 300, "protein": 20, "carbs": 1, "fat": 22, "timeMins": 10, "description": "Classic scrambled eggs.", "ingredients": [{"name": "Eggs", "amount": "3"}, {"name": "Salt",  

            "amount": "pinch"}], "instructions": ["Whisk eggs", "Cook in pan"] }, "lunch": { ... }, "dinner": { ... } }] }. 

            5. For each day, include keys "breakfast", "lunch", "dinner". 

            6. The schema for each meal should contain: title (string), calories (integer), protein (integer), carbs (integer), fat (integer), timeMins (integer), description (string), ingredients (array of objects with name and amount), and instructions (array of strings)."
        """

        # prompt = "what can you infer from ‘Shakespeare in AI’? (max: 300 words)."

        apikey = os.getenv( OLLAMA_VARS.get("API_KEY", "") )
        # print(apikey)
        generative_ai = GenerativeAI(api_key = apikey)
        
        response = generative_ai.generate_text(prompt=prompt, model=model)

        print(response)
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()