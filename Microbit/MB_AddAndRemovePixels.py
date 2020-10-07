from microbit import *

value = 0

while True:
    x = 0
    y = 0
    for n in range(value % 26):
        x = n % 5
        y = n // 5
        display.set_pixel(x, y, 9)
    if button_b.was_pressed():
        value += 1
    if button_a.was_pressed() and value != 0:
        value -= 1
        display.set_pixel(x,y,0)

    if value > 25:
        value = 25
