# START HERE

class MathOperations:
    
    # Constructor with an Argument
    def  __init__(self, num=1):
        self.num = num

    # Round Up Function Comparable to math.ceil
    def roundUp(self):
        if(self.num > 0):
            if(self.num > int(self.num)):
               return int(self.num) + 1
            else:
                return int(self.num)
        else:
            if(self.num < int(self.num)):
               return int(self.num)
            else:
                return int(self.num)
            
    # Round Down Function Comparable to math.floor
    def roundDown(self):
        if(self.num > 0):
            if(self.num > int(self.num)):
               return int(self.num)
            else:
                return int(self.num)
        else:
            if(self.num < int(self.num)):
               return int(self.num) - 1
            else:
                return int(self.num)
            
    # Round Function Comparable to round
    def justRound(self):
        if(self.num > 0):
            if(self.num > float(int(self.num) + 0.5)):
               return int(self.num) + 1
            else:
                return int(self.num)
        else:
            if(self.num > float(int(self.num) - 0.5)):
               return int(self.num)
            else:
                return int(self.num) - 1
