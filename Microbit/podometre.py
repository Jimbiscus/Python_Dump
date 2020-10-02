from microbit import *
steps = 0
while True:
    if accelerometer.was_gesture("shake"):
        steps += 1
    else:
        display.show(steps,wait=False)
    elif button_a.was_pressed():
        display.scroll(steps)


