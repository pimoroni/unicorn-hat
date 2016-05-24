#!/usr/bin/env python

import unicornhat as UH
import time

UH.set_layout(UH.AUTO)
width,height=UH.get_shape()



for y in range(height):
  for x in range(width):
    UH.set_pixel(x,y,255,0,255)
    UH.show()
    time.sleep(0.05)

time.sleep(1)
