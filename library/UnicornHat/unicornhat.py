import atexit
import colorsys

from neopixel import Adafruit_NeoPixel


# LED strip configuration:
LED_COUNT      = 64      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 128     # Set to 0 for darkest and 255 for brightest
LED_CHANNEL    = 0       # PWM channel
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

ws2812 = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
ws2812.begin()

"""
Store the rotation of UnicornHat, defaults to
0 which places 0,0 on the top left with the B+
HDMI port facing downwards
"""
_rotation = 0
_wx = 8
_wy = 8
_map = []

"""
Store a map of pixel indexes for
translating x, y coordinates.
"""
HAT = [
    [7 , 6 , 5 , 4 , 3 , 2 , 1 , 0 ],
    [8 , 9 , 10, 11, 12, 13, 14, 15],
    [23, 22, 21, 20, 19, 18, 17, 16],
    [24, 25, 26, 27, 28, 29, 30, 31],
    [39, 38, 37, 36, 35, 34, 33, 32],
    [40, 41, 42, 43, 44, 45, 46, 47],
    [55, 54, 53, 52, 51, 50, 49, 48],
    [56, 57, 58, 59, 60, 61, 62, 63]
]

PHAT_VERTICAL = [
    [0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 ],
    [8 , 9 , 10, 11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20, 21, 22, 23],
    [24, 25, 26, 27, 28, 29, 30, 31]
]

PHAT = [
    [24, 16, 8,  0],
    [25, 17, 9,  1],
    [26, 18, 10, 2],
    [27, 19, 11, 3],
    [28, 20, 12, 4],
    [29, 21, 13, 5],
    [30, 22, 14, 6],
    [31, 23, 15, 7]
]

AUTO = None

def set_layout(pixel_map = AUTO):
    """Set the layout to Unicorn HAT or Unicorn pHAT

    Note: auto detection relies upon the HAT EEPROM. Your Unicorn HAT
    must be connected before boot to successfully auto detect.

    :param pixel_map: Choose the layout to set, can be either HAT, PHAT, PHAT_VERTICAL or AUTO
    """
    global _map
    if pixel_map is None:
        pixel_map = PHAT # Assume PHAT
        try:
            product = open("/proc/device-tree/hat/product","r").read().strip()
            if product[:11] == "Unicorn HAT":
                pixel_map = HAT
        except IOError:
            pass
        
    _map = pixel_map

def get_shape():
    """Returns the shape (width, height) of the display"""
    global _map

    return (len(_map), len(_map[0]))

def _clean_shutdown():
    """Registered at exit to ensure ws2812 cleans up after itself
    and all pixels are turned off.
    """
    off()


def rotation(r=0):
    """Set the display rotation

    :param r: Specify the rotation in degrees: 0, 90, 180 or 270
    """

    global _map
    global _rotation
    if r in [0, 90, 180, 270]:
        wx = len(_map)
        wy = len(_map[0])
        if wx == wy:
          _rotation = r
        else:
          if r in [0, 180]:
            _map = PHAT
            _rotation = r
          else:
            _map = PHAT_VERTICAL
            _rotation = r-90
        return True
    else:
        raise ValueError('Rotation must be 0, 90, 180 or 270 degrees')


def brightness(b=0.2):
    """Set the display brightness between 0.0 and 1.0

    0.2 is highly recommended, UnicornHat can get painfully bright!

    :param b: Brightness from 0.0 to 1.0 (default 0.2)
    """

    if b > 1 or b < 0:
        raise ValueError('Brightness must be between 0.0 and 1.0')

    """Absolute max brightness has been capped to 50%, do not change
    this unless you know what you're doing.
    UnicornHAT draws too much current above 50%."""
    brightness = int(b*128.0)
    if brightness < 30:
        print("Warning: Low brightness chosen, your UnicornHAT might not light up!")
    ws2812.setBrightness(brightness)


def get_brightness():
    """Get the display brightness value

    Returns a float between 0.0 and 1.0
    """
    return round(ws2812.getBrightness()/128.0, 3)


def clear():
    """Clear the buffer"""
    for x in range(64):
        ws2812.setPixelColorRGB(x, 0, 0, 0)


def off():
    """Clear the buffer and immediately update UnicornHat

    Turns off all pixels."""
    clear()
    show()


def get_index_from_xy(x, y):
    """Convert an x, y value to an index on the display

    :param x: Horizontal position from 0 to 7
    :param y: Vertical position from 0 to 7
    """
    wx = len(_map) - 1
    wy = len(_map[0]) - 1

    y = (wy)-y

    if _rotation == 90 and wx == wy:
        x, y = y, (wx)-x
    elif _rotation == 180:
        x, y = (wx)-x, (wy)-y
    elif _rotation == 270 and wx == wy:
        x, y = (wy)-y, x

    try:
        index = _map[x][y]
    except IndexError:
        index = None

    return index


def set_pixel_hsv(x, y, h, s, v):
    """Set a single pixel to a colour using HSV

    :param x: Horizontal position from 0 to 7
    :param y: Veritcal position from 0 to 7
    :param h: Hue from 0.0 to 1.0 ( IE: degrees around hue wheel/360.0 )
    :param s: Saturation from 0.0 to 1.0
    :param v: Value (also known as brightness) from 0.0 to 1.0
    """
    index = get_index_from_xy(x, y)
    if index is not None:
        r, g, b = [int(n*255) for n in colorsys.hsv_to_rgb(h, s, v)]
        ws2812.setPixelColorRGB(index, r, g, b)


def set_pixel(x, y, r, g, b):
    """Set a single pixel to RGB colour

    :param x: Horizontal position from 0 to 7
    :param y: Veritcal position from 0 to 7
    :param r: Amount of red from 0 to 255
    :param g: Amount of green from 0 to 255
    :param b: Amount of blue from 0 to 255
    """
    index = get_index_from_xy(x, y)
    if index is not None:
        ws2812.setPixelColorRGB(index, r, g, b)


def get_pixel(x, y):
    """Get the RGB value of a single pixel

    :param x: Horizontal position from 0 to 7
    :param y: Veritcal position from 0 to 7"""
    index = get_index_from_xy(x, y)
    if index is not None:
        pixel = ws2812.getPixelColorRGB(index)
        return int(pixel.r), int(pixel.g), int(pixel.b)


def set_all(r, g, b):
    """Set all pixels to a specific colour"""
    shade_pixels(lambda x, y: (r, g, b))


def shade_pixels(shader):
    """Set all pixels using a pixel shader style function

    :param pixels: A function which accepts the x and y positions of a pixel and returns values r, g and b

    For example, this would be synonymous to clear::

        set_pixels(lambda x, y: return 0,0,0)

    Or perhaps we want to map red along the horizontal axis, and blue along the vertical::

        set_pixels(lambda x, y: return (x/7.0) * 255, 0, (y/7.0) * 255)
    """
    
    width, height = get_shape()
    for x in range(width):
        for y in range(height):
            r, g, b = shader(x, y)
            set_pixel(x, y, r, g, b)


def set_pixels(pixels):
    """Set all pixels using an array of `get_shape()`"""

    shade_pixels(lambda x, y: pixels[y][x])


def get_pixels():
    """Get the RGB value of all pixels in a 7x7x3 2d array of tuples"""
    width, height = get_shape()
    return [[get_pixel(x, y) for x in range(width)] for y in range(height)]


def show():
    """Update UnicornHat with the contents of the display buffer"""
    ws2812.show()

set_layout(HAT)

atexit.register(_clean_shutdown)
