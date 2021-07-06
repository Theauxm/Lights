import config, time, random, lightapi, sin_oscillator, snake
from rpi_ws281x import *


def main():
    light = lightapi.lights()

    try:
        #overlapping_waves(light)
        #snakes(light, 10)
        #sine_oscillation(light)
        rainbow(light)
        #random_colors(light)
    except KeyboardInterrupt:
        light.update(clear=True)

def overlapping_waves(light):
    p = light.strip.numPixels()
    osc = sin_oscillator.SineOscillator(200, 0.5)
    osc_2 = sin_oscillator.SineOscillator(1000, 0.5)

    osc_arr = [0 for i in range(p)]
    osc_arr_2 = [0 for i in range(p)]

    wheel = [[255, 0, 0]]
    for i in range(light.strip.numPixels() - 1):
        wheel.append(color_wheel(wheel[i], 1))

    while True:
        for i in range(light.strip.numPixels()):
            osc_arr[i] = int(osc.process() * 255 + 128)
            osc_arr_2[i] = int(osc_2.process() * 255 + 128)
            wheel[i] = color_wheel(wheel[i], 4)
            light.pixels[i] = [(wheel[i][0] + osc_arr[i]) % light.strip.numPixels(), wheel[i][1], wheel[i][2]]

        time.sleep(0.025)
        light.update()

def snakes(light, num_snakes):
    p = light.strip.numPixels()
    osc = sin_oscillator.SineOscillator(440, 0.5)
    snake_list = [snake.snake(5, [-1,1][i%2], [255, 0, 0], i*(p//num_snakes)) for i in range(1, num_snakes + 1)]
    x = 0
    while True:
        for j in range(num_snakes):
            val = int(osc.process() * 255 + 128)
            if val <= 1:
                x += 1
            for i in range(light.strip.numPixels()):
                if x % 3 == 0:
                    new_col = [val, 0, 0]
                elif x % 3 == 1:
                    new_col = [0, val, 0]
                else:
                    new_col = [0, 0, val]
            snek = snake_list[j]
            for i in range(snek.size):
                light.pixels[(snek.index + (i * snek.direction)) % p] = new_col

            light.pixels[(snek.index - (i * snek.direction)) % p] = [0, 0, 0]
            snek.index += snek.direction
            snek.index %= p

        time.sleep(0.05)
        light.update()

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

def rand_rgb():
    """
    Generates and returns a random RGB value
    """
    return [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

def random_colors(light):
    """
    Sets strip to random RGB values every 0.4 seconds
    Args:
        light(lights) : A lights object to update the LED strip
    """
    while True:
        for i in range(light.strip.numPixels()):
            light.pixels[i] = rand_rgb()

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
        light.pixels.append(color_wheel(light.pixels[i], 1))

    while True:
        for i in range(light.strip.numPixels()):
            light.pixels[i] = color_wheel(light.pixels[i], 1)

        light.update()


def color_wheel(col, iter):
    """
    Gets the next value in the color wheel given an RGB value
    Args:
        col(list) : A 3 value list of values between 0 and 255
    """
    if iter == 0:
        return col

    if col[0] == 0 and col[1] == 255 and col[2] == 0:
        col[2] += 1
    if col[0] == 255 and col[1] == 0 and col[2] == 0:
        col[1] += 1
    if col[0] == 0 and col[1] == 0 and col[2] == 255:
        col[0] += 1

    if col[0] == 255:
        if col[1] == 255:
            col[0] -= 1
            return color_wheel(col, iter - 1)

        if col[1] > 0 and col[1] < 255:
            col[1] += 1
            return color_wheel(col, iter - 1)
        else:
            col[2] -= 1
            return color_wheel(col, iter - 1)

    if col[1] == 255:
        if col[2] == 255:
            col[1] -= 1
            return color_wheel(col, iter - 1)

        if col[2] > 0 and col[2] < 255:
            col[2] += 1
            return color_wheel(col, iter - 1)
        else:
            col[0] -= 1
            return color_wheel(col, iter - 1)

    if col[2] == 255:
        if col[0] == 255:
            col[2] -= 1
            return color_wheel(col, iter - 1)
        
        if col[0] > 0 and col[0] < 255:
            col[0] += 1
            return color_wheel(col, iter - 1)
        else:
            col[1] -= 1
            return color_wheel(col, iter - 1)

if __name__ == "__main__":
    main()
