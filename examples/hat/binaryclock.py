#!/usr/bin/env python
import unicornhat as uh
import datetime
from time import sleep

print("""Binar Clock made by Iorga Dragos Florian
Displays Hour(red), Minute(yellow), Second(blue), Day(green) and Month(Pink) in binary format""")
FPS = 30.0
uh.rotation(0)
uh.brightness(1)

def draw_time(b,x,idx,color):
    if b == '1':
        uh.set_pixel(x,idx,color)
    sleep(1.0/FPS)

while True:
    now = datetime.datetime.now()
    month = bin(now.month)[2:][::-1]
    day = bin(now.day)[2:][::-1]
    hour = bin(now.hour)[2:][::-1]
    minute = bin(now.minute)[2:][::-1]
    second = bin(now.second)[2:][::-1]
    uh.clear()
    for idx,b in enumerate(hour):
        draw_time(b,7,idx,'red')

    for idx,b in enumerate(minute):
        draw_time(b,6,idx,'yellow')

    for idx,b in enumerate(second):
        draw_time(b,5,idx,'blue')

    for idx,b in enumerate(day):
        draw_time(b,3,idx,'green')

    for idx,b in enumerate(month):
        draw_time(b,2,idx,'purple')
    uh.show()
