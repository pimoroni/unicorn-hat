Unicorn HAT Examples
====================

By virture of the Unicorn HAT being a HAT(!), and hence using the Raspberry Pi's GPIO pins, all of these examples must be run with `sudo`, for example

    sudo ./clock.py

or

    sudo python clock.py    


The example in this hat folder are only work on the Unicorn HAT and have not been adapted for the pHAT geometry.


clock.py
--------

Uses `graphics.py` and shows how you can, but probably shouldn't, display an analogue clock on Unicorn HAT!


matrix.py
---------

Knock, knock, Neo.


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


