#!/usr/bin/env python

from sense_hat import SenseHat
import time
import random
sense = SenseHat()


while True:
	r = random.randint(1, 255)
	print("The random` number is"), r, ("This time")
	sense.show_letter("H", (0, r, r))
	time.sleep(1)
	sense.show_letter("i", (r, 0, r))
	time.sleep(1)
	sense.show_letter("!", (r, r, 0))
	time.sleep(1)
sense.clear()
