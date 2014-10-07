Unicorn
=======

This simple C program will let you display PNG files on your Unicorn Hat, and even run frame-based animations with them.

Getting Started
---------------

You'll need to install libpng:

    sudo apt-get install libpng-dev

Then make the binary:

    make

Then try displaying an animation:

    sudo ./unicorn anim/rainbow.png

You can change the animation speed by specifying a delay between frames:

    sudo ./unicorn anim/rainbow.png 500

And you can change the brightness by specifying a value between 0 and 100:

    sudo ./unicorn anim/rainbow.png 500 1

Demo Pattern
------------

By default, unicorn will display a swirly rainbow pattern demo.

    sudo ./unicorn

You can try different brightnesses by adding them on as a parameter from 0 to 100:

    sudo ./unicorn 50
