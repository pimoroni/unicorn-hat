.PHONY: clean lib

all: unicorn

lib:
	make -C ../../library/rpi-ws281x/lib/ lib

unicorn: lib
	gcc -Wall unicorn.c -o unicorn -I../../library/rpi-ws281x/lib -L../../library/rpi-ws281x/lib -lm -lws2811 -lpng

clean:
	make -C ../../library/rpi-ws281x/lib/ clean
	-rm -f unicorn
