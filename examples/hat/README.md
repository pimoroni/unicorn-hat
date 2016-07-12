Unicorn HAT Examples
====================

By virture of the Unicorn HAT being a HAT(!), and hence using the Raspberry Pi's GPIO pins, all of these examples must be run with `sudo`, for example

    sudo ./clock.py

or

    sudo python clock.py    


The example in this hat folder are only workin on the Unicorn HAT and have not been adapted for the pHAT geometry. Feel free to give it a try and move them down to the examples folder if you are successfull.


clock.py
--------

Uses `graphics.py` and shows how you can, but probably shouldn't, display an analogue clock on Unicorn HAT!

graphics.py
-----------

Used by clock.py

eve.py
------

TODO: Please fill some information about this example code.
Seems to monitor usb device?!

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

Shows how you can open and display a PNG image file (here lofi.png), great for sprite animations.

**Requirements:**

    sudo pip install pillow


