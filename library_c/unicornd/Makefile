.PHONY: clean lib install install-archlinux

all: unicornd

lib:
	make -C ../../library/rpi-ws281x/lib/ lib

unicornd: lib
	gcc -Wall unicornd.c -o unicornd -I../../library/rpi-ws281x/lib -L../../library/rpi-ws281x/lib -lws2811

clean:
	make -C ../../library/rpi-ws281x/lib/ clean
	-rm -f unicornd

install:
	cp unicornd /usr/sbin
	cp unicorn /etc/init.d
	sudo chmod +x /etc/init.d/unicorn

install-archlinux:
	cp unicornd /usr/sbin
	cp unicornd.service /etc/systemd/system/
