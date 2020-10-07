from microbit import *

value = 0

while True:
    for n in range(value % 26):
        x = n % 5
        y = n // 5
        display.set_pixel(x, y, 9)
    if button_b.was_pressed():
        value += 1
    elif button_a.was_pressed():
        value -= 1
        for n in range(5):
            display.set_pixel(x, y, 0)
