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
#inform the world what time the alarm will go off
print('Alarm set for: ', alarm_time)

#This function will draw the binary time at a specified location and colour
#t = time value which will be converted to binary
#l = length of the binary string once converted, e.g. day will not go past 31 so only needs 4 bits not like minutes or seconds which need 6 bits
#o = offset, all values are displayed with right alignment as conventional binary dictates, the offest will move it to the left
#y = this is the y-axis, i.e. what row you want it displayed on
#c = colour you want the binary to display as
def draw_time_string(t,l,o,y,c):
    #convert the time value to binary
    t = bin(int(t))[2:]
    #pad the binary with zeroes to left to the specified length
    t = '{:0>{}}'.format(t,l)
    #loop through each bit 
    for i in range(0,len(t)):
        #grab the actual binary value
        v = t[i]
        #if it's 1 then the LED should be ON otherwise it will be OFF, i.e. display the colour specified or else it will be black
        if v == '1':
            rgb = c
        else:
            rgb = (0,0,0)
        #determine where on the row it should display this LED
        x = (width - l - o) + i
        #set the pixel... duh!
        uh.set_pixel(x,y,rgb)

#make use of the remaining space to be used an alarm
def alarm(t,c):
    #by default we will assume the alarm will not be triggered so keep the default states of the brightness and LED colours
    uh.brightness(0.5)
    b = '0'
    #grab the hour and minute from the set alarm time
    h = int(alarm_time[:2])
    m = int(alarm_time[3:])
    #now check if it's time to flash the alarm or not
    if t.hour == h:
        if t.minute == m:
            #it's on the hour and on the minute, time to signal the alarm!
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
    except:
        print("Exiting")

if __name__ == "__main__":
    binary_clock()
