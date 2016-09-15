#!/usr/bin/env python
#import necessary modules
import unicornhat as unicorn
from time import sleep
from random import randint
#setup the unicorn hat
unicorn.set_layout(unicorn.PHAT)
unicorn.brightness(0.5)

def print_header():
        #print the program's description
        print("Unicorn PHat Toggle LEDs with input!")
        sleep(.5)
        #give instructions on how to operate
        print("Press <enter> to toggle or <ctrl> + <c> to quit")
        sleep(.5)

def toggle(tog):
        #toggle has been called determine state
        if tog:
                r = randint(30, 255)
                g = randint(30, 255)
                b = randint(30, 255)
                msg="On!"
        else:
                r=0
                g=0
                b=0
                msg="Off!"
        #print the relevant message
        print(msg,r,g,b)
        #set the LEDs to the relevant lighting (all on/off)
        for y in range(4):
                for x in range(8):
                        unicorn.set_pixel(x,y,r,g,b)
                        unicorn.show()
        #return the inverse boolean variable that was passed in
        return not tog

if __name__ == "__main__":
        #program starts here
        print_header()
        #this is the starting state (True=ON)
        bToggle = True
        #indefinite loop
        while True:
                #call the toggle function with a given state and it will return the inverse
                bToggle = toggle(bToggle)
                #pause and await input from keyboard i.e. <enter> no characters are checked
                raw_input("")
