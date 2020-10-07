from microbit import *
x = 0
y = 0
while True:
    if button_b.was_pressed():
        for i in range(5):
            display.set_pixel(x, y, 9)
            y += 1
            if y == 5:
                x += 1
                y %= 5
                x %= 5
    if button_a.was_pressed():
        for i in range(5):
            display.set_pixel(x, y, 9)
            y -= 1
            if y == 5:
                x -= 1
                y %= 5
                x %= 5
