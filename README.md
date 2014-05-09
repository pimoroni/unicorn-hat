RaspberryPi-NeoPixel-WS2812
===========================

Library for driving WS2812 pixels (also known as "NeoPixels" when sold by Adafruit) from a Raspberry Pi.

Wishlist:
* Modify DMA code so it can use more than one 4K page, enabling >450 pixels (some people have thousands!)
* Turn this into a FIFO daemon, like ServoBlaster
* Write some effects fading stuff
* Add whatever functions are present in the Adafruit Arduino library, but not implemented here
* There are a few stupid magic numbers left that I haven't changed to DEFINEs yet
* Change calculated delay after DMA transfer start to reflect number of pixel commands sent (plus two words, to ensure low latch signal is sent) rather than the length of the entire buffer
* Make it immediately return after initiating DMA transfer, so we can begin building the next frame (for higher framerate on huge lengths of pixels)
