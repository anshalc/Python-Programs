# START HERE

import unittest
import math
import json
from Python_Programs.BMF import MathOperations
from Python_Programs.CuboidVolumes import DimensionProcessor

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

    def test_Volumes(self):
        # Setup the processor with the file
        processor = DimensionProcessor("/Users/anshalchopra/Documents/Projects/Python Programs/Python_Programs/Datasets/Dimensions.json")
        expected_volumes = []

        # Load the data directly to get the expected volumes
        with open("/Users/anshalchopra/Documents/Projects/Python Programs/Python_Programs/Datasets/Dimensions.json", 'r') as file:
            data = json.load(file)
            for dim in data['dimensions']:
                expected_volume = dim['volume']
                expected_volumes.append(expected_volume)

            # Run the volume calculation
            updated_data = processor.calculateVolumes()
            
            # Extract calculated volumes from the updated data
            calculated_volumes = [dim['volume'] for dim in updated_data['dimensions']]

            # Test if the calculated volumes match the expected volumes
            self.assertEqual(calculated_volumes, expected_volumes)


if __name__ == "__main__":
    unittest.main()