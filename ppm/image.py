from pixel import Pixel

class Image:

    def __init__(self, xRes=0, yRes=0):
        self.xRes = xRes
        self.yRes = yRes
        self.pixels = []
        
        for y in range(1,yRes+1):
            thisRow = []
            for x in range(1,xRes+1):
                thisPixel = Pixel(x,y)
                thisRow.append(thisPixel)
            self.pixels.append(thisRow)

    def printPPM(self):
        myPrintedImage = "P3 " + str(self.xRes) + " " + str(self.yRes) + "\n255\n"

        for i in self.pixels:
            for ii in i:
                myPrintedImage = myPrintedImage + ii.PPMColour()
            myPrintedImage = myPrintedImage + "\n"

        print (myPrintedImage)