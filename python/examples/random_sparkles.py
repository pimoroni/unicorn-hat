#!/usr/bin/env python

import unicornhat as unicorn
from random import randint

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.4)
width,height=unicorn.get_shape()

while True:
    x = randint(0, (width-1))
    y = randint(0, (height-1))
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    unicorn.set_pixel(x, y, r, g, b)
    unicorn.show()
