#!/usr/bin/env python

import unicornhat as unicorn
import time, math, colorsys

print("Reticulating splines")
time.sleep(.5)
print("Enabled unicorn poop module!")
time.sleep(.5)
print("Pooping rainbows...")

unicorn.brightness(0.1)

i = 0.0
offset = 30
while True:
        i = i + 0.3
        for y in range(8):
                for x in range(8):
                        r = 0#x * 32
                        g = 0#y * 32
                        xy = x + y / 4
                        r = (math.cos((x+i)/2.0) + math.cos((y+i)/2.0)) * 64.0 + 128.0
                        g = (math.sin((x+i)/1.5) + math.sin((y+i)/2.0)) * 64.0 + 128.0
                        b = (math.sin((x+i)/2.0) + math.cos((y+i)/1.5)) * 64.0 + 128.0
                        r = max(0, min(255, r + offset))
                        g = max(0, min(255, g + offset))
                        b = max(0, min(255, b + offset))
                        unicorn.set_pixel(x,y,int(r),int(g),int(b))
        unicorn.show()
        time.sleep(0.01)
