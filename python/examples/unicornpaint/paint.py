#!/usr/bin/env python
from flask import Flask
import unicornhat as unicorn
import time
import threading

control_panel = """
	<table cellspacing="0" cellpadding="0" border-collapse="collapse">"""

for y in range(8):
	control_panel += '<tr>'
	for x in range(8):
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
	output = """<html>
<head>
	<title>Unicorn Hat</title>
	<link href="//maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet">
	<link rel="stylesheet" type="text/css" href="/static/jquery.minicolors.css">
	<link rel="stylesheet" type="text/css" href="/static/unicorn-paint.css">
</head>
<body>
<div class="unicorn">"""
	output += control_panel
	output += """
	<script type="text/javascript" src="/static/jquery.min.js"></script>
	<script type="text/javascript" src="/static/jquery.minicolors.js"></script>
	<script type="text/javascript" src="/static/unicorn-paint.js"></script>
</div>
</body>
</html>
	"""
	return output

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
	unicorn.brightness(0.3)
	app.run(host='0.0.0.0', debug=True)
