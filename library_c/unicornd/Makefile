.PHONY: all clean install install-archlinux

ws281x_path = rpi_ws281x

all: unicornd

$(ws281x_path)/libws2811.a:
	scons -C $(ws281x_path)

unicornd: unicornd.c $(ws281x_path)/libws2811.a
	gcc -Wall unicornd.c -o unicornd -I$(ws281x_path) -L$(ws281x_path) -lws2811

clean:
	scons -C $(ws281x_path) --clean
	-rm -f unicornd

install:
	cp unicornd /usr/sbin
	cp unicorn /etc/init.d
	sudo chmod +x /etc/init.d/unicorn

install-archlinux:
	cp unicornd /usr/sbin
	cp unicornd.service /etc/systemd/system/
