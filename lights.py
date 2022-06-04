from neopixel import Adafruit_NeoPixel, Color
import config
import time

class Lights:
    def __init__(self):
        self.strip = Adafruit_NeoPixel(config.LED_COUNT, config.LED_PIN, config.LED_FREQ_HZ, config.LED_DMA, config.LED_INVERT, config.LED_BRIGHTNESS)

        self.strip.begin()

        self.pixels = [(0,0,0) for x in range(config.LED_COUNT)]

    def update(self, clear=False):
        for i, pixel in enumerate(self.pixels):
            if clear:
                pixel = (0,0,0)

            self.strip._led_data[i] = Color(*pixel)

        self.strip.show()

