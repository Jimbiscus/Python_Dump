from microbit import *

while True:
    msg = uart.read()
    if msg:
        display.scroll(msg, delay=70)
