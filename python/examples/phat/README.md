Unicorn pHAT optimised Examples
===============================

The Unicorn pHAT is using the Raspberry Pi's GPIO pins in a direct way, all of these examples must be run with root priviledge that can be archived using `sudo`, for example

    sudo ./phat_demo.py

or

    sudo python phat_demo.py    


Note: All the example in this folder are specifically written for the Unicorn pHAT, they implicitly know about it's topology and use the folowing code to initialise the library:

```python
import unicornhat
unicornhat.set_layout(unicornhat.PHAT)
```

pHAT optimised examples is a temporary solution waiting for unification of HAT and pHAT example. This is a work in progress.

phat_demo.py
------------

Multi-effect demo;  twisty swirly goodness, roto-zooming checker board, weeee waaaah, rainbow search spotlights and zoom tunnel

This example display the 4 middle lines of the full fledge Unicorn HAT.


phat_rainbow_blinky.py
----------------------

Blinks a rainbow spot light on and off. Change `fwhm` to make the spot more/less focused (smaller numbers = more focused/larger numbers = less focused).


phat_random_blinky.py
---------------------

Blinks random yellow-orange-red LEDs.


phat_random_sparkles.py
-----------------------

Random multi-coloured sparkles.


phat_cross.py
-------------

Random horizontal and vertical moving pixels.


phat_drop.py
------------

Random Tetris like filling of the screen with falling pixels.


phat_snow.py
------------

Pixels falling like snowflakes.


