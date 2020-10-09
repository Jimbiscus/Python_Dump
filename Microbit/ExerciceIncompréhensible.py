from microbit import *
import radio

radio.on()
radio.config(channel=22)
value = 0
while True:
    display.show(str(value))
    incoming = radio.receive()
    if incoming == "+":
        display.show(str(value))
        value += 1
        sleep(333)
        display.show(str(value))
    elif incoming == "-":
        display.show(str(value))
        value -= 1
        sleep(333)
        display.show(str(value))
    if button_a.was_pressed():
        radio.send("+")
    if button_b.was_pressed():
        radio.send("-")

#chaque fois que j'appuie sur A j'envoie un message à l'autre, chaque fois qu'il appuie sur A il m'envoie un msg
