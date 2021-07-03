import config
from rpi_ws281x import *


def main():
    strip = Adafruit_NeoPixel(
            config.LED_COUNT,
            config.LED_PIN,
            config.LED_FREQ_HZ,
            config.LED_DMA,
            config.LED_INVERT,
            config.LED_BRIGHTNESS,
            config.LED_CHANNEL)

    strip.begin()
    wipe(strip)

def wipe(strip):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()


if __name__ == "__main__":
    main()
