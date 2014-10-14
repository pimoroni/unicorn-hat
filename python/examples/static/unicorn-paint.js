var col = {};
var tool = 'paint';
var md = false;
$(document).ready(function(){
$('table').on('mousedown',function(e){e.preventDefault();md=true;console.log(md);return false;});
$('table').on('mouseup',function(e){e.preventDefault();md=false;console.log(md);return false;});

$('.tools li').on('click',function(){
	$('.tools li').removeClass('selected');
	$(this).addClass('selected');
	tool = $(this).data('tool');
});

function handle_tool(obj){
	switch(tool){
		case 'paint':
			paint(obj);
			break;
		case 'pick':
			pick(obj);
			break;
		case 'lighten':
			lighten(obj);
			break;
		case 'darken':
			darken(obj);
			break;
	}
}

function lighten(obj){
	var col = $(obj).data('hex');

	var rgb = hex_to_rgb(col);

	rgb.r+=2;
	rgb.g+=2;
	rgb.b+=2;

	col = rgb_to_hex(rgb);

	update_pixel(obj, col);
}

function darken(obj){
	var col = $(obj).data('hex');

	var rgb = hex_to_rgb(col);

	rgb.r-=2;
	rgb.g-=2;
	rgb.b-=2;

	col = rgb_to_hex(rgb);

	update_pixel(obj, col);
}

function set_color(hex){
	col = hex.replace('#','');
}

function pick(obj){
	var hex = $(obj).data('hex');
	$('.mc').minicolors('value','#' + hex);
	set_color(hex);
}

function rgb_to_hex(rgb){
	var r = rgb.r >= 0 ? (rgb.r <= 255 ? rgb.r : 255) : 0;
	var g = rgb.g >= 0 ? (rgb.g <= 255 ? rgb.g : 255) : 0;
	var b = rgb.b >= 0 ? (rgb.b <= 255 ? rgb.b : 255) : 0;
	r = r.toString(16);
	g = g.toString(16);
	b = b.toString(16);
	if( r.length < 2 ) r = '0' + r;
	if( g.length < 2 ) g = '0' + g;
	if( b.length < 2 ) b = '0' + b;
	console.log(rgb);
	return [r,g,b].join('');
}

function hex_to_rgb(hex){
	r = parseInt('0x' + hex.substring(0,2), 16);
	g = parseInt('0x' + hex.substring(2,4), 16);
	b = parseInt('0x' + hex.substring(4,6), 16);
	return {'r':r,'g':g,'b':b};
}

function update_pixel(obj, col){
	if( col != $(obj).data('hex') ){
		$(obj)
			.data('hex', col)
			.data('changed', true)
			.css('background-color','#' + col);

		//var x = $(obj).data('x');
		//var y = $(obj).data('y');

		//rgb = hex_to_rgb(col);

		//console.log('/pixel/' + x + '/' + y + '/' + rgb.r + '/' + rgb.g + '/' + rgb.b);
		
		//$.get('/pixel/' + x + '/' + y + '/' + rgb.r + '/' + rgb.g + '/' + rgb.b);
		//$.get('/show');
	}
}

function update_pixels(){
	var changed = false;
	$('td').each(function( index, obj ){
		if( $(obj).data('changed') ){
			$(obj).data('changed',false);
			changed = true;
			var x = $(obj).data('x');
			var y = $(obj).data('y');
			var col = hex_to_rgb($(obj).data('hex'));
			
			var data = [x,y,col.r,col.g,col.b];

			$.get('/pixel/' + data.join('/'));
		}
	});
	if(changed){
		$.get('/show');
	}
}

function paint(obj){
	update_pixel(obj, col);
}

$('table td').on('click',function(){
	handle_tool(this);
});
$('table td').on('mousemove',function(){
	if(!md) return false;
	handle_tool(this);
})

col = '0000FF';
$('.mc').minicolors({
		control: 'saturation',
		inline: true,
		defaultValue: '#' + col,
		change: function(hex, opacity) {
			set_color(hex);
		}
});

$.get('/clear');
$.get('/show');

var update = setInterval(update_pixels, 50);
});	

