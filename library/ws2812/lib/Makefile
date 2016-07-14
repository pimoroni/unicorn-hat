.PHONY: clean shared

CPU := $(shell cat /proc/cpuinfo | grep BCM | awk '{print $$3}' | tr -d ' ')

$(warning Detected CPU=$(CPU))

ifeq ($(CPU),BCM2709)
	PERI_BASE := 0x3F000000
	RPI2 := -DRPI2
else
	PERI_BASE := 0x20000000
endif

all:
	gcc -fPIC -c ws2812-RPi.c -DPERI_BASE=$(PERI_BASE) $(RPI2)
	ar rc libws2812-RPi.a ws2812-RPi.o
	ranlib libws2812-RPi.a

shared:
	gcc -fPIC -c ws2812-RPi.c -DPERI_BASE=$(PERI_BASE) $(RPI2)
	gcc -shared ws2812-RPi.o -o ws2812-RPi.so	

clean:
	-rm -f *.o
	-rm -f *.a
