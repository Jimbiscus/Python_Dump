from microbit import *
import radio

radio.on()
radio.config(channel=22)
value = 0
while True:

    incoming = radio.receive()
    if incoming == "Temperature":
        display.scroll(temperature())
    elif incoming == "Lumiere":
        display.scroll(display.read_light_level())
    if button_a.was_pressed():
        radio.send("Temperature")
    if button_b.was_pressed():
        radio.send("Lumiere")

#chaque fois que j'appuie sur A j'envoie un message à l'autre, chaque fois qu'il appuie sur A il m'envoie un msg# Ecrit ton programme ici ;-)
