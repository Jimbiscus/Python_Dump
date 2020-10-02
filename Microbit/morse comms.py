import music

import radio
import random
from microbit import *

radio.on()
while True:
    incoming = radio.receive()
    if incoming == "dot":
        display.show(".")
        sleep(1000)
        display.clear()

    elif button_a.was_pressed():
        radio.send("dot")
    elif button_b.was_pressed():
        radio.send("line")
    elif incoming == "line":
        display.show("---")
        sleep(1000)
        display.clear()
