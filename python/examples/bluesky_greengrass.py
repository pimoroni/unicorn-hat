#!/usr/bin/env python

import unicornhat as unicorn
import time

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
width,height=unicorn.get_shape()

unicorn.brightness(0.4)

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

