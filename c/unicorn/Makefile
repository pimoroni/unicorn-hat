all: lib
	gcc -Wall unicorn.c -o unicorn -I../../python/rpi-ws281x/lib \
			-L../../python/rpi-ws281x/lib -lm -lws2811 -lpng

lib:
	make -C ../../python/rpi-ws281x/lib/ lib

clean:
	-rm -f unicorn
