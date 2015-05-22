#!/usr/bin/ruby
#
# Copyright (C) 2014 jibi <jibi@paranoici.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
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

