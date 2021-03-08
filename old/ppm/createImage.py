from pixel import Pixel
from pixel import Colour

resolutionX = 50
resolutionY = 25

whiteColour = Colour(1,1,1)
redColour = Colour(1,0,0)

myImage = []

lineEquation = ""
pointA = [0,0]
pointB = [resolutionX,resolutionY]
f = resolutionX/resolutionY
print (f)
#y = (resolutionY/resolutionX)*x

for y in range(1,resolutionY+1):
    thisRow = []
    for x in range(1,resolutionX+1):
        thisPixel = Pixel(x,y)
        if x==0.5*y:
            thisPixel.g = 1
            thisPixel.b = 0.5
        thisRow.append(thisPixel)
    myImage.append(thisRow)

myPrintedImage = "P3 " + str(resolutionX) + " " + str(resolutionY) + "\n255\n"

for i in myImage:
    for ii in i:
        myPrintedImage = myPrintedImage + ii.PPMColour()
    myPrintedImage = myPrintedImage + "\n"

print (myPrintedImage)