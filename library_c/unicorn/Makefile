.PHONY: all clean

ws281x_path = ../unicornd/rpi_ws281x

all: unicorn

$(ws281x_path)/libws2811.a:
	scons -C $(ws281x_path)

unicorn: $(ws281x_path)/libws2811.a unicorn.c
	gcc -Wall unicorn.c -o unicorn -I$(ws281x_path) -L$(ws281x_path) -lm -lws2811 -lpng

clean:
	scons -C $(ws281x_path) --clean
	-rm -f unicorn
