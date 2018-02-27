import unicornhat as uh
import datetime

uh.rotation(0)
uh.brightness(1)

def draw_time(b,x,idx,color):
    if b == '1':
        uh.set_pixel(x,idx,color)


while True:
    now = datetime.datetime.now()
    an = bin(now.month)[2:][::-1]
    luna = bin(now.month)[2:][::-1]
    zi = bin(now.day)[2:][::-1]
    ora = bin(now.hour)[2:][::-1]
    minut = bin(now.minute)[2:][::-1]
    secunda = bin(now.second)[2:][::-1]
    uh.clear()
    for idx,b in enumerate(ora):
        draw_time(b,7,idx,'red')

    for idx,b in enumerate(minut):
        draw_time(b,6,idx,'yellow')

    for idx,b in enumerate(secunda):
        draw_time(b,5,idx,'blue')

    for idx,b in enumerate(zi):
        draw_time(b,3,idx,'green')

    for idx,b in enumerate(luna):
        draw_time(b,2,idx,'purple')
    uh.show()
