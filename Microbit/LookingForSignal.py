from microbit import *
import radio
from random import randint

radio.on()
name = "MARIO"
found = False
while True:
    if not found:
        ranchan = randint(1, 2 /)
        radio.config(channel=ranchan)
        radio.send("free?")

        incoming = radio.receive()
        count = 0
        display.scroll(ranchan)
    while not incoming or count < 10:
        incoming = radio.receive()
        count += 1
        sleep(500)
    print(incoming)
    if incoming:
        if incoming == "yes":
            found = True
        elif incoming == "free?":
            if found:
                radio.send("no")
            else:
                radio.send("yes")
    else:
        radio.send(name)
        incoming = radio.receive()
        if incoming:
            display.scroll(incoming)

