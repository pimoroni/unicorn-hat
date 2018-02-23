import atexit
import colorsys
from rpi_ws281x import __version__ as __rpi_ws281x__, PixelStrip, Color

__version__ = '2.2.3'

# LED strip configuration:
LED_COUNT      = 64      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal
LED_BRIGHTNESS = 128     # Set to 0 for darkest and 255 for brightest
LED_CHANNEL    = 0       # PWM channel
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_GAMMA = [
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2,
2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5,
6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 11, 11,
11, 12, 12, 13, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18,
19, 19, 20, 21, 21, 22, 22, 23, 23, 24, 25, 25, 26, 27, 27, 28,
29, 29, 30, 31, 31, 32, 33, 34, 34, 35, 36, 37, 37, 38, 39, 40,
40, 41, 42, 43, 44, 45, 46, 46, 47, 48, 49, 50, 51, 52, 53, 54,
55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
71, 72, 73, 74, 76, 77, 78, 79, 80, 81, 83, 84, 85, 86, 88, 89,
90, 91, 93, 94, 95, 96, 98, 99,100,102,103,104,106,107,109,110,
111,113,114,116,117,119,120,121,123,124,126,128,129,131,132,134,
135,137,138,140,142,143,145,146,148,150,151,153,155,157,158,160,
162,163,165,167,169,170,172,174,176,178,179,181,183,185,187,189,
191,193,194,196,198,200,202,204,206,208,210,212,214,216,218,220,
222,224,227,229,231,233,235,237,239,241,244,246,248,250,252,255]

COLORS = {
    'red':(255,0,0),
    'green':(0,255,0),
    'blue':(0,0,255),
    'yellow':(255,255,0),
    'magenta':(255,0,255),
    'cyan':(0,255,255), 
    'black':(0,0,0),
    'white':(255,255,255),
    'gray':(127,127,127),
    'grey':(127,127,127)
}


"""
Store the rotation of UnicornHat, defaults to
0 which places 0,0 on the top left with the B+
HDMI port facing downwards
"""
_rotation = 0
_requested_rotation = 0
_wx = 8
_wy = 8
_map = []
_pixels = [(0,0,0) for x in range(64)]
_is_setup = False
ws2812 = None

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

def setup():
    global ws2812, _is_setup

    if _is_setup:
        return

    ws2812 = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_GAMMA)

    ws2812.begin()

    set_layout(HAT)

    atexit.register(_clean_shutdown)

    _is_setup = True


def set_gamma(gamma):
    setup()
    ws2812.setGamma(gamma)


def disable_gamma():
    setup()
    set_gamma(list(range(256)))


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
    global _requested_rotation

    if r in [0, 90, 180, 270]:
        _requested_rotation=r
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


def get_rotation():
    """Get the display rotation value

    Returns an integer, either 0, 90, 180 or 270
    """

    return _requested_rotation


def brightness(b=0.2):
    """Set the display brightness between 0.0 and 1.0

    0.2 is highly recommended, UnicornHat can get painfully bright!

    :param b: Brightness from 0.0 to 1.0 (default 0.2)
    """

    setup()

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

    setup()

    return round(ws2812.getBrightness()/128.0, 3)


def clear():
    """Clear the buffer"""

    setup()

    for x in range(64):
        ws2812.setPixelColorRGB(x, 0, 0, 0)
        _pixels[x] = (0, 0, 0)


def off():
    """Clear the buffer and immediately update UnicornHat

    Turns off all pixels.
    """

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


def set_pixel_hsv(x, y, h, s=None, v=None):
    """Set a single pixel to a colour using HSV

    :param x: Horizontal position from 0 to 7
    :param y: Veritcal position from 0 to 7
    :param h: Hue from 0.0 to 1.0 ( IE: degrees around hue wheel/360.0 )
    :param s: Saturation from 0.0 to 1.0
    :param v: Value (also known as brightness) from 0.0 to 1.0
    """

    if type(h) is tuple:
        h, s, v = h

    r, g, b = [int(n*255) for n in colorsys.hsv_to_rgb(h, s, v)]

    set_pixel(x, y, r, g, b)


def set_pixel(x, y, r, g=None, b=None):
    """Set a single pixel to RGB colour

    :param x: Horizontal position from 0 to 7
    :param y: Veritcal position from 0 to 7
    :param r: Amount of red from 0 to 255
    :param g: Amount of green from 0 to 255
    :param b: Amount of blue from 0 to 255
    """

    setup()

    if type(r) is tuple:
        r, g, b = r
    
    elif type(r) is str:
        try:
            r, g, b = COLORS[r.lower()]
        
        except KeyError:
            raise ValueError('Invalid color!')

    index = get_index_from_xy(x, y)

    if index is not None:
        ws2812.setPixelColorRGB(index, r, g, b)
        _pixels[index] = (r, g, b)


def get_pixel(x, y):
    """Get the RGB value of a single pixel

    :param x: Horizontal position from 0 to 7
    :param y: Veritcal position from 0 to 7
    """

    index = get_index_from_xy(x, y)
    if index is not None:
        return _pixels[index]


def set_all(r, g=None, b=None):
    """Set all pixels to a specific colour"""

    if type(r) is tuple:
        r, g, b = r
    
    elif type(r) is str:
        try:
            r, g, b = COLORS[r.lower()]
        
        except KeyError:
            raise ValueError('Invalid color!')

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

    setup()
    ws2812.show()

