#!/usr/bin/python

import socket
import struct
from random import randint
from time import sleep

socket_path = "/var/run/unicornd.socket"

class Unicorn:

    flag_lumen = bytes([0])
    flag_set_px = bytes([1])
    flag_set_all_px = bytes([2])
    flag_show = bytes([3])

    def __init__(self):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    def connect(self):
        self.sock.connect(socket_path)

    def set_brightness(self, val):
        self.sock.send(struct.pack('=cc', self.flag_lumen, bytes([val])))

    def set_pixel(self, x, y, r, g, b):
        self.sock.send(self.flag_set_px + bytes([x, y, r, g, b]))

    def clear(self):
        self.set_all_pixels(0, 0, 0)

    def set_all_pixels(self, r, g, b):
        self.sock.send(self.flag_set_all_px + bytes([r, g, b] * 64))

    def show(self):
        self.sock.send(struct.pack('=c', self.flag_show))

class UnicornDemo:

    def __init__(self, unicorn):
        self.unicorn = unicorn

    def show_random(self):
        for i in range(100):
            x = randint(0, 7)
            y = randint(0, 7)
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            self.unicorn.set_pixel(x, y, r, g, b)
            self.unicorn.show()
            sleep(0.1)

def main():
    u = Unicorn()
    u.connect()
    u.set_brightness(20)
    u.clear()

    demo = UnicornDemo(u)
    #demo.show_random()

    u.clear()
    u.show()

if __name__ == "__main__":
    main()
