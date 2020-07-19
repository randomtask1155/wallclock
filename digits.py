
def fillLEDs(p, s,e, color):
    for x in range(s,e):
        p[x] = color
    ## fill twice incase we miss something
    for x in range(s,e):
        p[x] = color

def emptyOne(p, offset):
    fillLEDs(p, offset, 18+offset, (0,0,0))

def emptyLEDs(p, offset):
    fillLEDs(p, offset, 63+offset, (0,0,0))

def Zero(p, offset, color):
    fillLEDs(p, offset, 27+offset, color)
    fillLEDs(p, 36+offset, 63+offset, color)

def One (p, offset, color):
    fillLEDs(p, offset, 18+offset, color)

def Two(p, offset, color):
    fillLEDs(p, offset, 18+offset, color)
    fillLEDs(p, 27+offset, 36+offset, color)
    fillLEDs(p, 45+offset, 45+18+offset, color)

def Three(p, offset, color):
    fillLEDs(p, offset, 18+offset, color)
    fillLEDs(p, 27+offset, 27+27+offset, color)

def Four(p, offset, color):
    fillLEDs(p, offset, 9+offset, color)
    fillLEDs(p, 18+offset, 45+offset, color)

def Five(p, offset, color):
    fillLEDs(p, 9+offset, 54+offset, color)

def Six(p, offset, color):
    fillLEDs(p, 9+offset, 63+offset, color)

def Seven(p, offset, color):
    fillLEDs(p, offset, 18+offset, color)
    fillLEDs(p, 36+offset, 45+offset, color)

def Eight(p, offset, color):
    fillLEDs(p, offset, 63+offset, color)

def Nine(p, offset, color):
    fillLEDs(p, offset, 45+offset, color)



