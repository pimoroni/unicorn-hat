#!/usr/bin/env python

import colorsys
import math
import time
from random import randint

import unicornhat as unicorn


print("""Unicorn HAT: Candle

This example simulates a flickering candle flame.

Press Ctrl+C to exit!

""")

unicorn.rotation(180) # 180 is correct when powercord is at top of RPi

unicorn.brightness(0.5)
# brightness of 0.2 is too low b/c the top dim part of the flame doesn't show up
# 0.26 to 0.31 shape of flame OK, nice low warm color, but no constrast b/t light and dark parts
# 0.32 to 0.5 works very well, looks normal

width, height = unicorn.get_shape()

# buffer to contain candle "heat" data
candle = [0] * 256

# create a palette for mapping heat values onto colours
palette = [0] * 256
for i in range(0, 256):
    h = i / 5.0
    h /= 360.0
    s = (1.0 / (math.sqrt(i / 50.0) + 0.01))
    s = min(1.0, s)
    s = max(0.0, s)

    v = i / 200.0
    if i < 60:
        v = v / 2
    v = min(1.0, v)
    v = max(0.0, v)

    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    palette[i] = (int(r * 255.0), int(g * 255.0), int(b * 255.0))


def set_pixel(b, x, y, v):
    b[y * 16 + x] = int(v)                   # edited 16 to 8


def get_pixel(b, x, y):
    # out of range sample lookup
    if x < 0 or y < 0 or x >= 16 or y >= 16:  # edited 16 to 8
        return 0

    # subpixel sample lookup
    if isinstance(x, float) and x < 7:      # edited 15 to 7
        f = x - int(x)
        return (b[int(y) * 16 + int(x)] * (1.0 - f)) + (b[int(y) * 16 + int(x) + 1] * (f)) # edited 16 to 8

    # fixed pixel sample lookup
    return b[int(y) * 16 + int(x)]          # edited 16 to 8


step = 0

try:
    while True:
	# step for waving animation, adds some randomness
        step += randint(0, 15)

        # clone the current candle
        temp = candle[:]

        # seed new heat
        v = 500

        set_pixel(candle, 1, 7, v)  # Converting from unicornhatHD, subtracted 8 from these
        set_pixel(candle, 2, 7, v)  # since unicornhat is half the size.
        set_pixel(candle, 3, 7, v)  # candle is a list, and 2 numbers are used to
        set_pixel(candle, 4, 7, v)  # calculate a position in list
        set_pixel(candle, 1, 6, v)  # that will be assigned integer value v
        set_pixel(candle, 2, 6, v)
        set_pixel(candle, 3, 6, v)
        set_pixel(candle, 4, 6, v)

        # blur, wave, and shift up one step
        # v is changed then a pixel is set, 8x8 times, then all assigned to candle

        for x in range(0, 8):
            for y in range(0, 8): # 8x8 is 64, length of list candle, and size of unicornhat
                s = math.sin((y / 30.0) + (step / 10.0)) * ((16 - y) / 20.0)
                v = 0
                for i in range(0, 3):          # range seems to scale height of low bright part of flame
                    for j in range(0, 3):      # range seems to scale height of top dim part of flame
                        r = randint(0, 2) - 1  # provides some slight color variations
                        v += get_pixel(candle, x + i + s - 1, y + j)

                v /= 12
                # denominator scales the size of flame, so larger number-->smaller flame
                # 11 is too tall, the top of the flame is clipped off
                # 12 fills the unicornhat perfectly
                # 16 is about 5 pixels high, and five pixels wide, barely ok
                # 20 is too small at about 3 pixels high, seems like all one color

                set_pixel(temp, x, y, v)
            time.sleep(.003)  # adjusts how fast the flame dances around

        candle = temp

        # copy candle into unicornhat with palette
        # from unicornhatHD, adjusted to 8x8 values of candle, convert from hsv to rbg
        # and painted onto unicornhat
        for x in range(0, 8):
            for y in range(0, 8):
                o = (i * 3) + 1
                r, g, b = palette[max(0, min(255, get_pixel(candle, x, y)))]
                unicorn.set_pixel(x, y, r, g, b)
        unicorn.show()

except KeyboardInterrupt:
    unicorn.off()
