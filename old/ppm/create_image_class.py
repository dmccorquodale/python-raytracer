from image import Image
import math

myImage = Image(200,100)

r = 80

for i in myImage.pixels:
    for o in i:
        o.x = float(o.x)
        o.y = float(o.y)
        try:
            if ((o.x - math.sqrt((r**2) - (o.y**2)))-100) < 1:
                if ((o.x - math.sqrt((r**2) - (o.y**2)))-100) > -1:
                    print (str(o.x) + " " + str(o.y))
                    o.r = 1.0
                else:
                    print(str(o.x) + " " + str(o.y) + " " + "didn't fit the equation")
            else:
                print(str(o.x) + " " + str(o.y) + " " + "didn't fit the equation")
        except ValueError:
            print ("ValueError - not sure why yet")




myImage.printPPM()