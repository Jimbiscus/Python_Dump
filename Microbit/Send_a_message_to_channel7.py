from microbit import *
import radio

radio.on()
n = 7
radio.config(channel=n)

while True:
    radio.send("Tupac is alive")
    sleep(400)
    incoming = radio.receive()
