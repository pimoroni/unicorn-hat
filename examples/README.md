Unified Unicorn HAT and pHAT Examples
======================================

The examples in this folder must be run with `sudo`, like so:

    sudo ./clock.py

or

    sudo python clock.py


The library can detect if you're using a Unicorn HAT or a Unicorn pHAT.
The recommended initialisation is as folows:

```python
import unicornhat as unicorn
unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.4)
width,height=unicorn.get_shape()
```

Explicitly setting the rotation to 0 lets users of your code adapt it to their orientation. Forcing the brightness to 0.4 is for safety. Always use the get_shape() call after having decided on the rotation. If your code uses width and height properly, it should adapt to current and future geometry.

Note: If you're only using a Unicorn pHAT you may want to specify it in your code, like so:

```python
import unicornhat as unicorn
unicorn.set_layout(unicorn.PHAT)
```

Most examples work with both Unicorn HAT and pHAT, using autodetect. Examples that have not been adapted for the pHAT reside in hat folder. Similarly, examples that were specifically designed for the pHAT reside in the phat folder.


detect.py
---------

Demo code to verify if the auto detection code properly identifies if you have a unicorn HAT or a unicorn pHAT. The code assumes that if height == width then you must have a HAT.

IMPORTANT: for the auto detection process to work, Unicorn HAT must be fitted onto the GPIO at boot time. If that was not the case, the auto detection will default to the pHAT layout of 8x4!


bluesky_greengrass.py
---------------------

Example code to verify the rotation of the screen. The sky (top) should be blue and the grass (bottom) should be green.
If you can not re-orientate the screen, use unicorn.rotation(90) or 180 or 270 until you get blue and green in the expected location.


demo.py
-------

Multi-effect demo;  twisty swirly goodness, roto-zooming checker board, weeee waaaah, rainbow search spotlights and zoom tunnel.


simple.py
---------

Sets each pixel in turn and updates the display.


rainbow.py
----------

Demonstrates the use of `colorsys` to animate through colour hues.


rainbow_blinky.py
-----------------

Blinks a rainbow spot light on and off. Change `fwhm` to make the spot more/less focused (smaller numbers = more focused/larger numbers = less focused).


random_blinky.py
----------------

Blinks random yellow-orange-red LEDs.


random_sparkles.py
------------------

Random multi-coloured sparkles.


drop.py
-------

Tetris like filling of a board with random color falling pixels.


drop_four_orientation.py
------------------------

Tetris like filling of a board with random color falling pixels. The demo show the 4 rotation in loop.


cross.py
--------

Crossing random multi-color pixels in the 4 directions.


snow.py
-------

Falling snowflake pixels.



