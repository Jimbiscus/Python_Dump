from microbit import *
a = 0
b = 1
x = 0
y = 0
while True:

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
