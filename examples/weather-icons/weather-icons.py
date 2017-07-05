#!/usr/bin/env python

# The MIT License (MIT)
#
# Copyright (c) 2016 LoveBootCaptain
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# *************************************************************
# animated weather icons for the unicorn-hat by LovebootCaptain
# *************************************************************
#
# The icons in the /icons folder are made of 8-16 individual 8x8 images combined to a sprite.
#
# draw_animation(image) is same as in the 'show-png' example but put into a tiny little function.
# Put in your image object and you're done. The function will loop through all images in the sprite
# and it will look like a tiny animation. Awesome !!
#
# You can change the 'fps' with changing the 'cycle_time' variable (0.25 is very smooth)
#
# loop() finally loops through all png images in a folder (you might guessed it) so you can see all possibilities.
#
# usage:
#
# 'weather-icons.py loop' for all animations or images
#
# 'weather-icons.py clear-day.png' for a single animation or image

import os
import time
from sys import exit, argv

try:
    from PIL import Image
except ImportError:
    exit('This script requires the pillow module\nInstall with: sudo pip install pillow')

import unicornhat as unicorn

print('''
    *************************************************************
    animated weather icons for the unicorn-hat by LovebootCaptain
    *************************************************************
    ''')

unicorn.brightness(1)
unicorn.rotation(0)

folder_path = 'icons/'

icon_extension = '.png'

width, height = unicorn.get_shape()

cycle_time = 0.25


def helper():
    print('''
    Usage:
    python weather-icons.py options
    
    options:
    loop
    image-file.png

    example:
    weather-icons.py loop
    weather-icons.py clear-day.png
    
    try one of the files from this list: 
    {}
    '''.format(", ".join(os.listdir(folder_path))))


def draw_animation(image):
    # this is the original pimoroni function for drawing sprites
    try:

        for o_x in range(int(image.size[0] / width)):

            for o_y in range(int(image.size[1] / height)):

                valid = False

                for x in range(width):

                    for y in range(height):
                        pixel = image.getpixel(((o_x * width) + y, (o_y * height) + x))
                        r, g, b = int(pixel[0]), int(pixel[1]), int(pixel[2])
                        if r or g or b:
                            valid = True
                        unicorn.set_pixel(x, y, r, g, b)

                if valid:
                    unicorn.show()
                    time.sleep(cycle_time)

    except KeyboardInterrupt:
        unicorn.off()


def loop():

    print('Looping through all images in folder {}\n'
          'CRL+C to skip image'.format(folder_path))

    try:

        for img_file in os.listdir(folder_path):

            if img_file.endswith(icon_extension):

                print('Drawing image: {}'.format(folder_path + img_file))

                img = Image.open(folder_path + img_file)

                draw_animation(img)

            else:

                print('Not using this file, might be not an image: {}'.format(img_file))

    except KeyboardInterrupt:
        unicorn.off()

    unicorn.off()


def weather_icons():
    try:

        if argv[1] == 'loop':

            loop()

        elif argv[1] in os.listdir(folder_path):

            print('Drawing Image: {}'.format(argv[1]))

            img = Image.open(folder_path + argv[1])

            draw_animation(img)
            unicorn.off()

        else:
            helper()

    except IndexError:
        helper()


if __name__ == '__main__':
    weather_icons()
