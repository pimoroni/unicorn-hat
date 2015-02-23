#!/usr/bin/env python

import unicornhat as unicorn
import time, colorsys

print("Reticulating splines")
time.sleep(.5)
print("Enabled unicorn poop module!")
time.sleep(.5)
print("Pooping rainbows...")

unicorn.brightness(0.9)

while True:
        for z in range(360):
                for y in range(8):
                        for x in range(8):
                                rgb = colorsys.hsv_to_rgb(z/360.0,y/7.0,x/7.0)
                                r = x * 32
                                g = y * 32
                                b = 255 - (x * 32)
                                unicorn.set_pixel(x,y,int(r),int(g),int(b))
                unicorn.show()
                time.sleep(0.1)
