# START HERE

import unittest
import math
from Python_Programs.BMF import MathOperations

class TestMathOperations(unittest.TestCase):

    def test_roundUp(self):
        self.assertEqual(MathOperations(-1.2).roundUp(), math.ceil(-1.2))
        self.assertEqual(MathOperations().roundUp(), 0)
        self.assertEqual(MathOperations(10000000000.2).roundUp(), math.ceil(10000000000.2))
        self.assertEqual(MathOperations(-10000000000.2).roundUp(), math.ceil(-10000000000.2))
    
    def test_roundDown(self):
        self.assertEqual(MathOperations(-1.2).roundDown(), math.floor(-1.2))
        self.assertEqual(MathOperations().roundDown(), 0)
        self.assertEqual(MathOperations(10000000000.2).roundDown(), math.floor(10000000000.2))
        self.assertEqual(MathOperations(-10000000000.2).roundDown(), math.floor(-10000000000.2))
    
    def test_justRound(self):
        self.assertEqual(MathOperations(-1.2).justRound(), round(-1.2))
        self.assertEqual(MathOperations().justRound(), 0)
        self.assertEqual(MathOperations(10000000000.2).justRound(), round(10000000000.2))
        self.assertEqual(MathOperations(-10000000000.6).justRound(), round(-10000000000.6))

if __name__ == "__main__":
    unittest.main()