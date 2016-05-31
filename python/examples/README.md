Unified Unicorn HAT and pHAT Examples
======================================

By virture of the Unicorn HAT being a HAT(!), and hence using the Raspberry Pi's GPIO pins, all of these examples must be run with `sudo`, for example

    sudo ./clock.py

or

    sudo python clock.py    


The library can detect if you're using a Unicorn HAT or a Unicorn pHAT.
The recommended initialisation is the folowing:

```python
unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.4)
width,height=unicorn.get_shape()
```

Explicitly seting the rotation to 0 let user of your code adapt it to their orientation. Forcing the brightness to 0.4 is for safety. Always use get_shape after having decide on the rotation.

If you code use properly width and height, it should adapt to current and futur geometry.


Note: If you're only using a Unicorn pHAT you may want to specify in your code, like so:

```python
import unicornhat as unicorn
unicorn.set_layout(unicorn.PHAT)
```

Most exemple work both on HAT and pHAT using autodetect.
Exemple that have not been adapted for the pHAT reside in hat folder.


detect.py
---------

Demo code to verify if the auto detection code properly identify if you have a unicorn HAT or a unicorn pHAT. The code assume that if height == width then you must have a HAT.


bluesky_greengrass.py
---------------------

Example code to verify the rotation of the screen.
The sky (top) should be blue and the grass (bottom) green.
If you can not orientate the screen, use unicorn.rotation(90) or 180 or 270 until you get blue and green at the expected location.


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



