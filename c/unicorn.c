#include "ws2812-RPi.h"

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdarg.h>
#include <stdint.h>
#include <dirent.h>
#include <fcntl.h>
#include <assert.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/time.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>
#include <math.h>
#include <time.h>
#include <signal.h>

#include <png.h>


// =================================================================================================
//	   _____         .__        
//	  /     \ _____  |__| ____  
//	 /  \ /  \\__  \ |  |/    \ 
//	/    Y    \/ __ \|  |   |  \
//	\____|__  (____  /__|___|  /
//	        \/     \/        \/ 
// =================================================================================================


void abort_(const char * s, ...)
{
        va_list args;
        va_start(args, s);
        vfprintf(stderr, s, args);
        fprintf(stderr, "\n");
        va_end(args);
        abort();
}

int x, y;

int width, height;
png_byte color_type;
png_byte bit_depth;

png_structp png_ptr;
png_infop info_ptr;
int number_of_passes;
png_bytep * row_pointers;
int anim_delay = 50;

void read_png_file(char* file_name)
{
        char header[8];    // 8 is the maximum size that can be checked

        /* open file and test for it being a png */
        FILE *fp = fopen(file_name, "rb");
        if (!fp)
                abort_("[read_png_file] File %s could not be opened for reading", file_name);
        fread(header, 1, 8, fp);
        if (png_sig_cmp(header, 0, 8))
                abort_("[read_png_file] File %s is not recognized as a PNG file", file_name);


        /* initialize stuff */
        png_ptr = png_create_read_struct(PNG_LIBPNG_VER_STRING, NULL, NULL, NULL);

        if (!png_ptr)
                abort_("[read_png_file] png_create_read_struct failed");

        info_ptr = png_create_info_struct(png_ptr);
        if (!info_ptr)
                abort_("[read_png_file] png_create_info_struct failed");

        if (setjmp(png_jmpbuf(png_ptr)))
                abort_("[read_png_file] Error during init_io");

        png_init_io(png_ptr, fp);
        png_set_sig_bytes(png_ptr, 8);

        png_read_info(png_ptr, info_ptr);

        width = png_get_image_width(png_ptr, info_ptr);
        height = png_get_image_height(png_ptr, info_ptr);
        color_type = png_get_color_type(png_ptr, info_ptr);
        bit_depth = png_get_bit_depth(png_ptr, info_ptr);

        number_of_passes = png_set_interlace_handling(png_ptr);
        png_read_update_info(png_ptr, info_ptr);


        /* read file */
        if (setjmp(png_jmpbuf(png_ptr)))
                abort_("[read_png_file] Error during read_image");

        row_pointers = (png_bytep*) malloc(sizeof(png_bytep) * height);
        for (y=0; y<height; y++)
                row_pointers[y] = (png_byte*) malloc(png_get_rowbytes(png_ptr,info_ptr));

        png_read_image(png_ptr, row_pointers);

        fclose(fp);
}

void process_file(void)
{
        /*if (png_get_color_type(png_ptr, info_ptr) == PNG_COLOR_TYPE_RGB)
                abort_("[process_file] input file is PNG_COLOR_TYPE_RGB but must be PNG_COLOR_TYPE_RGBA "
                       "(lacks the alpha channel)");

        if (png_get_color_type(png_ptr, info_ptr) != PNG_COLOR_TYPE_RGBA)
                abort_("[process_file] color_type of input file must be PNG_COLOR_TYPE_RGBA (%d) (is %d)",
                       PNG_COLOR_TYPE_RGBA, png_get_color_type(png_ptr, info_ptr));
*/
	int currentFrame;

	for (currentFrame=0; currentFrame<(height/8); currentFrame++){
        for (y=0; y<8; y++) {
                png_byte* row = row_pointers[y + (8*currentFrame)];
                for (x=0; x<width; x++) {
                        png_byte* ptr = &(row[x*3]);
                        //printf("Pixel at position [ %d - %d ] has RGB values: %d - %d - %d\n",
    //                           x, y, ptr[0], ptr[1], ptr[2]);

			setPixelColor(getPixelPosition(x,y), ptr[0], ptr[1], ptr[2]);

                        //ptr[0] = 0;
                        //ptr[1] = ptr[2];
                }
        }
	show();
	usleep(anim_delay*1000);
	}
}

void h2rgb(float h, float *r, float *g, float *b){

	int i;
	float f, p, q, t, s, v;

	s = 1.0;
	v = 1.0;

	// Wrap hue
	if(h < 0.0 || h > 1.0){
		h=fabsf(fmodf(h,1.0));	
	}

	h *= 360.0;
	h /= 60.0;

	i = floor( h );
	f = h - i;
	p = (v * ( 1 - s ));
	q = (v * ( 1 - s * f ));
	t = (v * ( 1 - s * ( 1 - f ) ));

	switch( i ){
		case 0:
			*r = v;
			*g = t;
			*b = p;
			break;
		case 1:
			*r = q;
			*g = v;
			*b = p;
			break;
		case 2:
			*r = p;
			*g = v;
			*b = t;
			break;
		case 3:
			*r = p;
			*g = q;
			*b = v;
			break;
		case 4:
			*r = t;
			*g = p;
			*b = v;
			break;
		default:
			*r = v;
			*g = p;
			*b = q;
			break;
		
	}

}

void makeRGB(float *r, float *g, float *b, 
		float f1, float f2, float f3,
		float p1, float p2, float p3,
		float c, float w, float pos){


	*r = (( sin(f1 * pos + p1) * w ) + c) / 255;
	*g = (( sin(f2 * pos + p2) * w ) + c) / 255;
	*b = (( sin(f3 * pos + p3) * w ) + c) / 255;

}

void transformPixel(float *x, float *y, float angle){

	float px, py, cs, sn;

	cs = cos(angle);
	sn = sin(angle);
	
	px = *x * cs - *y * sn;
	py = *x * sn + *y * cs;

	*x = px;
	*y = py;
}


void shadePixel(double t, int pixel, float x, float y){

	float r, g, b;

	float angle = fmod( (double)(t)/10, (double)360);

	angle /= 57.2957795;

	float px, py, cs, sn;
	
	// Move origin to center
	x-=0.5;
	y-=0.5;

	x+=sin(t/10000.0);
	y+=sin(y/10000.0);

	cs = cos(angle);
	sn = sin(angle);

	px = (x * cs) - (y * sn);
	py = (y * cs) + (x * sn);


	// Convert hue to RGB

	float hue = (((px+py)/8) + t / 10000.0);

	//hue = fmodf(hue, 1.0);
	h2rgb(hue, &r, &g, &b);

	// Reduce the brightness
	//r*=0.2;g*=0.2;b*=0.2;

	// Clamp max value
	if(r>1.0) r=1.0;
	if(g>1.0) g=1.0;
	if(b>1.0) b=1.0;

	setPixelColor(pixel, (int)(r*255), (int)(g*255), (int)(b*255));

}
/*
void shadePixel(double t, int pixel, float x, float y){
	
	float h, r, g, b;

	t /= 10.0;

	h = ((x+y)/10.0) + (fmodf(t,360.0)/360.0);

	h2rgb(h, &r, &g, &b);

	float br = ( 0.5 + (sin(t/50) / 2.0) );

	r*=br;
	g*=br;;
	b*=br;

	makeRGB(&r, &g, &b, 1.5, 0.1, 0.1, 0, 1.5, 3, 30, 30, (x+y)*t);

	r*=0.2;
	g*=0.8;

	setPixelColor(pixel, (int)(r*255), (int)(g*255), (int)(b*255));


}
*/
void run_shader(void){

	struct timeval tv;
	double t;
	while(1){
		gettimeofday(&tv, NULL);
		t = (tv.tv_sec) * 1000 + (tv.tv_usec) / 1000;
		for(y=0; y<8; y++){
			for(x=0; x<8; x++){

				int pixel = getPixelPosition(x,y);
				shadePixel(t, pixel, x/7.0, y/7.0);
	
			}
		}
		show();
		usleep(10);
	}

}

void unicorn_exit(int status){
	int i;
	for (i = 0; i < 64; i++){
		setPixelColor(i,0,0,0);
	}
	show();
	terminate(status);
}

int getPixelPosition(int x, int y){

	int map[8][8] = {
		{7 ,6 ,5 ,4 ,3 ,2 ,1 ,0 },
		{8 ,9 ,10,11,12,13,14,15},
		{23,22,21,20,19,18,17,16},
		{24,25,26,27,28,29,30,31},
		{39,38,37,36,35,34,33,32},
		{40,41,42,43,44,45,46,47},
		{55,54,53,52,51,50,49,48},
		{56,57,58,59,60,61,62,63}
	};

	return map[x][y];
}

int main(int argc, char **argv) {
	if (argc >= 3){
		if(sscanf (argv[2], "%i", &anim_delay)!=1){
			printf ("Error, delay must be an integer \n");
			return 0;
		}
	}

	setBrightness(DEFAULT_BRIGHTNESS);

	int newbrightness = 0;
	if (argc >= 4){
		if(sscanf (argv[3], "%i", &newbrightness)!=1){
			printf ("Error, brightness must be an integer \n");
			return 0;

		}else{
			setBrightness(newbrightness/100.0);
		}
	}

	int i;
	for (i = 0; i < 64; i++) {
		struct sigaction sa;
		memset(&sa, 0, sizeof(sa));
		sa.sa_handler = unicorn_exit;
		sigaction(i, &sa, NULL);
	}

	setvbuf(stdout, NULL, _IONBF, 0);
	
	numLEDs = 64;

	//setBrightness(DEFAULT_BRIGHTNESS);

	initHardware();
	clearLEDBuffer();

	if(argc < 2){
		run_shader();
	}else{

		read_png_file(argv[1]);
		while(1){
			process_file();
			if (height/8 == 1){
				break;
			}
		}
	
	}

	unicorn_exit(0);

	return 0;
}
