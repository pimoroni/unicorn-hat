%module ws2812

%{
#include "lib/ws2812-RPi.h"
%}

%typemap(in) (unsigned char *data, int len) {
      $1 = (unsigned char *) PyString_AsString($input);
      $2 = PyString_Size($input);
};

%apply unsigned char { uint8_t };

typedef struct {
        unsigned char r;
        unsigned char g;
        unsigned char b;
} Color_t;

extern void init(int numPixels);
extern void clear(void);
extern void show(void);

extern Color_t Wheel(uint8_t WheelPos);
extern void colorWipe(Color_t c, uint8_t wait);
extern void rainbow(uint8_t wait);
extern void rainbowCycle(uint8_t wait);
extern void theaterChase(Color_t c, uint8_t wait);
extern void theaterChaseRainbow(uint8_t wait);
extern unsigned char setBrightness(double b);
extern double getBrightness();

extern Color_t RGB2Color(unsigned char r, unsigned char g, unsigned char b);
extern Color_t Color(unsigned char r, unsigned char g, unsigned char b);
extern unsigned char setPixelColor(unsigned int pixel, unsigned char r, unsigned char g, unsigned char b);
extern unsigned char setPixelColorT(unsigned int pixel, Color_t c);
extern Color_t getPixelColor(unsigned int pixel);
extern unsigned int numPixels(void);
extern Color_t* getPixels(void);
extern void setPWMBit(unsigned int bitPos, unsigned char bit);
extern unsigned char getPWMBit(unsigned int bitPos);

extern void dumpLEDBuffer(void);
extern void dumpPWMBuffer(void);
extern void dumpPWMStatus(void);
extern void dumpPWMControl(unsigned int word);
extern void dumpPWMDMAC(void);
extern void dumpPWM(void);
extern void dumpDMARegs(void);
extern void dumpControlBlock(dma_cb_t *c);
extern void dumpTransferInformation(unsigned int TI);
extern void dumpDMA(void);

extern void terminate(int dummy);
