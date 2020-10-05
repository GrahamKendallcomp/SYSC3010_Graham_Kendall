from sense_hat import SenseHat
import time
import keyboard

hat = SenseHat()

green = (0, 255, 0)
n = (0,0,0)

def show_g():
    hat.show_letter("G", back_colour = green)
    time.sleep(0.2)
    
def show_k():
    hat.show_letter("K", back_colour = green)
    time.sleep(0.2)
    
counter = 0
    
while True:
    if  keyboard.is_pressed('left'):
        hat.set_pixels([g,g,g,g,g,g,g,g,
                    n,n,n,n,n,n,n,n,
                    n,n,n,n,n,n,n,n,
                    n,n,n,n,n,n,n,n,
                    n,n,n,n,n,n,n,n,
                    n,n,n,n,n,n,n,n,
                    n,n,n,n,n,n,n,n,
                    n,n,n,n,n,n,n,n])
    if keyboard.is_pressed('right'):
        hat.set_pixels([n,n,n,n,n,n,n,n,
                    n,n,n,n,n,n,n,n,
                    n,n,n,n,n,n,n,n,
                    n,n,n,n,n,n,n,n,
                    n,n,n,n,n,n,n,n,
                    n,n,n,n,n,n,n,n,
                    n,n,n,n,n,n,n,n,
                    n,n,n,n,n,n,n,n])