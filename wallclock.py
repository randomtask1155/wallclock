#!/usr/bin/python3

import time
import board
import neopixel
import time
import sys
import os
import datetime
import math


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import digits

# digit offsets
h0 = 189
h1 = 126
m0 = 63
m1 = 0

# sub lights offest
sub0 = 207

hd0Cache = -1
hd1Cache = -1
md0Cache = -1
md1Cache = -1 # used to save the current minute so we know when to update the clock
sub0Cache = -1 # 0 for morning and 1 for night


# colors
white = (255,255,255)
pink = (252,15,192)
green = (0,255,0)
shadedSpruce = (0,89,96)
clockColor=white

## set up led strip
defaultBrightness = 0.2
pixel_pin = board.D18
num_pixels = 219
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=defaultBrightness
)

pixels.fill((255, 255, 255))

def getTime():
    now = datetime.datetime.now()
    return now.hour, now.minute

def displayNumber(n, offset, color):
    digits.emptyLEDs(pixels, offset)
    if n == 0:
        digits.Zero(pixels, offset,color)
    elif n == 1:
        digits.One(pixels, offset,color)
    elif n == 2:
        digits.Two(pixels, offset,color)
    elif n == 3:
        digits.Three(pixels, offset,color)
    elif n == 4:
        digits.Four(pixels, offset,color)
    elif n == 5:
        digits.Five(pixels, offset,color)
    elif n == 6:
        digits.Six(pixels, offset,color)
    elif n == 7:
        digits.Seven(pixels, offset,color)
    elif n == 8:
        digits.Eight(pixels, offset,color)
    elif n == 9:
        digits.Nine(pixels, offset,color)

def checkNeedsUpdate(m):
    if m != minuteCache:
        return True
    return False

def fillSublights(color, brightness):
    pixels.brightness = brightness
    digits.fillLEDs(pixels, sub0, num_pixels, color)
    pixels.brightness = defaultBrightness

while True:
    h,m = getTime()
    md0 = math.floor(m / 10)
    md1 = m % 10
    hd0 = 0
    hd1 = h
    if h > 12:
        hd1 = h - 12 
    if hd1 > 9:
        hd0 = 1
        hd1 = hd1 - 10

    if hd0 != hd0Cache:
        if hd0 == 1:
            digits.fillOne(pixels, h0, clockColor)
        else:
            digits.emptyOne(pixels, h0)
    #print (hd0,hd1,md0,md1) 
        
    if hd1 != hd1Cache:
        displayNumber(hd1, h1, clockColor)
    if md0 != md0Cache:
        displayNumber(md0, m0, clockColor)
    if md1 != md1Cache:
        displayNumber(md1, m1, clockColor)
    hd0Cache = hd0
    hd1Cache = hd1
    md0Cache = md0
    md1Cache = md1

    if h >= 20 and h < 7 and sub0Cache != 1:
        fillSublights(white, .8)
        sub0Cache = 1
    if h >=7 and h < 20 and sub0Cache != 0:
        fillSublights(white, .2)
        sub0Cache = 0

    time.sleep(3)
    


