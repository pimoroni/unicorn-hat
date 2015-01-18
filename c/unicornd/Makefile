all: lib
	gcc -Wall unicornd.c -o unicornd -I../../python/ws2812/lib -L../../python/ws2812/lib -lws2812-RPi

lib:
	make -C ../../python/ws2812/lib/

clean:
	-rm unicornd

install:
	cp unicornd /usr/sbin
	cp unicorn /etc/init.d
