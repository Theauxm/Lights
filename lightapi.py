import config, time, random
from rpi_ws281x import *

class lights:
    def __init__(self):
        """
        An API to sit on top of Adafruit_NeoPixel
        """
        self.strip = Adafruit_NeoPixel(
                config.LED_COUNT,
                config.LED_PIN,
                config.LED_FREQ_HZ,
                config.LED_DMA,
                config.LED_INVERT,
                config.LED_BRIGHTNESS,
                config.LED_CHANNEL)


        self.pixels = [[0, 0, 0] for i in range(self.strip.numPixels())]

        self.strip.begin()


    def update(self, clear=False):
        """
        Update the values of the LED strip given the values of self.pixels
        Args:
            clear(bool) : Boolean value based on whether the LEDs should be cleared
        """
        for i in range (self.strip.numPixels()):
            if clear:
                self.strip.setPixelColor(i, 0)
            else:
                self.strip.setPixelColor(i, Color(self.pixels[i][0],
                                                self.pixels[i][1],
                                                self.pixels[i][2]))

        self.strip.show()

    def play(self, algs):
        bon_jovi = zip(map(lambda x: x(self), algs))
        print(bon_jovi)
        while True:
            self.pixels.pop(0)


