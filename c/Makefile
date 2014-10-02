all: lib
	gcc -Wall unicorn.c -o unicorn -I../python/ws2812/lib -L../python/ws2812/lib -lws2812-RPi -lpng

lib:
	make -C ../python/ws2812/lib/

clean:
	-rm unicorn
