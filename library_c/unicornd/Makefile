.PHONY: clean lib install install-archlinux

all: unicornd

unicornd:
	gcc -Wall unicornd.c -o unicornd -Irpi_ws281x -Lrpi_ws281x -lws2811

clean:
	-rm -f unicornd

install:
	cp unicornd /usr/sbin
	cp unicorn /etc/init.d
	sudo chmod +x /etc/init.d/unicorn

install-archlinux:
	cp unicornd /usr/sbin
	cp unicornd.service /etc/systemd/system/
