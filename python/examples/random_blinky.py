#!/usr/bin/env python

import unicornhat as unicorn
import time, colorsys
import numpy as np

unicorn.brightness(0.5)

while True:
	rand_mat = np.random.rand(8,8)	
	for y in range(8):
		for x in range(8):
			h = 0.1 * rand_mat[x, y]
			s = 0.8
			v = rand_mat[x, y]
			rgb = colorsys.hsv_to_rgb(h, s, v)
			r = int(rgb[0]*255.0)
			g = int(rgb[1]*255.0)
			b = int(rgb[2]*255.0)
			unicorn.set_pixel(x, y, r, g, b)
	unicorn.show()
	time.sleep(0.01)
