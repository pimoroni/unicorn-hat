all:
	gcc -fPIC -c ws2812-RPi.c
	ar rc libws2812-RPi.a ws2812-RPi.o
	ranlib libws2812-RPi.a

shared:
	gcc -fPIC -c ws2812-RPi.c
	gcc -shared ws2812-RPi.o -o ws2812-RPi.so	

clean:
	-rm *.o
	-rm *.a
