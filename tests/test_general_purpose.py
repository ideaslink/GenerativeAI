"""
general purpose test 

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

class TestGeneral(unittest.TestCase):
    def setUp(self):
        pass

    def test_environment_var(self):
        """
        test environment variable
        """
        api_key = ""
        api_key = os.getenv("API_KEY")

        print(api_key)
        self.assertIsInstance(api_key, str)
        self.assertGreater(len(api_key), 0)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()