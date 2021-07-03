import config
from rpi_ws281x import *
import time
import random

STRIP = Adafruit_NeoPixel(
            config.LED_COUNT,
            config.LED_PIN,
            config.LED_FREQ_HZ,
            config.LED_DMA,
            config.LED_INVERT,
            config.LED_BRIGHTNESS,
            config.LED_CHANNEL)

STRIP.begin()

PIXEL_MAP = [[0, 0, 0] for i in range(STRIP.numPixels())]


def main():
    try:
        #rainbow()
        random_colors()
    except KeyboardInterrupt:
        update_strip(clear=True)

def random_colors():
    while True:
        for i in range(STRIP.numPixels()):
            PIXEL_MAP[i] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

        time.sleep(0.4)
        update_strip()

def update_strip(clear=False):
    for i in range(STRIP.numPixels()):
        if clear:
            STRIP.setPixelColor(i, 0)
        else:
            STRIP.setPixelColor(i, Color(PIXEL_MAP[i][0], PIXEL_MAP[i][1], PIXEL_MAP[i][2]))

    STRIP.show()

def rainbow():
    PIXEL_MAP = [[255, 0, 0]]
    for i in range(STRIP.numPixels() - 1):
        PIXEL_MAP.append(color_wheel(PIXEL_MAP[i]))

    while True:
        for i in range(STRIP.numPixels()):
            PIXEL_MAP[i] = color_wheel(PIXEL_MAP[i])

        update_strip()

def color_wheel(col):
    if col[0] == 0 and col[1] == 255 and col[2] == 0:
        col[2] += 1
    if col[0] == 255 and col[1] == 0 and col[2] == 0:
        col[1] += 1
    if col[0] == 0 and col[1] == 0 and col[2] == 255:
        col[0] += 1

    if col[0] == 255:
        if col[1] == 255:
            col[0] -= 1
            return [col[0], col[1], col[2]]

        if col[1] > 0 and col[1] < 255:
            col[1] += 1
            return [col[0], col[1], col[2]]
        else:
            col[2] -= 1
            return [col[0], col[1], col[2]]

    if col[1] == 255:
        if col[2] == 255:
            col[1] -= 1
            return [col[0], col[1], col[2]]

        if col[2] > 0 and col[2] < 255:
            col[2] += 1
            return [col[0], col[1], col[2]]
        else:
            col[0] -= 1
            return [col[0], col[1], col[2]]

    if col[2] == 255:
        if col[0] == 255:
            col[2] -= 1
            return [col[0], col[1], col[2]]
        
        if col[0] > 0 and col[0] < 255:
            col[0] += 1
            return [col[0], col[1], col[2]]
        else:
            col[1] -= 1
            return [col[0], col[1], col[2]]



if __name__ == "__main__":
    main()
