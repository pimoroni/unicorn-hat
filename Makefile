all: lib
	gcc -Wall leds.c -o leds -L. -lws2812-RPi -lpng


lib:
	gcc -fPIC -c ws2812-RPi.c
	ar rc libws2812-RPi.a ws2812-RPi.o
	ranlib libws2812-RPi.a

bindings:
	swig2.0 -python ws2812-RPi.i

module: lib bindings
	./setup.py build

module_install: lib bindings
	sudo ./setup.py install

shared:
	gcc -fPIC -c ws2812-RPi.c
	gcc -shared ws2812-RPi.o -o ws2812-RPi.so	

clean:
	-rm -rf build/
	-rm *.o
	-rm *.a
