#!/usr/bin/env python

import unicornhat as unicorn
import time, colorsys
import numpy as np

unicorn.set_layout(unicorn.AUTO)
width,height=unicorn.get_shape()

if height==4:
    delta=2
else:
    delta=0


def make_gaussian(fwhm):
	x = np.arange(0, 8, 1, float)
	y = x[:, np.newaxis]
	x0, y0 = 3.5, 3.5
	fwhm = fwhm
	gauss = np.exp(-4 * np.log(2) * ((x - x0) ** 2 + (y - y0) ** 2) / fwhm ** 2)
	return gauss

while True:
	for z in list(range(1, 10)[::-1]) + list(range(1, 10)):
		fwhm = 5.0/z
		gauss = make_gaussian(fwhm)
                start = time.time()
		for y in range(height):
			for x in range(width):
				h = 1.0/(x + y + delta + 1)
				s = 0.8
				v = gauss[x,y+delta]
				rgb = colorsys.hsv_to_rgb(h, s, v)
				r = int(rgb[0]*255.0)
				g = int(rgb[1]*255.0)
				b = int(rgb[2]*255.0)
				unicorn.set_pixel(x, y, r, g, b)
		unicorn.show()
                end = time.time()
                t = end - start
                if t < 0.04:
		    time.sleep(0.04 - t)
