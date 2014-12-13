import ws2812, atexit

def clean_shutdown():
  '''
  Registered at exit to ensure ws2812 cleans up after itself
  and all pixels are turned off.
  '''
  off()
  ws2812.terminate(0)

atexit.register(clean_shutdown)

'''
Initialize ws2812 with a buffer of 64 pixels ( 8x8 )
'''
ws2812.init(64)

'''
Store the rotation of UnicornHat, defaults to
0 wwhich places 0,0 on the top left with the B+
HDMI port facing downwards
'''
_rotation = 0


'''
Store a map of pixel indexes for
translating x, y coordinates.
'''
map = [
  [7 ,6 ,5 ,4 ,3 ,2 ,1 ,0 ],
  [8 ,9 ,10,11,12,13,14,15],
  [23,22,21,20,19,18,17,16],
  [24,25,26,27,28,29,30,31],
  [39,38,37,36,35,34,33,32],
  [40,41,42,43,44,45,46,47],
  [55,54,53,52,51,50,49,48],
  [56,57,58,59,60,61,62,63]
]

def rotation(r = 0):
  global _rotation
  '''
  Set the display rotation valid values:
  0
  90
  180
  270
  '''
  if r in [0,90,180,270]:
    _rotation = r
    return True
  else:
    raise ValueError('Rotation must be 0, 90, 180 or 270 degrees')
    return

def brightness(b = 0.2):
  '''
  Set the display brightness between 0.0 and 1.0
  0.2 is highly recommended, UnicornHat can get painfully bright!
  '''
  if b > 1 or b < 0:
    raise ValueError('Brightness must be between 0.0 and 1.0')
    return
  ws2812.setBrightness(b)

def get_brightness():
  '''
  Get the display brightness value
  Returns a float between 0.0 and 1.0
  '''
  return ws2812.getBrightness()

def clear():
  '''
  Clear the buffer
  '''
  for x in range(64):
    ws2812.setPixelColor(x,0,0,0)

def off():
  '''
  Clear the buffer and immediately update UnicornHat to
  turn off all pixels.
  '''
  clear()
  show()
 
def get_index_from_xy(x, y):
  '''
  Convert an x, y value to an index on the display
  '''
  if x > 7 or x < 0:
    raise ValueError('X position must be between 0 and 7')
    return
  if y > 7 or y < 0:
    raise ValueError('Y position must be between 0 and 7')
    return

  y = 7-y

  if _rotation == 90:
    x,y = y,7-x
  if _rotation == 180:
    x,y = 7-x,7-y
  if _rotation == 270:
    x,y = 7-y,x

  return map[x][y]

def set_pixel(x, y, r, g, b):
  '''
  Set a single pixel to RGB colour
  '''
  index = get_index_from_xy(x, y)
  if index != None:
    ws2812.setPixelColor(index, r, g, b)

def get_pixel(x, y):
  '''
  Get the RGB value of a single pixel
  '''
  index = get_index_from_xy(x, y)
  if index != None:
    pixel = ws2812.getPixelColor(index)
    return (int(pixel.r), int(pixel.g), int(pixel.b))

def get_pixels():
  '''
  Get the RGB value of all pixels in a 7x7x3 2d array of tuples
  '''
  return [[get_pixel(x,y) for x in range(0,8)] for y in range(0,8)]

def show():
  '''
  Update UnicornHat with the contents
  of the display buffer
  '''
  ws2812.show()
