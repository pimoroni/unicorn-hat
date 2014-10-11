Unicorn Hat C Example
=====================

This example shows the ws2812 library being used within a C application.

You'll need to install libpng before building unicorn.c

Build with:

    make

Then run unicorn for pretty lights!

Notes
-----

If you plan on writing your own C applications to control ws2812 LEDs then please pay special attention
to how unicorn.c handles exit signals and terminates cleanly.

You absolutely must call terminate() on the ws2812 library when exiting!