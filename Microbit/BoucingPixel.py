from microbit import *
x = 0
goBack = False
while True:
    display.set_pixel(x%5, 2, 9)
    if x < 4 and goBack == False:
        sleep(150)
        display.clear()
        x += 1
    if x == 4:
        display.set_pixel(4, 2, 9)
        goBack = True
    if goBack == True:
        sleep(150)
        display.clear()
        x -= 1
    if x == 0:
        goBack = False
