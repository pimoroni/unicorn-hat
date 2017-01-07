#!/usr/bin/env python

from time import sleep

import unicornhat as unicorn


print("""ASCII Pic

You should see a scrolling image, defined in the below variable ASCIIPIC.

If the smiley looks sad, change the rotation from 0 to 180.
""")

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()

# Every line needs to be exactly 8 characters
# but you can have as many lines as you like.
ASCIIPIC = [
     "  X  X  "
    ,"        "
    ,"X      X"
    ," XXXXXX "
    ,"        "
    ,"        "
    ,"        "
    ]
i = -1

def step():
    global i
    i = 0 if i>=100*len(ASCIIPIC) else i+1 # avoid overflow
    for h in range(height):
        for w in range(width):
            hPos = (i+h) % len(ASCIIPIC)
            chr = ASCIIPIC[hPos][w]
            if chr == ' ':
                unicorn.set_pixel(w, h, 0, 0, 0)
            else:
                unicorn.set_pixel(w, h, 255, 0, 0)
    unicorn.show()

while True:
    step()
    sleep(0.2)
