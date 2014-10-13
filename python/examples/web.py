#!/usr/bin/env python
from flask import Flask
import UnicornHat as unicorn
import time
import threading

control_panel = '<input type="text" class="mc" style="height:30px;"><table style="width:160px;height:160px;margin-top:10px;" cellspacing="0" cellpadding="0" border-collapse="collapse">'

for y in range(8):
	control_panel += '<tr>'
	for x in range(8):
		control_panel += '<td data-x="' + str(x) + '" data-y="' + str(y) + '" style="width:20px;height:20px;border:1px solid #333;"></td>'
	control_panel += '</tr>'

control_panel += '</table>'

app = Flask(__name__)

@app.route('/')
def home():
	output = """<html>
<head>
	<title>Unicorn Hat</title>
	<script type="text/javascript" src="//cdn.jsdelivr.net/jquery/2.1.1/jquery.min.js"></script>
	<script type="text/javascript" src="//cdn.jsdelivr.net/jquery.minicolors/2.1.2/jquery.minicolors.js"></script>
	<link rel="stylesheet" type="text/css" href="//cdn.jsdelivr.net/jquery.minicolors/2.1.2/jquery.minicolors.css">
</head>
<body>"""
	output += control_panel
	output += """
	<p>Endpoints:</p>
	<ul>
		<li>/pixel/x/y/r/g/b - set pixel at x/y to colour r/g/b</li>
	</ul>
	<script type="text/javascript">
		var col = {};
		var md = false;
		$(document).ready(function(){
			$('table').on('mousedown',function(e){e.preventDefault();md=true;console.log(md);return false;});
			$('table').on('mouseup',function(e){e.preventDefault();md=false;console.log(md);return false;});
			$('table td').on('click',function(){
				if( col.hex != $(this).data('hex') ){
					$(this).data('hex', col.hex);
					x = $(this).data('x');
					y = $(this).data('y');
					$(this).css('background-color','#' + col.hex)
					r = col.r;
					g = col.g;
					b = col.b;
					console.log(x, y);
					$.get('/pixel/' + x + '/' + y + '/' + r + '/' + g + '/' + b);
					$.get('/show');
				}
			});
			$('table td').on('mousemove',function(){
				console.log('mousemove');
				if(!md) return false;
				if( col.hex != $(this).data('hex') ){
					$(this).data('hex', col.hex);
					x = $(this).data('x');
					y = $(this).data('y');
					$(this).css('background-color','#' + col.hex)
					r = col.r;
					g = col.g;
					b = col.b;
					console.log(x, y);
					$.get('/pixel/' + x + '/' + y + '/' + r + '/' + g + '/' + b);
					$.get('/show');
				}
			})
			$('.mc').minicolors({
					change: function(hex, opacity) {
						hex = hex.replace('#','');
						r = parseInt('0x' + hex.substring(0,2));
						g = parseInt('0x' + hex.substring(2,4));
						b = parseInt('0x' + hex.substring(4,6));
						col = {'hex': hex, 'r': r, 'g': g, 'b': b};
					}
				});
		});
	</script>
</body>
</html>
	"""
	return output

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
	app.run(host='0.0.0.0', debug=True)