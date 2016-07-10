all: lib
	gcc -Wall unicornd.c -o unicornd -I../../library/rpi-ws281x/lib -L../../library/rpi-ws281x/lib -lws2811

lib:
	make -C ../../library/rpi-ws281x/lib/

clean:
	-rm unicornd

install:
	cp unicornd /usr/sbin
	cp unicorn /etc/init.d
	sudo chmod +x /etc/init.d/unicorn

install-archlinux:
	cp unicornd /usr/sbin
	cp unicornd.service /etc/systemd/system/
