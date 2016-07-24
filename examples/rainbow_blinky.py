#!/usr/bin/env python

import colorsys
import time

try:
    import numpy as np
except ImportError:
    exit("This script requires the numpy module\nInstall with: sudo pip install numpy")

import unicornhat as unicorn


unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0) # tested on pHAT/HAT with rotation 0, 90, 180 & 270
unicorn.brightness(0.4)
width,height=unicorn.get_shape()

if height==width:
    delta=0
else:
    delta=2


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
                if height<=width:
                    v = gauss[x,y+delta]
                else:
                    v = gauss[x+delta,y]
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
