from microbit import *
import radio
from random import randint

ranchan = randint(0, 7)
radio.on()
radio.config(channel=ranchan)
while True:
    outgoing = radio.send()
    if button_a.was_pressed():

    incoming = radio.receive()
    if incoming:
        try:
            image = Image(incoming)
            display.show(image)
            sleep(2000)
        except:
            display.scroll(incoming)
