"""
unit tests for Z-ai generative ai

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
from z_ai.generative_ai import GenerativeAI
from shared.vars import ZAI_VARS

class TestGenerativeAI(unittest.TestCase):
    def setUp(self):
        pass

    # @unittest.skip("Skipping test that requires actual API call")
    def test_generative_ai(self):
        """
        test zai generative ai - content generation
        """
        
        # print("openrouter api call")
        model = f"z-ai/glm4.7"
        prompt = "given raw food: shrimp (about 10 pieces), pasta, broccoli, and cheese, suggest a meal recipe with cooking instructions, and provide nutrition facts."
        # prompt= """
        # You are a nutrition-expert meal planner. 

        #     Inventory: 2 items of Apples, 0.25 lbs of Chicken Breast, 0 gallon of Milk, 0 items of Salmon Fillets, 0 lbs of Broccoli, 1.0625 lbs of Beef sirloin , 180.5 g of Bacon , 0.25 lbs of Shrimp , 1 lbs of Chicken wings , 4 lbs of Chicken wings, 2.5 items of Tomato. 

        #     Current Preferences: Italian. 

        #     Generate a full 7-day meal plan (Monday-Sunday). 

        #     Rules: 

        #     1. Every meal MUST primarily use the provided Inventory items. 

        #     2. You may assume basic staples are available: salt, black pepper, olive oil, water, and sugar. 

        #     3. Do NOT suggest recipes requiring major ingredients NOT in the inventory. 

        #     4. Output MUST be valid JSON matching this schema: { "week": [{ "day": "Monday", "breakfast": { "title": "Scrambled Eggs", "calories": 300, "protein": 20, "carbs": 1, "fat": 22, "timeMins": 10, "description": "Classic scrambled eggs.", "ingredients": [{"name": "Eggs", "amount": "3"}, {"name": "Salt",  

        #     "amount": "pinch"}], "instructions": ["Whisk eggs", "Cook in pan"] }, "lunch": { ... }, "dinner": { ... } }] }. 

        #     5. For each day, include keys "breakfast", "lunch", "dinner". 

        #     6. The schema for each meal should contain: title (string), calories (integer), protein (integer), carbs (integer), fat (integer), timeMins (integer), description (string), ingredients (array of objects with name and amount), and instructions (array of strings)."
        # """

        # prompt = "what can you infer from ‘Shakespeare in AI’? (max: 300 words)."
        apikey = os.getenv( ZAI_VARS.get("API_KEY", "") )
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