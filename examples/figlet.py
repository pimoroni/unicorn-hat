#!/usr/bin/env python

from time import sleep
from sys import exit

try:
    from pyfiglet import figlet_format
except ImportError:
    exit("This script requires the pyfiglet module\nInstall with: sudo pip install pyfiglet")

import unicornhat as unicorn


print("""Figlet

You should see scrolling text that is defined in the TXT variable.

If the text moves in the wrong direction, change the rotation from 0 to 180.

Text output is kind of limited on a pHAT of course because most letters don't
fit on the small display of 4x8.
""")

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()

TXT = "HELLO"

figletText = figlet_format(TXT+' ', "banner", width=1000) # banner font generates text with heigth 7
textMatrix = figletText.split("\n")[:width] # width should be 8 on both HAT and pHAT!
textWidth = len(textMatrix[0]) # the total length of the result from figlet
i = -1

def step():
    global i
    i = 0 if i>=100*textWidth else i+1 # avoid overflow
    for h in range(height):
        for w in range(width):
            hPos = (i+h) % textWidth
            chr = textMatrix[w][hPos]
            if chr == ' ':
                unicorn.set_pixel(width-w-1, h, 0, 0, 0)
            else:
                unicorn.set_pixel(width-w-1, h, 255, 0, 0)
    unicorn.show()

while True:
    step()
    sleep(0.2)
