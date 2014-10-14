#!/usr/bin/env python

import unicornhat as unicorn
from graphics import Drawing, Color
import time, signal, threading

class UnicornDrawing(Drawing):
  def __init__(self):
    Drawing.__init__(self,8,8)

  '''
  All drawing operations use the pixel method
  so we override it for UnicornHat
  '''
  def pixel(self, x, y, col):
    if x < 0 or x > 7 or y < 0 or y > 7:
      return False
    self.buffer[(x,y)] = col
    unicorn.set_pixel(x, y, col.r, col.g, col.b)

  def show(self):
  	unicorn.show()

d = UnicornDrawing()

O_X = 3
O_Y = 3
R = 3

def tick():
  currenthour = time.localtime().tm_hour
  currentmin  = time.localtime().tm_min
  currentsec  = time.localtime().tm_sec

  d.clear()

  d.circle(O_X,O_Y,R,Color(255,0,255))

  d.circle_line(O_X,O_Y,R-1,360.0*(currenthour/60.0),Color(255,0,0))
  d.circle_line(O_X,O_Y,R-1,360.0*(currentmin/60.0), Color(0,255,0))
  d.circle_line(O_X,O_Y,R-1,360.0*(currentsec/60.0), Color(0,0,255))

  d.show()

  threading.Timer(1,tick).start()

tick()
