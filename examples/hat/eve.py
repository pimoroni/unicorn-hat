#!/usr/bin/env python

import colorsys
import math
import random
import time
from sys import exit

try:
    import glib
except ImportError:
    exit("This script requires the glib module")

try:
    import gudev
except ImportError:
    exit("This script requires the gudev module")

import unicornhat as unicorn


unicorn.set_layout(unicorn.HAT)
unicorn.rotation(0)
unicorn.brightness(0.5)

sin_off = [[0]*8 for i in range(8)]
for y in range(8):
    for x in range(8):
        sin_off[x][y] = random.random() * (math.pi * 2)

tick_mask = [[0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,1,0],
             [0,0,0,0,0,1,1,1],
             [0,0,1,0,1,1,1,0],
             [0,1,1,1,1,1,0,0],
             [0,0,1,1,1,0,0,0],
             [0,0,0,1,0,0,0,0],
             [0,0,0,0,0,0,0,0]]

steps_per = 16
def background(x, y, step):
    v = math.sin(sin_off[x][y] + (step / 10.0))

    g = v + 1.0
    g = g * 20.0
    g += 20

    v = math.sin(sin_off[y][x] + (step / 20.0))

    b = v + 1.0
    b = b * 15.0
    b += 20

    r = 0

    g /= (r/50) + 1
    b /= (r/50) + 1

    pos = int(step / steps_per)
    fill = int((float(step % steps_per) / float(steps_per)) * 8.0)

    if x < pos:
        r = math.sin(sin_off[y][x] + (step / 20.0))
        r *= 30
        r += 80
        g = 0
        b = 0
    elif x == pos and y < fill:
        r = math.sin(sin_off[y][x] + (step / 20.0))
        r *= 30
        r += 80
        g = 0
        b = 0

    return (g, r, b)

def effect():
    # trigger effect
    for i in range(steps_per * 8):
        for y in range(8):
            for x in range(8):
                r, g, b = background(x, y, i)
                r = int(max(0, min(255, r)))
                g = int(max(0, min(255, g)))
                b = int(max(0, min(255, b)))
                unicorn.set_pixel(x, y, r, g, b)

        unicorn.show()

        time.sleep(0.01)

    for i in range(200):
        v = (math.sin(i / 6.0) + 1.0) / 2.0
        for y in range(8):
            for x in range(8):
                r = 0
                b = 0
                g = 100
                g *= tick_mask[y][x]
                g *= v
                r = int(max(0, min(255, r)))
                g = int(max(0, min(255, g)))
                b = int(max(0, min(255, b)))
                unicorn.set_pixel(x, y, r, g, b)

        unicorn.show()

        time.sleep(0.02)

def clear():
    for y in range(8):
        for x in range(8):
            unicorn.set_pixel(x, y, 0, 0, 0)

    unicorn.show()

def callback(client, action, device, user_data):
    if action == "add":
        effect()

    if action == "remove":
        clear()


client = gudev.Client(["usb/usb_device"])
client.connect("uevent", callback, None)

loop = glib.MainLoop()
loop.run()
