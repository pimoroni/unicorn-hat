#!/usr/bin/env python

from random import randint

import unicornhat as unicorn


print("""Random Sparkles

Displays random, colorful sparkles.

If you're using a Unicorn HAT and only half the screen lights up, 
edit this example and  change 'unicorn.AUTO' to 'unicorn.HAT' below.
""")

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()

while True:
    x = randint(0, (width-1))
    y = randint(0, (height-1))
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    unicorn.set_pixel(x, y, r, g, b)
    unicorn.show()
