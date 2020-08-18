import time
from rpi_ws281x import *
import random as rand

LED_COUNT = 450
LED_PIN = 12
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 10
LED_INVERT = False
LED_CHANNEL = 0

def main():
    strip = Adafruit_NeoPixel(
            LED_COUNT,
            LED_PIN,
            LED_FREQ_HZ,
            LED_DMA,
            LED_INVERT,
            LED_BRIGHTNESS,
            LED_CHANNEL)

    strip.begin()

    try:
        better_rainbow(strip)
    except KeyboardInterrupt:
        wipe(strip)

def rainbow(strip):
    col = [255, 0, 0]
    curr = 1
    sets = 10
    i = 0

    while True:
        for j in range(sets):
            strip.setPixelColor((i + j) % strip.numPixels(), Color(col[0], col[1], col[2]))
        col[curr] += 1

        if col[curr] == 255:
            while col[(curr - 1) % 3] > 0:
                for j in range(sets):
                    strip.setPixelColor((i + j) % strip.numPixels(), Color(col[0], col[1], col[2]))
                col[(curr - 1) % 3] -= 1

            curr = (curr + 1) % 3

        i = (i + sets) % strip.numPixels()
        strip.show()
        time.sleep(5.0/1000.0)

def better_rainbow(strip):
    col = [255, 0, 0]
    pixels = []
    for k in range(strip.numPixels()):
        pixels.append(col)
        color_wheel(col)

    while True:
        for j in range(strip.numPixels()):
            color_wheel(pixels[j])
            strip.setPixelColor(j, Color(pixels[j][0], pixels[j][1], pixels[j][2])) 
        strip.show()
        time.sleep(500.0/1000.0)


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
            return

        if col[1] > 0 and col[1] < 255:
            col[1] += 1
            return
        else:
            col[2] -= 1
            return

    if col[1] == 255:
        if col[2] == 255:
            col[1] -= 1
            return

        if col[2] > 0 and col[2] < 255:
            col[2] += 1
            return
        else:
            col[0] -= 1
            return

    if col[2] == 255:
        if col[0] == 255:
            col[2] -= 1
            return
        
        if col[0] > 0 and col[0] < 255:
            col[0] += 1
            return
        else:
            col[1] -= 1
            return

def set_color_range(strip, color, start, end):
    for i in range(start, end):
        strip.setPixelColor(i, color)
    strip.show()

def wipe(strip):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()

if __name__ == '__main__':
    main()
