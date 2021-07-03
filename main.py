import config, time, random, lightapi
from rpi_ws281x import *


def main():

    light = lightapi.lights()

    try:
        rainbow(light)
        #random_colors(light)
    except KeyboardInterrupt:
        light.update(clear=True)

def random_colors(light):
    while True:
        for i in range(light.strip.numPixels()):
            light.pixels[i] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

        time.sleep(0.4)
        light.update()

def rainbow(light):
    light.pixels = [[255, 0, 0]]
    for i in range(light.strip.numPixels() - 1):
        light.pixels.append(color_wheel(light.pixels[i]))

    while True:
        for i in range(light.strip.numPixels()):
            light.pixels[i] = color_wheel(light.pixels[i])

        light.update()

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
