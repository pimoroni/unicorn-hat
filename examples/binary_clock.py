#!/usr/bin/env python
from __future__ import print_function
import unicornhat
import datetime
from time import sleep

print("""True Binary Clock made by Jarrod Price, inspired by Iorga Dragos Florian and reviewed by Philip Howard
Displays the time on the LEDs as follows:
Top row ->  First 4 = Month(Pink), Last 4 = Day(Blue)
Second row ->  First 2 = Alarm(Orange), Last 6 = Hour(Red)
Third row -> First 2 = Alarm(Orange), Last 6 = Minute(Yellow)
Fourth row ->  First 2 = Alarm(Orange), Last 6 = Second(Green)""")

unicornhat.set_layout(unicornhat.AUTO)
# default brightness does not need to be too bright
unicornhat.brightness(0.5)
# get the width of the hat because the LEDs are displayed from the righ to the left
width, height = unicornhat.get_shape()
right_most_pixel = width - 1

# colour tuples
red = (255, 0, 0)
orange = (255, 127, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 127, 255)
lightblue = (100, 200, 255)
magenta = (255, 0, 255)
white = (255, 255, 255)

# alarm must be 24 hour format
alarm_time = '07:00'
# how many minutes should the alarm flash for
alarm_flash_time = 5
# inform the world what time the alarm will go off
print('Alarm set for: ', alarm_time)


def draw_time_string(time_string, length, offset, row, colour):
    """Draw the binary time on a specified row in a certain colour.

    :param time_string: string containing time value that will be used for the bit comparison
    :param length: width of the binary string once converted, e.g. 5 bits for day, 6 bits for hour and minute
    :param offset: left offset - all values are displayed with right alignment as conventional binary dictates, the offest will move it to the left
    :param row: row on which to display the time, this is the y-axis
    :param colour: colour to draw in

    """
    # convert the time string to an integer
    value = int(time_string)
    # loop through the pixels from the right to the left
    for i in range(right_most_pixel, right_most_pixel - length, -1):
        # use the & operator to do a bit comparison
        # for example:
        # 1 & 1 = 1 (ie: 0b1 & 0b1 = 0b1)
        # 2 & 1 = 0 (ie: 0b10 & 0b01 = 0b00)
        if value & 1:
            rgb = colour
        else:
            rgb = (0, 0, 0)
        # determine where on the row it should display this LED
        # either at the given location in the loop or shifted over to the left a little
        column = (i - offset)
        # set the pixels colour
        unicornhat.set_pixel(column, row, rgb)
        # use a binary shift to move all the values over to the right
        # for example:
        # 10 = 0b1010 shifted by 1 place becomes 0b0101 = 5
        # 5 = 0b101 shifted by place becomes 0b010 = 2
        value >>= 1


# this function will make use of the remaining space to light up when indicated
def alarm(t, c):
    # by default we will assume the alarm will not be triggered so keep the default states of the brightness and LED colours
    unicornhat.brightness(0.5)
    b = '0'
    # grab the hour and minute from the set alarm time
    h = int(alarm_time[:2])
    m = int(alarm_time[3:])
    s = 0
    # create time slot for alarm for today
    at = t.replace(hour=h, minute=m, second=s)
    # create a new time object by adding x minutes to the alarm time
    ft = at + datetime.timedelta(minutes=alarm_flash_time)
    # now check if it's time to flash the alarm or not, by checking if we have passed the time it is meant to go off or 5 minutes have not gone passed
    if t >= at and t < ft:
        # signal the alarm!
        # set the brightness to max
        unicornhat.brightness(1)
        # this will make it flash ON when a second is equal and OFF when it is odd
        if int(t.second % 2) == 0:
            # when converted to binary becomes 0b11, so this will turn ON 2 LEDs per row
            b = '3'
    # always update the pixels, the logic above will decide if it displays or not
    # 3 rows, 2 LEDs wide for the alarm, padded to left by 6
    draw_time_string(b, 2, 6, 1, c)
    draw_time_string(b, 2, 6, 2, c)
    draw_time_string(b, 2, 6, 3, c)


# this is the main function, will get the current time and display each time and check the alarm
def binary_clock():
    try:
        while True:
            now = datetime.datetime.now()

            # draw each time string in their specific locations
            draw_time_string(now.month, 4, 4, 0, magenta)
            draw_time_string(now.day >> 1, 4, 0, 0, lightblue if now.day & 16 else blue)
            draw_time_string(now.hour, 6, 0, 1, red)
            draw_time_string(now.minute, 6, 0, 2, yellow)
            draw_time_string(now.second, 6, 0, 3, green)

            # check if the alarm needs to be signalled or not
            alarm(now, orange)

            # we've now set all the LEDs, time to show the world our glory!
            unicornhat.show()

            # sleep for 1 second, because we don't want to waste unnecessary CPU
            sleep(1)

    except Exception as e:
        print(e)

    print("Exiting")


if __name__ == "__main__":
    binary_clock()
