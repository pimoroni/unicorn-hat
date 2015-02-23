all: lib test

lib:
	gcc -o ws2811.o -c -g -O2 -Wall -Werror ws2811.c
	gcc -o pwm.o -c -g -O2 -Wall -Werror pwm.c
	gcc -o dma.o -c -g -O2 -Wall -Werror dma.c
	gcc -o board_info.o -c -g -O2 -Wall -Werror board_info.c
	gcc -o mailbox.o -c -g -O2 -Wall -Werror mailbox.c
	ar rc libws2811.a ws2811.o pwm.o dma.o board_info.o mailbox.o
	ranlib libws2811.a

test:
	gcc -o main.o -c -g -O2 -Wall -Werror main.c
	gcc -o test main.o libws2811.a

clean:
	-rm ws2811.o pwm.o dma.o board_info.o mailbox.o
	-rm libws2811.a
	-rm test
