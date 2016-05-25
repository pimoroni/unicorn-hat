#!/usr/bin/env python

import unicornhat as uh
import time
from random import randint

uh.set_layout(uh.AUTO)
uh_width,uh_height=uh.get_shape()
uh.rotation(0)
heights = []


def setup():

    global heights
    heights = []
    for b in range(0, (uh_width-2)):
        heights.append(0)
    uh.off()
    for b in range(0, uh_height):
#        uh.set_pixel(0, b, 255, 127, 127)
        uh.set_pixel(0, b, 255, 255, 255)
    for b in range(0, uh_height):
#        uh.set_pixel((uh_width-1), b, 127, 255, 127)
        uh.set_pixel((uh_width-1), b, 255, 255, 255)
    for b in range(1, (uh_width-1)):
#        uh.set_pixel(b, 0, 255, 255, 255)
        uh.set_pixel(b, 0, 127, 127, 255)
    uh.show()


def drop_ball():

    ball_colour = [randint(100, 255), randint(100, 255), randint(100, 255)]
    ball_column = randint(0, (uh_width-3))

    while heights[ball_column] == (uh_height-1):
        ball_column = randint(0, (uh_width-3))
    height = heights[ball_column]
    ball_y = (uh_height-1)
    uh.set_pixel(ball_column + 1, ball_y, ball_colour[0], ball_colour[1], ball_colour[2])
    uh.show()
    dropcount = (uh_height-2) - height
    for y in range(0, dropcount):
        uh.set_pixel(ball_column + 1, ball_y, 0, 0, 0)
        ball_y -= 1
        uh.set_pixel(ball_column + 1, ball_y, ball_colour[0], ball_colour[1], ball_colour[2])
        uh.show()
        time.sleep(0.02)
    heights[ball_column] += 1


setup()
while True:
    for i in range(0, (uh_width-2)*(uh_height-1)):
        drop_ball()
    time.sleep(1)
    setup()

