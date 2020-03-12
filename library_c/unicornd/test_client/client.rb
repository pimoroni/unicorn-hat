#!/usr/bin/ruby
#
# Copyright (C) 2014 jibi <jibi@paranoici.org>
#

require 'socket'

UNICORND_SOCKET_PATH        = "/var/run/unicornd.socket"

UNICORND_CMD_SET_BRIGHTNESS = 0
UNICORND_CMD_SET_PIXEL      = 1
UNICORND_CMD_SET_ALL_PIXELS = 2
UNICORND_CMD_SHOW           = 3

def connect
  $sock = UNIXSocket.new(UNICORND_SOCKET_PATH)
end

def set_brightness(val)
  $sock.write([UNICORND_CMD_SET_BRIGHTNESS, val].pack("CC"))
end

def set_pixel(x,y,r,g,b)
  $sock.write([UNICORND_CMD_SET_PIXEL, x, y, r, g, b].pack("CCCCCC"))
end

def set_all_pixels(pixels)
  $sock.write([UNICORND_CMD_SET_ALL_PIXELS, pixels].flatten.pack("C*"))
end

def show
  $sock.write([UNICORND_CMD_SHOW].pack("C"))
end

connect

set_brightness(40)

set_pixel(2,2, 255, 0, 0)
set_pixel(4,4, 0, 255, 0)
set_pixel(6,6, 0, 0, 255)

show

sleep(2)

pixels = []

8.times do |x|
  8.times do |y|
    z = (x + y) % 3
    case z
    when 0
      pixels << [255,0,0]
    when 1
      pixels << [0,255,0]
    when 2
      pixels << [0,0,255]
    end
  end
end

set_all_pixels(pixels)

show

