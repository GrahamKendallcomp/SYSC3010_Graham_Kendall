from sense_hat import SenseHat
import time
import keyboard

hat = SenseHat()

green = (0, 255, 0)

def show_g():
    hat.show_letter("G", back_colour = green)
    time.sleep(0.2)
    
def show_k():
    hat.show_letter("K", back_colour = green)
    time.sleep(0.2)
    
counter = 0
    
while True:
    if keyboard.is_pressed('up') or keyboard.is_pressed('down') or keyboard.is_pressed('left') or keyboard.is_pressed('right'):
        show_g() if counter % 2 == 0 else show_k()
        counter+=1
    if keyboard.is_pressed('e'):
        break