from microbit import *
from random import randint
value = 0

while True:
    display.show(value)
    if button_a.is_pressed():
        value += 1
    elif button_b.is_pressed():
        value -= 1
    elif accelerometer.was_gesture("shake"):
        display.show(Image.SAD)
        sleep(2000)
        value = 0
