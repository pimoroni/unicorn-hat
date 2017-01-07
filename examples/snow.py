#!/usr/bin/env python

from random import randint
from time import sleep

import unicornhat as unicorn

print("""Snow

Draws random white pixels to look like a snowstorm.

If you're using a Unicorn HAT and only half the screen lights up, 
edit this example and  change 'unicorn.AUTO' to 'unicorn.HAT' below.
""")

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()


rows = []
row_pointer = 0


def init():

    # create a buffer of <height> blank rows
    for i in range(height):
        rows.append(get_blank_row())


def get_blank_row():

    # generate a blank row
    return [0] * width


def get_new_row():

    # get a new blank row and add a random brightness snowflake to a random column
    row = get_blank_row()
    row[randint(0, width - 1)] = 50 + randint(0, 155)
    return row


def update_display():

    # keep track of the row we are updating
    c = row_pointer
    for h in range(height):
        for w in range(width):
            # val is between 50 and 255
            val = rows[c][w]

            # invert coordinates
            unicorn.set_pixel((width - 1) - w, (height - 1) - h, val, val, val)
        c += 1
        if c > height - 1:
            c = 0
    unicorn.show()


def step():
    global row_pointer

    # add new row at current row pointer
    # leave other rows the same, display will start from this one which overwrites the
    # oldest existing row from the last time we updated the display
    rows[row_pointer] = get_new_row()
    update_display()

    # determine next row pointer, wrapping around if we went past zero
    row_pointer -= 1
    if row_pointer < 0:
        row_pointer = height - 1


init()
while True:
    step()
    sleep(0.3)
