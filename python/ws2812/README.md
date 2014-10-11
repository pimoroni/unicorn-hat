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

Changes
-------

Please do not modify ws2812-RPi_wrap.c or ws2812.py directly.

You should change only the bindings file: ws2812-RPi.i

Changes to this file will let you use SWIG to auto-generate the correct bindings:

   swig2.0 -python ws2812-RPi.i

If you wish to add any Python methods for a specific product or application, then it's
recommended that you create a separate module ( like UnicornHat ).