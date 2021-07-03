import config, time, random, lightapi, sin_oscillator
from rpi_ws281x import *


def main():
    light = lightapi.lights()

    try:
        sine_oscillation(light)
        #rainbow(light)
        #random_colors(light)
    except KeyboardInterrupt:
        light.update(clear=True)

def sine_oscillation(light):
    """
    Oscillates over a sine wave with red, green, and blue values
    """
    osc = sin_oscillator.SineOscillator(440, 0.5)

    x = 0
    while True:
        val = int(osc.process() * 255 + 128)
        if val <= 1:
            x += 1
        for i in range(light.strip.numPixels()):
            if x % 3 == 0:
                light.pixels[i] = [val, 0, 0]
            elif x % 3 == 1:
                light.pixels[i] = [0, val, 0]
            else:
                light.pixels[i] = [0, 0, val]


        light.update()


def random_colors(light):
    """
    Sets strip to random RGB values every 0.4 seconds
    Args:
        light(lights) : A lights object to update the LED strip
    """
    while True:
        for i in range(light.strip.numPixels()):
            light.pixels[i] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

        time.sleep(0.4)
        light.update()

def rainbow(light):
    """
    Sets strip to iterate each step in the color wheel of RGB values
    Args:
        light(lights) : A lights object to update the LED strip
    """
    light.pixels = [[255, 0, 0]]
    for i in range(light.strip.numPixels() - 1):
        light.pixels.append(color_wheel(light.pixels[i]))

    while True:
        for i in range(light.strip.numPixels()):
            light.pixels[i] = color_wheel(light.pixels[i])

        light.update()

def color_wheel(col):
    """
    Gets the next value in the color wheel given an RGB value
    Args:
        col(list) : A 3 value list of values between 0 and 255
    """
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
