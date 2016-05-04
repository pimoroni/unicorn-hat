#!/usr/bin/env python

import unicornhat as uh
import time
from random import randint

width = 8
height = 8
points = []


class LightPoint:

    def __init__(self):

        self.direction = randint(1, 4)
        if self.direction == 1:
            self.x = randint(0, width - 1)
            self.y = 0
        elif self.direction == 2:
            self.x = 0
            self.y = randint(0, height - 1)
        elif self.direction == 3:
            self.x = randint(0, width - 1)
            self.y = height - 1
        else:
            self.x = width - 1
            self.y = randint(0, height - 1)

        self.colour = []
        for i in range(0, 3):
            self.colour.append(randint(100, 255))


def update_positions():

    for point in points:
        if point.direction == 1:
            point.y += 1
            if point.y > height - 1:
                points.remove(point)
        elif point.direction == 2:
            point.x += 1
            if point.x > width - 1:
                points.remove(point)
        elif point.direction == 3:
            point.y -= 1
            if point.y < 0:
                points.remove(point)
        else:
            point.x -= 1
            if point.x < 0:
                points.remove(point)


def plot_points():

    uh.clear()
    for point in points:
        uh.set_pixel(point.x, point.y, point.colour[0], point.colour[1], point.colour[2])
    uh.show()


while True:

    if len(points) < 10 and randint(0, 5) > 1:
        points.append(LightPoint())
    plot_points()
    update_positions()
    time.sleep(0.03)

