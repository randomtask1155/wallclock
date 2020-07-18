#!/usr/bin/python3

import time
import board
import neopixel
import time
import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import digits

h0 = 189
h1 = 126
m0 = 63
m1 = 0
pink = (252,15,192)
shadedSpruce = (0,89,96)
pixel_pin = board.D18

num_pixels = 219

    #pixel_pin, num_pixels, brightness=0.2, auto_write=False
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2
)

#pixels.fill((252, 15, 192)) # pink
#pixels.fill((252, 15, 192))


digits.Zero(pixels, m1, pink)
digits.Eight(pixels, m0, shadedSpruce)
digits.Nine(pixels, h1, (252,15,192))
digits.One(pixels, h0, (252,15,192))
time.sleep(3)
pixels.fill((0, 0, 0))




