#!/usr/bin/env python

import Queue
import signal
import socket
import threading
import time
from sys import exit, version_info

try:
    from Tkinter import Canvas, Frame, Tk
except ImportError:
    if version_info[0] < 3:
        exit("This library requires python-tk\nInstall with: sudo apt-get install python-tk")
    elif version_info[0] == 3:
        exit("This library requires python3-tk\nInstall with: sudo apt-get install python3-tk")


PIXELS_X = 8
PIXELS_Y = 8
PIXEL_SPACING = 5
PIXEL_W = 10
PIXEL_H = 10
BORDER  = 10

DISPLAY_W = ((PIXEL_W + PIXEL_SPACING) * PIXELS_X) - PIXEL_SPACING + (BORDER * 2)
DISPLAY_H = ((PIXEL_H + PIXEL_SPACING) * PIXELS_Y) - PIXEL_SPACING + (BORDER * 2)

window = None
display = None

class Display(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.canvas = None
        self.buffer = {}
        self.pixels = {}
        self.pack()
        self.init_display()

    def init_display(self):
        self.canvas = Canvas(self.master, width=DISPLAY_W, height=DISPLAY_H, bg='white')
        self.canvas.pack()

        for x in range(PIXELS_X):
            for y in range(PIXELS_Y):
                pixel_x = ((PIXEL_W + PIXEL_SPACING) * x) + BORDER
                pixel_y = ((PIXEL_H + PIXEL_SPACING) * y) + BORDER
                self.buffer[ (x,y) ] = [0,0,0]
                self.pixels[ (x,y) ] = self.canvas.create_rectangle(pixel_x, pixel_y, pixel_x + PIXEL_W, pixel_y + PIXEL_H, fill='black', width=0)

    def set_pixel(self,x, y, r, g, b):
        self.buffer[ (x,y) ] = [r,g,b]

    def clear():
        # Clear the display
        for x in range(8):
            for x in range(8):
                self.set_pixel(x,y,0,0,0)
                self.show()

    def show_q(self, pixels):
        x = 0
        for idx,pixel in enumerate(pixels):
            x = idx % 8
            y = int(idx / 8)
            self.canvas.itemconfigure(self.pixels[(x,y)], fill= '#' + pixel)
            x+=1

    def show(self):
        for position, colour in self.buffer.iteritems():
            pixel = self.pixels[ position ]
            r = hex(colour[0])[2:].zfill(2)
            g = hex(colour[1])[2:].zfill(2)
            b = hex(colour[2])[2:].zfill(2)
            self.canvas.itemconfigure(pixel, fill= '#' + r + g + b)


queue = Queue.Queue()

## Basic stoppable thread wrapper
#
#  Adds Event for stopping the execution loop
#  and exiting cleanly.
class StoppableThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_event = threading.Event()
        self.daemon = True         

    def start(self):
        if self.isAlive() == False:
            self.stop_event.clear()
            threading.Thread.start(self)

    def stop(self):
        if self.isAlive() == True:
            # set event to signal thread to terminate
            self.stop_event.set()
            # block calling thread until thread really has terminated
            self.join()

## Basic thread wrapper class for asyncronously running functions
#
#  Basic thread wrapper class for running functions
#  asyncronously. Return False from your function
#  to abort looping.
class AsyncWorker(StoppableThread):
    def __init__(self, todo):
        StoppableThread.__init__(self)
        self.todo = todo

    def run(self):
        while self.stop_event.is_set() == False:
            if self.todo() == False:
                self.stop_event.set()
                break

def tcp():
    global buf, queue, client

    if client == None:
        try:
            client = sck.accept()
        except:
            pass

    if client != None:
        char = None
        try:
            char = client[0].recv(1)
        except:
            pass
        if char != None:
            if char == '\n':
                message = ''.join(buf).strip()
                if message == 'stop':
                    client = None
                else:
                    queue.put(message)
                buf = []
            else:
                buf.append(char)

    return True

buf = []
client = None
window = Tk()
display = Display(window)


def processqueue():
    try:
        message = None
        while queue.qsize() > 1:
            message = queue.get_nowait()

        if message != None:
            if message == 'show':
                display.show()
            elif message == 'clear':
                display.clear()
            else:
                message = message.split(',')
                display.show_q(message)
            ##display.set_pixel(int(message[0]),int(message[1]),int(message[2]),int(message[3]),int(message[4]))
    except Queue.Empty:
        pass
    window.after(5, processqueue)

window.after(5, processqueue)

sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sck.settimeout(0)
port = 7676
bound = False
while not bound:
    try:
        sck.bind(('127.0.0.1',port))
        bound = True
        print("Bound to",port)
    except socket.error:
        port+=1

sck.listen(50)

t_setup = AsyncWorker(tcp)
t_setup.start()

display.mainloop()
