import ws2812, atexit

def clean_shutdown():
  clear()
  # Call the cleanup function
  ws2812.terminate(0)

atexit.register(clean_shutdown)

ws2812.init(64)

def clear():
  # Clear the display
  for x in range(64):
    ws2812.setPixelColor(x,0,0,0)
  ws2812.show()
 
def get_index_from_xy(x, y):

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

  return map[x][y]

def set_pixel(x, y, r, g, b):
  index = get_index_from_xy(x, y)
  ws2812.setPixelColor(index, r, g, b)

def show():
  ws2812.show()
