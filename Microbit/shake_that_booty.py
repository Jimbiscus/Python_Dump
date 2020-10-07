from microbit import *
i = 0
while True:
    while accelerometer.was_gesture("shake"):
        if i < 9:
            display.show(i)
            i += 1
            display.show(i)
        else:
            i = 0
            display.show(i)

#### CORRECTION ####

while True:
    display.show(n)
    if accelerometer.was_gesture("shake"):
        n += 1
        n %= 10
