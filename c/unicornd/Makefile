all: lib
	gcc -Wall unicornd.c -o unicornd -I../../python/rpi-ws281x/lib -L../../python/rpi-ws281x/lib -lws2811

lib:
	make -C ../../python/rpi-ws281x/lib/

clean:
	-rm unicornd

install:
	cp unicornd /usr/sbin
	cp unicorn /etc/init.d
	sudo chmod +x /etc/init.d/unicorn

install-archlinux:
	cp unicornd /usr/sbin
	cp unicornd.service /etc/systemd/system/
