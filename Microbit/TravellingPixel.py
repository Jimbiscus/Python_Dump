from microbit import *
a = 1
b = 1
x = 0
y = 0

while True:

    while b == 1:
        display.set_pixel(x, y, 9)

        if x < 4 and b == 1:
            sleep(150)
            display.clear()
            x += b

        if b == -1:
            sleep(150)
            display.clear()
            x += b

        if x == 0:
            b = 1
        if x == 4:
            b = -1
    while b == -1:
        display.set_pixel(x, y, 9)

        if y < 4 and a == 1:
            sleep(150)
            display.clear()
            y += a
        if a == -1:
            sleep(150)
            display.clear()
            y += a

        if y == 0:
            a = 1
        if y == 4:
            a = -1
