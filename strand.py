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
        rainbow(strip)
    except KeyboardInterrupt:
        wipe(strip)

def rainbow(strip):
    col = [255, 0, 0]
    pixels = []
    for k in range(strip.numPixels()):
        pixels.append(color_wheel(col))

    while True:
        for j in range(strip.numPixels()):
            pixels[j] = color_wheel(pixels[j])
            strip.setPixelColor(j, Color(pixels[j][2], pixels[j][1], pixels[j][0]))
        strip.show()

def clash(strip):
    num_snakes = 3
    pos = {}
    for i in range(num_snakes):
        pos[strip.numPixels() // num_snakes] = Snake(10, rand_color(), True)

    while True:
        for snake in pos:
            if snake.

def rand_color()
    num = rand.randint(0, 255)
    return Color(num, (num + 85) % 255, (num + 170) % 255)

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

class Snake:
    def __init__(self, size, color, direction):
        self.size = size
        self.col = color
        self.direc = direction
