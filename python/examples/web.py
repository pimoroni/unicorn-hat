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
	<link href="//maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet">
	<link rel="stylesheet" type="text/css" href="//cdn.jsdelivr.net/jquery.minicolors/2.1.2/jquery.minicolors.css">
</head>
<body>"""
	output += control_panel
	output += """
	<ul class="tools">
		<li class="paint"><span class="fa fa-paint-brush"></span></li>
		<li class="pick"><span class="fa fa-eyedropper"></span></li>
	</ul>
	<p>Endpoints:</p>
	<ul>
		<li>/pixel/x/y/r/g/b - set pixel at x/y to colour r/g/b</li>
	</ul>
	<script type="text/javascript">
		var col = {};
		var tool = 'paint';
		var md = false;
		$(document).ready(function(){
			$('table').on('mousedown',function(e){e.preventDefault();md=true;console.log(md);return false;});
			$('table').on('mouseup',function(e){e.preventDefault();md=false;console.log(md);return false;});

			$('.tools li').on('click',function(){
				tool = $(this).attr('class');
			});

			function handle_tool(obj){
				switch(tool){
					case 'paint':
						paint(obj);
						break;
					case 'pick':
						pick(obj);
						break;
				}
			}

			function set_color(hex){
				hex = hex.replace('#','');
				r = parseInt('0x' + hex.substring(0,2));
				g = parseInt('0x' + hex.substring(2,4));
				b = parseInt('0x' + hex.substring(4,6));
				col = {'hex': hex, 'r': r, 'g': g, 'b': b};
			}

			function pick(obj){
				var hex = $(obj).data('hex');
				$('input').minicolors('value','#' + hex);
				set_color(hex);
			}

			function paint(obj){
				if( col.hex != $(obj).data('hex') ){
					$(obj).data('hex', col.hex);
					x = $(obj).data('x');
					y = $(obj).data('y');
					$(obj).css('background-color','#' + col.hex)
					r = col.r;
					g = col.g;
					b = col.b;
					console.log(x, y);
					$.get('/pixel/' + x + '/' + y + '/' + r + '/' + g + '/' + b);
					$.get('/show');
				}
			}

			$('table td').on('click',function(){
				handle_tool(this);
			});
			$('table td').on('mousemove',function(){
				if(!md) return false;
				handle_tool(this);
			})
			$('.mc').minicolors({
					change: function(hex, opacity) {
						set_color(hex);
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