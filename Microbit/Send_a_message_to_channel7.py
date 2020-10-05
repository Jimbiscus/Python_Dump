from microbit import *
import radio

radio.on()
radio.config(channel=7)

while True:
    radio.send("Coucou")
    sleep(400)
