#from vector import Vector
class Pixel:

    def __init__(self, x=1, y=1, r=0.0, g=0.0, b=0.0):
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.b = b

    def PPMColour(self):
        self.r = self.r * 255
        self.g = self.g * 255
        self.b = self.b * 255
        self.r = int(self.r)
        self.g = int(self.g)
        self.b = int(self.b)
        return str(self.r) + " " + str(self.g) + " " + str(self.b) + " "

class Colour:

    def __init__(self, r=0.0, g=0.0, b=0.0, a=0.0):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def PPMColour(self):
        self.r = self.r * 255
        self.g = self.g * 255
        self.b = self.b * 255
        return str(self.r) + " " + str(self.g) + " " + str(self.b) + " "