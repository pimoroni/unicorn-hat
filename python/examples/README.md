Unicorn HAT Examples
====================

By virture of the Unicorn HAT being a HAT(!), and hence using the Raspberry Pi's GPIO pins, all of these examples must be run with `sudo`, for example

    sudo ./clock.py

or

    sudo python clock.py    


Note: If you're using a Unicorn pHAT make sure you specify in your code, like so:

```python
import unicornhat
unicornhat.set_layout(unicornhat.PHAT)
```

Some pHAT specific version of examples are present in phat folder.


bleusky_greengrass.py
---------------------

Example code to verify the rotation of the screen.
The sky (top) should be blue and the grass (bottom) green.
If you can not orientate the screen, use unicorn.rotation(90) or 180 or 270.


demo.py
-------

Multi-effect demo;  twisty swirly goodness, roto-zooming checker board, weeee waaaah, rainbow search spotlights and zoom tunnel


simple.py
---------

Sets each pixel in turn and updates the display.


detect.py
---------

Demo code to verify if the auto detection code properly identify if you have a unicorn HAT or a unicorn pHAT


rainbow_blinky.py
-----------------

Blinks a rainbow spot light on and off. Change `fwhm` to make the spot more/less focused (smaller numbers = more focused/larger numbers = less focused).


random_blinky.py
----------------

Blinks random yellow-orange-red LEDs.


not documented
==============

cross.py
drop.py
rainbow_blinky.py
random_blinky.py
snow.py


Work in Progress
================

Program likely available in the HAT and maybe pHAT folder.


clock.py
--------

Uses `graphics.py` and shows how you can, but probably shouldn't, display an analogue clock on Unicorn HAT!


random_sparkles.py
------------------

Random multi-coloured sparkles.


unicornpaint/paint.py
---------------------

Use your web browser to pixel paint onto Unicorn HAT.

**Requirements:**

    sudo pip install flask


show_png.py
-----------

Shows how you can open and display a PNG image file, great for sprite animations.

**Requirements:**

    sudo pip install pillow

