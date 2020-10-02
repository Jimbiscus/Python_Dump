from microbit import *

jokes = []
while True:
    msg = uart.read()
    if msg:
        if button_a.was_pressed:
            display.scroll(msg,delay=100)


