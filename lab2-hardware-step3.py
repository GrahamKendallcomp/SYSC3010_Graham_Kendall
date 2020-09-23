from sense_hat import SenseHat
import time, random

'''
Hardware device used was a sensehat
Program randomly places pixel on screen edge which then 'bounces' around
'''

hat = SenseHat()

green = (0, 255, 0)
n = (0,0,0)
x = random.randint(0,7)
y = random.choice([0,7])
x_change = 1
y_change = 1

while True:
    hat.set_pixels([n,n,n,n,n,n,n,n,
                    n,n,n,n,n,n,n,n,
                    n,n,n,n,n,n,n,n,
                    n,n,n,n,n,n,n,n,
                    n,n,n,n,n,n,n,n,
                    n,n,n,n,n,n,n,n,
                    n,n,n,n,n,n,n,n,
                    n,n,n,n,n,n,n,n])
    hat.set_pixel(x,y,green)
    if x == 0:
        x_change = 1
    elif x == 7:
        x_change = -1
    if y == 0:
        y_change = 1
    elif y == 7 :
        y_change = -1
    x = x + x_change
    y = y + y_change
    time.sleep(0.2)
        

