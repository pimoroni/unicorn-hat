#!/usr/bin/env python

import unicornhat as UH
import time

for y in range(8):
  for x in range(8):
    UH.set_pixel(x,y,255,0,255)
    UH.show()
    time.sleep(0.05)

time.sleep(1)
