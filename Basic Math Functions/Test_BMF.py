# START HERE

import unittest
import math
from Basic_Math_Functions import main

class TestMainProgram(unittest.TestCase):

    def test_floor(self):
        # Test case for math.floor()
        self.assertEqual(math.floor(3.7), 3)