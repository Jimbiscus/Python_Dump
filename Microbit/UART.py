from microbit import *

heads = Image(
    "99999:"
    "99099:"
    "90909:"
    "99099:"
    "99999")

tails = Image(
    "99999:"
    "99999:"
    "90909:"
    "90909:"
    "99999")

while True:
    msg = uart.read()
    if msg:

        if msg == b"Heads":
            display.show(heads)
        elif msg == b"Tails":
            display.show(tails)
        else:
            display.scroll(msg)


