#!/usr/bin/env python
import socket, struct

UNICORND_SOCKET_PATH        = "/var/run/unicornd.socket"

UNICORND_CMD_SET_BRIGHTNESS = 0
UNICORND_CMD_SET_PIXEL      = 1
UNICORND_CMD_SET_ALL_PIXELS = 2
UNICORND_CMD_SHOW           = 3

sock = None

def connect():
    global sock
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect(UNICORND_SOCKET_PATH)

def set_brightness(val):
    sock.send(struct.pack('=cc',*[chr(UNICORND_CMD_SET_BRIGHTNESS), val]))

def set_pixel(x,y,r,g,b):
    sock.send(''.join(chr(x) for x in [UNICORND_CMD_SET_PIXEL, x, y, r, g, b]))

def clear():
    set_all_pixels([0,0,0]*64)

def set_all_pixels(pixels):
    sock.send(chr(UNICORND_CMD_SET_ALL_PIXELS) + ''.join(chr(x) for x in pixels))

def show():
    sock.send(struct.pack('=c',chr(UNICORND_CMD_SHOW)))
