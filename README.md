#Unicorn Hat Python Library & Examples

Available from Pimoroni: http://shop.pimoroni.com/products/unicorn-hat

Here you'll find everything you need to start lighting up your UnicornHat in python.

Python users should probably ignore most of this repository and just:

**Full install for beginners:**

```bash
\curl -sS get.pimoroni.com/unicornhat | bash
```

**Install for Python 3 ( idle3 ):**

```bash
sudo apt-get install python3-pip python3-dev
sudo pip-3.2 install unicornhat
```

**Install for Python 2 ( idle ):**

```bash
sudo apt-get install python-pip python-dev
sudo pip install unicornhat
```

Then proceed to [python/examples](python/examples).

###Using with idle/idle3:

Unicorn HAT needs root to function. Please make sure you start LXTerminal and run idle or idle3 with the "sudo" command like so:

```bash
sudo idle
```

##Based Upon rpi_ws281x

Unicorn HAT is based upon a modified, Pi 2 compatible version of the RPi ws281x Library by Jeremy Garff.

The library was modified by Richard Hirst.

* Modified version: https://github.com/richardghirst/rpi_ws281x
* Original: https://github.com/jgarff/rpi_ws281x

##RaspberryPi-NeoPixel-WS2812

Note: Unicorn HAT is no longer based upon this library, but this information is included for posterity.

Unicorn Hat was previously based upon a modified version of the ws2812 C driver from: https://github.com/626Pilot/RaspberryPi-NeoPixel-WS2812
