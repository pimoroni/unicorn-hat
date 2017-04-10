#!/usr/bin/env python

import os
import stat
import threading
import time
from sys import exit

try:
    from flask import Flask, render_template
except ImportError:
    exit("This script requires the flask module\nInstall with: sudo pip install flask")

import unicornhat as unicorn


unicorn.set_layout(unicorn.AUTO)
width,height=unicorn.get_shape()

control_panel = """
    <table cellspacing="0" cellpadding="0" border-collapse="collapse">"""

for y in range(height):
    control_panel += '<tr>'
    for x in range(width):
        control_panel += '<td data-x="' + str(x) + '" data-y="' + str(y) + '" data-hex="000000" style="background-color:#000000;"></td>'
    control_panel += '</tr>'

control_panel += '</table><div class="mc"></div>'

control_panel += """
    <ul class="tools">
        <li data-tool="paint" class="paint selected"><span class="fa fa-paint-brush"></span></li>
        <li data-tool="pick" class="pick"><span class="fa fa-eyedropper"></span></li>
        <li data-tool="lighten" class="lighten"><span class="fa fa-adjust"></span> Lighten</li>
        <li data-tool="darken" class="darken"><span class="fa fa-adjust"></span> Darken</li>
    </ul>"""


app = Flask(__name__)

@app.route('/')
def home():
    if height == width:
        return render_template('painthat.html')
    else:
        return render_template('paintphat.html')

@app.route('/save/<filename>')
def save(filename):
    try:
        os.mkdir('saves/')
    except OSError:
        pass
    try:
        data = unicorn.get_pixels()
        print(filename, data)
        file = open('saves/' + filename + '.py', 'w')
        file.write('#!/usr/bin/env python\n')
        file.write('import unicornhat, signal\n')
        file.write('pixels = ' + str(unicorn.get_pixels()) + '\n')
        file.write('unicornhat.set_pixels(pixels)\n')
        file.write('unicornhat.show()\n')
        file.write('signal.pause()')
        file.close()
        os.chmod('saves/' + filename + '.py', 0o777 | stat.S_IEXEC)

        return("ok" + str(unicorn.get_pixels()))
    except AttributeError:
        print("Unable to save, please update")
        print("unicornhat library!")
        return("fail")

@app.route('/clear')
def clear():
    s = threading.Thread(None,unicorn.clear)
    s.start()
    return "ok"

@app.route('/show')
def show():
    s = threading.Thread(None,unicorn.show)
    s.start()
    return "ok"

@app.route('/pixel/<x>/<y>/<r>/<g>/<b>')
def set_pixel(x, y, r, g, b):
    x, y, r, g, b = int(x), int(y), int(r), int(g), int(b)
    unicorn.set_pixel(x, y, r, g, b)
    return "ok"

if __name__ == "__main__":
    unicorn.brightness(0.5)
    app.run(host='0.0.0.0', debug=True)
