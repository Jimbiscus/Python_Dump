from microbit import *
x = -1
while True:

    if button_b.was_pressed():
        x += 1
        if x > 4:
            x = 4

        for y in range(5):
            display.set_pixel(x, y, 9)
    elif button_a.was_pressed():


        if x > -1:
            of
            for y in range(5):
                display.set_pixel(x, y, 0)

            x -= 1
            if x < -1:
                x = -1

        else:
            pass

