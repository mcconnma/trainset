#!/usr/bin/python3

from PIL import Image

blank_image = Image.new("RGB", (1050, 350))

im1 = Image.open('example1.png')
im2 = Image.open('example2.png')
im3 = Image.open('example3.png')

blank_image.paste(im1, (0,0))
blank_image.paste(im2, (350,0))
blank_image.paste(im3, (700,0))

blank_image.show()
