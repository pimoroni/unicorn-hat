from random import randint
import unicornhat as unicorn
from time import sleep

width = 8
height = 8
rows = []
row_pointer = 0

unicorn.brightness(0.2)


def init():
    for i in range(height):
        rows.append(get_blank_row())


def get_blank_row():
    return [0] * width


def get_new_row():
    row = get_blank_row()
    row[randint(0, width - 1)] = 50 + randint(0, 155)
    return row


def update_display():
    c = row_pointer
    for h in range(height):
        for w in range(width):
            val = rows[c][w]
            unicorn.set_pixel((width - 1) - w, (height - 1) - h, val, val, val)
        c += 1
        if c > height - 1:
            c = 0
    unicorn.show()


def step():
    global row_pointer
    rows[row_pointer] = get_new_row()
    update_display()
    row_pointer -= 1
    if row_pointer < 0:
        row_pointer = height - 1


init()
while True:
    step()
    sleep(0.3)
