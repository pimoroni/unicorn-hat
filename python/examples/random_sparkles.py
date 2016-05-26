#!/usr/bin/env python

import unicornhat as u
from random import randint

u.set_layout(u.AUTO)
u.rotation(0)
width,height=u.get_shape()


while True:
    x = randint(0, (width-1))
    y = randint(0, (height-1))
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    u.set_pixel(x, y, r, g, b)
    u.show()
