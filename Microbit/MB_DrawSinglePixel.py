from microbit import *
x = -1
y = -1
while True:
    if button_b.was_pressed():
        x += 1
        display.set_pixel(x, 0, 9)
        if x > 4:
            x // 5
            x += 1
            display.set_pixel(x, 1, 9)
