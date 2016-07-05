'''
This file is used in UnicornHat examples
for drawing things.
'''
import colorsys, math

class Color():
  def __init__(self, r, g, b):
    self.r = r
    self.g = g
    self.b = b

  def __str__(self):
    r = hex(self.r)[2:]
    g = hex(self.g)[2:]
    b = hex(self.b)[2:]
    return ''.join([r,g,b])

  def rgb(self):
    return (self.r, self.g, self.b)

  def hsv(self):
    return colorsys.rgb_to_hsv(self.r, self.g, self.b)

class Drawing():
  def __init__(self,width=8,height=8):
    self.width = width
    self.height = height
    self.buffer = {}
    for x in range(width):
      for y in range(height):
        self.buffer[(x,y)] = Color(0,0,0)

  def fill(self, col = Color(0,0,0)):
    for x in range(self.width):
      for y in range(self.height):
        self.pixel(x, y, col)

  def clear(self):
    self.fill(Color(0,0,0))

  '''
  Creates a color tuple from r, g, b elements
  with values 0 to 255
  '''
  def color_from_rgb(self, r, g, b):
    return (r, g, b)

  '''
  Creates a color tuple from h, s, v elements
  with values 0.0 to 1.0
  '''
  def color_from_hsv(self, h, s, v):
    rgb = colorsys.hsv_to_rgb(h, s, v)
    return color_from_rgb( int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255) )

  def pixel(self, x, y, col):
    self.buffer[(x,y)] = col

  def circle(self, x0, y0, r, col=Color(0,0,0), fill=None):
    f = 1 - r
    ddf_x = 1
    ddf_y = -2 * r
    x = 0
    y = r
    self.pixel(x0, y0 + r, col)
    self.pixel(x0, y0 - r, col)
    self.pixel(x0 + r, y0, col)
    self.pixel(x0 - r, y0, col)

    while x < y:
      if f >= 0: 
          y -= 1
          ddf_y += 2
          f += ddf_y
      x += 1
      ddf_x += 2
      f += ddf_x
      self.pixel(x0 + x, y0 + y, col)
      self.pixel(x0 - x, y0 + y, col)
      self.pixel(x0 + x, y0 - y, col)
      self.pixel(x0 - x, y0 - y, col)
      self.pixel(x0 + y, y0 + x, col)
      self.pixel(x0 - y, y0 + x, col)
      self.pixel(x0 + y, y0 - x, col)
      self.pixel(x0 - y, y0 - x, col)

  def circle_line(self, origin_x, origin_y, radius, angle, col):
    angle = (angle / 360.0) * (2*math.pi)

    x = origin_x + radius * math.sin(angle)
    y = origin_y + radius * math.cos(angle)

    self.line( origin_x, origin_y, int(round(x)), int(round(y)), col )

  def line(self, x0, y0, x1, y1, col=Color(0,0,0)):
    s = abs(y1 - y0) > abs(x1 - x0)
    if s:
      x0, y0 = y0, x0
      x1, y1 = y1, x1

    if x0 > x1:
      x0, x1 = x1, x0
      y0, y1 = y1, y0

    dx = x1 - x0
    dy = abs(y1 - y0)

    err = dx / 2

    ystep = 0

    if y0 < y1:
      ystep = 1
    else:
      ystep = -1

    while x0<=x1:
      if s:
        self.pixel(y0, x0, col)
      else:
        self.pixel(x0, y0, col)
      err -= dy

      if err < 0:
        y0 += ystep
        err += dx

      x0+=1

  def test(self):
    out = ''
    for y in range(self.height):
      for x in range(self.width):
        if self.buffer[(x,y)].rgb() == (0,0,0):
          out += '  '
        else:
          out += '##'
      out += '\n'
    print(out)

if __name__ == '__main__':
  print("Testing color")
  print(Color(255,50,20))
  g = Drawing()
  g.test()
  print("Testing circle")
  g.circle(4,4,3,Color(255,255,255))
  g.test()
  g.clear()
  print("Testing line")
  g.line(0,0,7,7,Color(255,255,255))
  g.test()
  g.clear()
  print("Testing circle line")
  g.circle_line(4,4,3,0,Color(255,255,255))
  g.test()

