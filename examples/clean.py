#!/usr/bin/env python

import unicornhat as unicorn

#setup the unicorn hat
unicorn.set_layout(unicorn.AUTO)

#get the width and height of the hardware
width, height = unicorn.get_shape()

def clean():
    for y in range(height):
        for x in range(width):
            unicorn.set_pixel(x,y,0,0,0)
    unicorn.show()

if __name__ == "__main__":
    clean()
