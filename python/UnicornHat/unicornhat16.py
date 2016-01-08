# adjusted version of unicorn hat to support a 16 x 16 grid and an attempt to make it general
# This library should now work with much larger grids and you'll not have to write out the map matrix by hand
#Just change the LED_PER_ROW and LED_PER_COL values
from neopixel import *
import atexit
import colorsys

# LED strip configuration:
LED_PER_ROW    = 16      # Number of LED's per row
LED_PER_COL    = 16      # Number of LED's per colum
LED_COUNT      = LED_PER_ROW * LED_PER_COL     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

ws2812 = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
ws2812.begin()

"""
Store the rotation of UnicornHat, defaults to
0 which places 0,0 on the top left with the B+
HDMI port facing downwards
"""
_rotation = 0


"""
Store a map of pixel indexes for
translating x, y coordinates.
"""

# naaa... Lets generate one instead !!
# ROW and COL might be wrong way 'round .. sorry

map = [] # create list

for app in range(0,LED_PER_ROW):

     map.append([]) # populate list with lists


for x in range( 0, LED_PER_ROW ):
   for y in range( 0, LED_PER_COL ):

        if x & 1 : # odd numbered rows
            v = ((( x + 1 ) * LED_PER_ROW ) - 1 ) - y
        else : # even numbered rows
            v = ( LED_PER_ROW * x ) + y

        map[x].append(v) # stuff values into lists





     

def _clean_shutdown():
    """Registered at exit to ensure ws2812 cleans up after itself
    and all pixels are turned off.
    """
    off()


def rotation(r=0):
    """Set the display rotation
    Valid values:
    0
    90
    180
    270"""

    global _rotation
    if r in [0, 90, 180, 270]:
        _rotation = r
        return True
    else:
        raise ValueError('Rotation must be 0, 90, 180 or 270 degrees')


def brightness(b=0.2):
    """Set the display brightness between 0.0 and 1.0
    0.2 is highly recommended, UnicornHat can get painfully bright!"""

    if b > 1 or b < 0:
        raise ValueError('Brightness must be between 0.0 and 1.0')

    ws2812.setBrightness(int(b*255.0))


def get_brightness():
    """Get the display brightness value
    Returns a float between 0.0 and 1.0
    """
    return 0#ws2812.getBrightness()


def clear():
    """Clear the buffer"""
    for x in range(LED_COUNT):
        ws2812.setPixelColorRGB(x, 0, 0, 0)


def off():
    """Clear the buffer and immediately update UnicornHat
    Turns off all pixels."""
    clear()
    show()


def get_index_from_xy(x, y):
    """Convert an x, y value to an index on the display"""
	
	# find limits - might be swapped
	xlim = LED_PER_ROW - 1
	ylim = LED_PER_COL - 1
	
    if x > xlim or x < 0:
        raise ValueError('X position must be between 0 and ' xlim )
    if y > ylim or y < 0:
        raise ValueError('Y position must be between 0 and  ' ylim )

    y = ylim-y

    if _rotation == 90:
        x, y = y, xlim-x
    elif _rotation == 180:
        x, y = xlim-x, ylim-y
    elif _rotation == 270:
        x, y = ylim-y, x

    return map[x][y]


def set_pixel_hsv(x, y, h, s, v):
    """Set a single pixel to a colour using HSV"""
    index = get_index_from_xy(x, y)
    if index is not None:
        r, g, b = [int(n*255) for n in colorsys.hsv_to_rgb(h, s, v)]
        ws2812.setPixelColorRGB(index, r, g, b)


def set_pixel(x, y, r, g, b):
    """Set a single pixel to RGB colour"""
    index = get_index_from_xy(x, y)
    if index is not None:
        ws2812.setPixelColorRGB(index, r, g, b)


def get_pixel(x, y):
    """Get the RGB value of a single pixel"""
    index = get_index_from_xy(x, y)
    if index is not None:
        pixel = ws2812.getPixelColorRGB(index)
        return int(pixel.r), int(pixel.g), int(pixel.b)


def set_pixels(pixels):
    for x in range(LED_PER_ROW):
        for y in range(LED_PER_COL):
            r, g, b = pixels[y][x]
            set_pixel(x, y, r, g, b)


def get_pixels():
    """Get the RGB value of all pixels in a 7x7x3 2d array of tuples"""
    return [[get_pixel(x, y) for x in range(LED_PER_ROW)] for y in range(LED_PER_COL)]


def show():
    """Update UnicornHat with the contents of the display buffer"""
    ws2812.show()


atexit.register(_clean_shutdown)
