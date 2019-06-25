#!/usr/bin/env python

from sense_hat import SenseHat
sense = SenseHat()
import random
import time

while True:
	rr = random.randint(1, 255)
	rb = random.randint(1, 255)
        rg = random.randint(1, 255)
        rx = random.randint(0, 7)
        ry = random.randint(0, 7)
        sense.set_pixel(rx, ry, (rr, rb, rg))
	time.sleep(.5)
	sense.clear()
        
