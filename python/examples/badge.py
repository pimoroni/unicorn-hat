#!/usr/bin/env python

import unicornhat as unicorn
import time, math, colorsys

# twisty swirly goodness
def swirl(x, y, step):
    x -= 4
    y -= 4

    dist = math.sqrt(pow(x, 2)+pow(y,2)) / 2.0
    angle = (step / 10.0) + (dist * 1.5)
    s = math.sin(angle);
    c = math.cos(angle);    
    
    xs = x * c - y * s;
    ys = x * s + y * c;

    r = abs(xs + ys)
    r = r * 64.0
    r -= 20

    return (r, r, r)

# roto-zooming checker board
def checker(x, y, step):
    x -= 4
    y -= 4

    angle = (step / 10.0)
    s = math.sin(angle);
    c = math.cos(angle);    
    
    xs = x * c - y * s;
    ys = x * s + y * c;

    xs -= math.sin(step / 200.0) * 40.0
    ys -= math.cos(step / 200.0) * 40.0

    scale = step % 20
    scale /= 20
    scale = (math.sin(step / 50.0) / 8.0) + 0.25;

    xs *= scale
    ys *= scale

    xo = abs(xs) - int(abs(xs))
    yo = abs(ys) - int(abs(ys))
    l = 0 if (math.floor(xs) + math.floor(ys)) % 2 else 1 if xo > .1 and yo > .1 else .5

    r, g, b = colorsys.hsv_to_rgb((step % 255) / 255.0, 1, l)

    return (r * 255, g * 255, b * 255)

# weeee waaaah
def blues_and_twos(x, y, step):
    x -= 4
    y -= 4

    xs = (math.sin((x + step) / 10.0) / 2.0) + 1.0
    ys = (math.cos((y + step) / 10.0) / 2.0) + 1.0

    scale = math.sin(step / 6.0) / 1.5
    r = math.sin((x * scale) / 1.0) + math.cos((y * scale) / 1.0)
    b = math.sin(x * scale / 2.0) + math.cos(y * scale / 2.0)
    g = r - .8
    g = 0 if g < 0 else g
    
    b -= r
    b /= 1.4

    return (r * 255, (b + g) * 255, g * 255)

# rainbow search spotlights
def rainbow_search(x, y, step):
    xs = math.sin((step) / 100.0) * 20.0
    ys = math.cos((step) / 100.0) * 20.0

    scale = ((math.sin(step / 60.0) + 1.0) / 5.0) + 0.2
    r = math.sin((x + xs) * scale) + math.cos((y + xs) * scale)
    g = math.sin((x + xs) * scale) + math.cos((y + ys) * scale)
    b = math.sin((x + ys) * scale) + math.cos((y + ys) * scale)

    return (r * 255, g * 255, b * 255)

effects = [rainbow_search, swirl, checker]

unicorn.brightness(0.05)

step = 0
while True:
    for i in range(200):
        for y in range(8):
            for x in range(8):              
                r, g, b = effects[0](x, y, step)
                if i > 150:
                    r2, g2, b2 = effects[-1](x, y, step)

                    ratio = (200.00 - i) / 50.0
                    r = r * ratio + r2 * (1.0 - ratio)
                    g = g * ratio + g2 * (1.0 - ratio)
                    b = b * ratio + b2 * (1.0 - ratio)
                r = int(max(0, min(255, r)))
                g = int(max(0, min(255, g)))
                b = int(max(0, min(255, b)))
                unicorn.set_pixel(x, y, r, g, b)

        step += 1
        print step
        unicorn.show()

    effect = effects.pop()
    effects.insert(0, effect)
    time.sleep(0.01)
