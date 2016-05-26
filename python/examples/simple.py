#!/usr/bin/env python

import unicornhat as unicorn
import time

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
width,height=unicorn.get_shape()


for y in range(height):
  for x in range(width):
    unicorn.set_pixel(x,y,255,0,255)
    unicorn.show()
    time.sleep(0.05)

time.sleep(1)
