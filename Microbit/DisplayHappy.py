from microbit import *
y = 0
x = 0
# faire parcourir un pixel sur les axes
# while True:
#     display.clear()
#     display.set_pixel(x, 0, 9)
#     display.set_pixel(0, y, 9)
#     x += 1
#     x %= 5
#     y += 1
#     y %= 5
#     sleep(100)

while True:
    for x in range(5):
        for y in range(5):
            display.clear()
            display.set_pixel(x, y, 9)
            sleep(100)
