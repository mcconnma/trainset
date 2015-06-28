#!/usr/bin/python3

import glob
import sys
import math
from PIL import Image

depth = str(sys.argv[1])
images = glob.glob(depth + '*.png')

im_width = 400
im_height = 400
num_images_width = 3
height = int(math.ceil(len(images)/num_images_width))

blank_image = Image.new("RGB", (im_width * num_images_width, im_height * height) , "white")

count = 0
curr_height = 0
for image in images:
	i = Image.open(image)
	print("opening image: " +  image)
	blank_image.paste(i, (count * im_width, curr_height))
	count = count + 1
	if count == num_images_width:
		count = 0
		curr_height = curr_height + im_height

blank_image.show()

blank_image.save(depth + '.png')
