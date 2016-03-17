#!/usr/bin/env python

'''
This basic example shows use of the Python Pillow library:

sudo pip-3.2 install pillow # or sudo pip install pillow

The tiny 8x8 chars in lofi.png are from Oddball:
http://forums.tigsource.com/index.php?topic=8834.0

Licensed under Creative Commons Attribution-Noncommercial-Share Alike 3.0 Unported License.
'''

import unicornhat as unicorn
from PIL import Image
import signal, numpy, time

unicorn.rotation(90)
unicorn.brightness(0.9)

img = Image.open('lofi.png')

for o_x in range(int(img.size[0]/8)):
	for o_y in range(int(img.size[1]/8)):

		for x in range(8):
			for y in range(8):
				pixel = img.getpixel(((o_x*8)+y,(o_y*8)+x))
				print(pixel)
				r, g, b = int(pixel[0]),int(pixel[1]),int(pixel[2])
				unicorn.set_pixel(x, y, r, g, b)
		unicorn.show()
		time.sleep(0.5)
