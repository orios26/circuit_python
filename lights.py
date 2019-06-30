from adafruit_circuitplayground.express import cpx
from random import randint
import time

rainbow_colors = [(255, 0, 0),(255, 85, 0),(255, 255, 0),(0, 255, 0),(34, 139, 34),(34, 139, 34),(0, 255, 255),(0, 0, 255),(255, 0, 255),(75, 0, 130)]
rgb = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

def color_rand():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    s = (r, g, b)
    return tuple(s)

def color_randomizer():
    for i in range(10):
        time.sleep(.1)
        cpx.pixels[i] = color_rand()

def color_white_rotate():
    for i in range(3):
        time.sleep(.1)
        cpx.pixels.fill( rgb[i])
        for j in range(10):
            time.sleep(.1)
            cpx.pixels[j] = (125, 125, 125)

def xmas():
    r = (255, 0, 0)
    g = (0, 255, 0)
    cpx.pixels.fill(r)
    for i in range(2):
        time.sleep(.1)
        cpx.pixels[0+i] = g
        cpx.pixels[2+i] = g
        cpx.pixels[4+i] = g
        cpx.pixels[6+i] = g
        cpx.pixels[8+i] = g
        time.sleep(.1)

def tony_stark():
    cpx.pixels.fill((0,0,0))
    for i in range(125):
        time.sleep(.3)
        cpx.pixels.fill((0+i,0+i,0+i))


def cotton_candy():
    cpx.pixels.fill((125, 10, 45))
    for i in range(2):
        time.sleep(1)
        cpx.pixels[0+i] = (0, 0, 255)
        cpx.pixels[2+i] = (0, 0, 255)
        cpx.pixels[4+i] = (0, 0, 255)
        cpx.pixels[6+i] = (0, 0, 255)
        cpx.pixels[8+i] = (0, 0, 255)
        time.sleep(1)

def rainbow():
    cpx.pixels[0] = rainbow_colors[0]
    cpx.pixels[1] = rainbow_colors[1]
    cpx.pixels[2] = rainbow_colors[2]
    cpx.pixels[3] = rainbow_colors[3]
    cpx.pixels[4] = rainbow_colors[4]
    cpx.pixels[5] = rainbow_colors[5]
    cpx.pixels[6] = rainbow_colors[6]
    cpx.pixels[7] = rainbow_colors[7]
    cpx.pixels[8] = rainbow_colors[8]
    cpx.pixels[9] = rainbow_colors[9]

def rainbow_color_rotate():
    cpx.pixels.fill(color_rand())
    for i in range(10):
        for j in rainbow_colors:
            time.sleep(.01)
            cpx.pixels[i] = j
        time.sleep(.1)
        cpx.pixels.fill(j)

while True:
    if cpx.button_a:
        rainbow()
    elif cpx.button_b:
        xmas()
    else:
        rainbow_color_rotate()
