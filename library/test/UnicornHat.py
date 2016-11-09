import atexit
import socket
import time


sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Unicorn Started')

connected = False
port = 7676
pixels = ['000000'] * 64
attempt = 0

while not connected:
    try:
        time.sleep(0.5)
        print('Trying port',port + attempt)
        sck.connect(('127.0.0.1',port + attempt))
        connected = True
        print('Connected',port + attempt)
    except:
        if attempt >= 10:
            exit("Unable to connect to UnicornHat Emulator")
        attempt += 1

def close():
    send('stop')
    sck.shutdown(socket.SHUT_RDWR)
    sck.close()

atexit.register(close)

def send(cmd):
    print(cmd);
    sck.send(cmd + '\n')

def clear():
    send('clear')

def set_pixel(x, y, r, g, b):

    r = hex(r)[2:].zfill(2)
    g = hex(g)[2:].zfill(2)
    b = hex(b)[2:].zfill(2)

    pixels[(x*8) + y] = ''.join([r,g,b])
    #send( ','.join([str(x),str(y),str(r),str(g),str(b)]) )

def show():
    #send('show')
    send(','.join(pixels))
