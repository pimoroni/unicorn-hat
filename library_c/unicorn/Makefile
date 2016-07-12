all: lib
	gcc -Wall unicorn.c -o unicorn -I../../library/rpi-ws281x/lib -L../../library/rpi-ws281x/lib -lm -lws2811 -lpng

lib:
	make -C ../../library/rpi-ws281x/lib/ lib

clean:
	-rm -f unicorn
