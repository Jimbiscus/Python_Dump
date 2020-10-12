from microbit import *
import radio
radio.config(channel=7)
radio.on()
x = 2
y = 2
p2x = 2

def display_pixel(x, p2x):
    display.clear()
    display.set_pixel(x, 2, 9)
    display.set_pixel(p2x, 0, 9)
while True:
    incoming = radio.receive()
    display.set_pixel(x, y, 9)
    if button_b.was_pressed():
        if x < 4:
            x+=1
            radio.send(z)
            display_pixel(x, p2x)
        if x == 4:
            x = 4
    if button_a.was_pressed():
        if x > 0:
            x-=1
            z = str(x) + str(0)

            radio.send(z)
            display_pixel(x, p2x)



        if x < 0:
            x = 0
    if incoming:
        display.clear()
        p2x = incoming[0]
        p2y = 0
        display.clear()
        display.set_pixel(int(p2x), int(p2y), 9)
        display.set_pixel(x, y, 9)

