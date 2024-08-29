# STARTS HERE
import json

class DimensionProcessor:
    
    def __init__(self, filename):
        self.filename = filename
        self.data = None

    def readDimensions(self):
    # Reads lengths, breadths, and widths from the JSON file into arrays.
        with open(self.filename, 'r') as file:
            self.data = json.load(file)
        
        lengths = [dim['length'] for dim in self.data['dimensions']]
        breadths = [dim['breadth'] for dim in self.data['dimensions']]
        widths = [dim['width'] for dim in self.data['dimensions']]
        
        return lengths, breadths, widths
    
    def calculateVolumes(self):
        # Calculates volumes based on lengths, breadths, and widths, then appends them to the dictionary."""
        if self.data is None:
            self.readDimensions()
        
        for dim in self.data['dimensions']:
            dim['volume'] = dim['length'] * dim['breadth'] * dim['width']
        
        return self.data
    


