#!/usr/bin/env python

import time

import unicornhat as unicorn


print("""Blue Sky, Green Grass

Displays a horizon on your Unicorn HAT/pHAT so you can
see which orientation is which.

If you're using a Unicorn HAT and only half the screen lights up, 
edit this example and  change 'unicorn.AUTO' to 'unicorn.HAT' below.
""")

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()

y=0
for x in range(width):
  unicorn.set_pixel(x,y,0,255,0)
  unicorn.show()
  time.sleep(0.05)

y=height-1
for x in range(width):
  unicorn.set_pixel(x,y,0,0,255)
  unicorn.show()
  time.sleep(0.05)

for y in range(1,3):
  for x in range(0,y):
    unicorn.set_pixel(x,y,255,0,0)
    unicorn.show()
    time.sleep(0.05)

time.sleep(10)
