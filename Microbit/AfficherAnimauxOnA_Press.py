from microbit import *
from random import choice

t = [Image.HEART, Image.COW, Image.SAD, Image.DUCK]
index = 0
while True:
    if button_a.was_pressed():
        index += 1
        index %= len(t)
    display.show(t[index])

