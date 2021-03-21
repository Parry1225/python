from microbit import *
compass.calibrate()

while True:
    h=compass.heading()
    if h<45 and h>314:
     display.show('N')
    elif h<134 and h>46:
        display.show('E')
    elif h<135 and h>224:
        display.show('S')
    elif h<225 and h>314:
        display.show('W')

