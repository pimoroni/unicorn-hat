#!/usr/bin/env python
from __future__ import print_function
import unicornhat as uh
import datetime
from time import sleep

print("""True Binary Clock made by Iorga Dragos Florian and Jarrod Price
Displays the following:
Top row ->  First 4 = Month(Pink), Last 4 = Day(Blue)
Second row ->  First 2 = Alarm(Orange), Last 6 = Hour(Red)
Third row -> First 2 = Alarm(Orange), Last 6 = Minute(Yellow)
Fourth row ->  First 2 = Alarm(Orange), Last 6 = Second(Green)""")
uh.set_layout(uh.AUTO)
#default brightness does not need to be too bright
uh.brightness(0.5)
#we need the width of the hat for the padding, see below
width, height = uh.get_shape()
right_most_pixel=width-1

#colour tuples 
red = (255,0,0)
orange = (255,127,0)
yellow = (255,255,0)
green = (0,255,0)
blue = (0,127,255)
magenta = (255,0,255)
white = (255,255,255)

#alarm must be 24 hour format
alarm_time = '07:00'
alarm_flash_time=5
#inform the world what time the alarm will go off
print('Alarm set for: ', alarm_time)

#This function will draw the binary time at a specified location and colour
#time_string, containing time value which will be used for the bit comparison
#length, .i.e. width of the binary string once converted, e.g. day will not go past 31 so only needs 4 bits not like minutes or seconds which need 6 bits
#offset, all values are displayed with right alignment as conventional binary dictates, the offest will move it to the left
#row you want the time to be displayed on, this is the y-axis
#colour, you want the binary to display as
def draw_time_string(time_string,length,offset,row,colour):
    #convert the time value to binary
    value = int(time_string)
    #loop through the given width of the binary time 
    # Our value will be a number <= 59
    # It takes 6 binary digits (bits) to represent all possible values
    # For example: 17 minutes = 0b10001
    # If we step through these binary digits from right to left,
    # this results in the first and fifth pixels being lit.
    for i in range(right_most_pixel,right_most_pixel-length,-1):
        # The & operator gives us a result containing all the bits that
        # are set in both values, for example:
        #
        # 1 & 1 = 1 (ie: 0b1 & 0b1 = 0b1)
        # 2 & 1 = 0 (ie: 0b10 & 0b01 = 0b00)
        # 7 & 27 = 3 (ie: 0b00111 & 0b11011 = 0b00011
        if value & 1:
            rgb = colour
        else:
            rgb = (0,0,0)
        #determine where on the row it should display this LED
        column = (i - offset) 
        #set the pixel... duh!
        uh.set_pixel(column,row,rgb)
        value >>= 1

#make use of the remaining space to be used an alarm
def alarm(t,c):
    #by default we will assume the alarm will not be triggered so keep the default states of the brightness and LED colours
    uh.brightness(0.5)
    b = '0'
    #grab the hour and minute from the set alarm time
    h = int(alarm_time[:2])
    m = int(alarm_time[3:])
    s = 0
    #create time slot for alarm for today
    at = t.replace(hour=h,minute=m,second=s)
    #create a new time object by adding x minutes to the alarm time
    ft = at + datetime.timedelta(minutes=alarm_flash_time)
    #now check if it's time to flash the alarm or not, by checking if we have passed the time it is meant to go off or 5 minutes have not gone passed
    if t >= at and t < ft:
        #signal the alarm!
        uh.brightness(1)
        #this will make it flash ON when a second is equal and OFF when it is odd
        if int(t.second % 2) == 0:
            #when converted to binary 3 = '11', so this will turn ON 2 LEDs per row
            b = '3'
    #always update the pixels, the logic above will decide if it displays or not
    #3 rows, 2 LEDs wide for the alarm
    draw_time_string(b, 2, 6, 1, c)
    draw_time_string(b, 2, 6, 2, c)
    draw_time_string(b, 2, 6, 3, c)



def binary_clock():
    try:
        while True:
            now = datetime.datetime.now()
            #print(now)

            #draw each time string in their specific locations
            draw_time_string(now.month, 4, 4, 0, magenta)
            draw_time_string(now.day, 4,0, 0, blue)
            draw_time_string(now.hour, 6, 0, 1, red)
            draw_time_string(now.minute, 6, 0, 2, yellow)
            draw_time_string(now.second, 6, 0, 3, green)

            #check if the alarm needs to be signalled or not
            alarm(now, orange)

            #we've now set all the LEDs, time to show the world our glory!
            uh.show()

            #sleep for sec, cos we don't want to wast unnecessary CPU
            sleep(1)
    except Exception as e:
        print(e)
    print("Exiting")

if __name__ == "__main__":
    binary_clock()
