.PHONY: clean lib

all: lib test

lib: libws2811.a


ws2811.o:
	gcc -o ws2811.o -c -g -O2 -Wall -Werror ws2811.c -fPIC

rpihw.o:
	gcc -o rpihw.o -c -g -O2 -Wall -Werror rpihw.c -fPIC

pwm.o:
	gcc -o pwm.o -c -g -O2 -Wall -Werror pwm.c -fPIC

dma.o:
	gcc -o dma.o -c -g -O2 -Wall -Werror dma.c -fPIC

mailbox.o:
	gcc -o mailbox.o -c -g -O2 -Wall -Werror mailbox.c -fPIC

libws2811.a: ws2811.o rpihw.o pwm.o dma.o mailbox.o
	ar rc libws2811.a ws2811.o rpihw.o pwm.o dma.o mailbox.o
	ranlib libws2811.a


main.o:
	gcc -o main.o -c -g -O2 -Wall -Werror main.c

test: main.o libws2811.a
	gcc -o test main.o libws2811.a


clean:
	-rm -f ws2811.o rpihw.o pwm.o dma.o mailbox.o libws2811.a main.o test
