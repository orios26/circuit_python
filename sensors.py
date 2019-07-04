from adafruit_circuitplayground.express import cpx
from random import randint
import time

while True:
    light_lvl = cpx.light
    temp_c = cpx.temperature
    temp_f = (temp_c * 1.8) + 32

    print("C: " + str(temp_c))
    print("F: " + str(temp_f))
    print("Light level: " + str(light_lvl))