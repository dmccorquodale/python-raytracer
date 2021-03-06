#!/usr/bin/env python
from image import Image
from colour import Colour

def main():
    WIDTH = 3
    HEIGHT = 2
    im = Image(WIDTH, HEIGHT)
    red = Colour(x=1, y=0, z=0)
    green = Colour(x=0, y=1, z=0)
    blue = Colour(x=0, y=0, z=1)

    im.set_pixel(0, 0, red)
    im.set_pixel(1, 0, blue)
    im.set_pixel(2, 0, green)

    im.set_pixel(0, 1, red + green)
    im.set_pixel(1, 1, red + blue + green)
    im.set_pixel(2, 1, red * 0.001)

    with open("test.ppm", "w") as img_file:
        im.write_ppm(img_file)

if __name__=="__main__":
    main()