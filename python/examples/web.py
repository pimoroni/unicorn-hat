#!/usr/bin/env python
from flask import Flask
import UnicornHat as unicorn

control_panel = '<table style="width:720px;height:720px;" cellspacing="0" cellpadding="0" border-collapse="collapse">'

for y in range(8):
	control_panel += '<tr>'
	for x in range(8):
		control_panel += '<td data-x="' + str(x) + '" data-y="' + str(y) + '" style="width:90px;height:90px;border:1px solid #333;"><input type="text" class="mc"></td>'
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
		$(document).ready(function(){
			$('.mc').minicolors();
		});
	</script>
</body>
</html>
	"""
	return output

@app.route('/pixel/<x>/<y>/<r>/<g>/<b>')
def set_pixel(x, y, r, g, b):
	x, y, r, g, b = int(x), int(y), int(r), int(g), int(b)
	unicorn.set_pixel(x, y, r, g, b)


if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)