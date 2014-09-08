ws2812 Python Module
====================

Usage
-----

Install with:

    sudo ./setup.py install

Then:

    import ws2812
    numPixels = 64
    ws2812.init(64)
    idx = 0
    r = 255
    g = 0
    b  = 255
    ws2812.setPixelColor(idx, r, g, b)
    ws2812.show()

Reference
---------

* init(numPixels) - Initialise the hardware and set the number of pixels to update

* clear() - Clear the LED buffer
* setPixelColor(index, r, g, b) - Change the colour of a single LED
* setPixelColor(index, color) - Same as above, using color object
* show() - Update the LEDs with current buffer

* Color(r, g, b) - Create an instance of color, for use with setPixelColor, theaterChase, etc.

* Wheel(0 - 255) - From Adafruit ws2812 demos, gets an RGB colour
* rainbow(wait) - Animates a rainbow across pixels, delay of "wait"
* rainbowCycle(wait) - Same as above, with a slightly different animation
* theaterChase(color, wait) - Animate a colour across pixels

* terminate(0) - Should ideally be called upon exiting to clean up hardware

leds utility
------------

Requires libpng, compile with:

    make


RaspberryPi-NeoPixel-WS2812
===========================

Library for driving WS2812 pixels (also known as "NeoPixels" when sold by Adafruit) from a Raspberry Pi.

Wishlist:
* Modify DMA code so it can use more than one 4K page, enabling >450 pixels (some people have thousands!)
* Turn this into a FIFO daemon, like ServoBlaster
* There are a few stupid magic numbers left that I haven't changed to DEFINEs yet
* Make it immediately return after initiating DMA transfer, so we can begin building the next frame (for higher framerate on huge lengths of pixels)

Done:
* Add whatever functions are present in the Adafruit Arduino library, but not implemented here
* Change calculated delay after DMA transfer start to reflect number of pixel commands sent (plus one word, to ensure low latch signal is sent) rather than the length of the entire buffer
* Fix high CPU usage
