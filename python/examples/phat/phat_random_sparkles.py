#!/usr/bin/env python

import unicornhat as u
from random import randint

u.set_layout(u.PHAT)

while True:
    x = randint(0, 7)
    y = randint(0, 4)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    u.set_pixel(x, y, r, g, b)
    u.show()
