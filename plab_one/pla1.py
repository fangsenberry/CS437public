from sense_hat import SenseHat
from time import sleep

import random

sense = SenseHat()

color = (255, 255, 255)
x = 4
y = 4
sense.set_pixel(x, y, color)

while True:
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    for event in sense.stick.get_events():
        if event.direction == 'up' and event.action == 'pressed':
            if y > 0:
                y -= 1
                sense.clear()
                sense.set_pixel(x, y, color)
        elif event.direction == 'down' and event.action == 'pressed':
            if y < 7:
                y += 1
                sense.clear()
                sense.set_pixel(x, y, color)
        elif event.direction == 'left' and event.action == 'pressed':
            if x > 0:
                x -= 1
                sense.clear()
                sense.set_pixel(x, y, color)
        elif event.direction == 'right' and event.action == 'pressed':
            if x < 7:
                x += 1
                sense.clear()
                sense.set_pixel(x, y, color)
        elif event.direction == 'middle' and event.action == 'pressed':
            sense.clear()
            exit()