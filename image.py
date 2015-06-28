#!/usr/bin/python3

from PIL import Image

blank_image = Image.new("RGB", (1050, 350))

im1 = Image.open('8-1.png')

blank_image.paste(im1, (0,0))

blank_image.show()
