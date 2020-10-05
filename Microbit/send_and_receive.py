from microbit import *
import radio

radio.on()
n = 7
radio.config(channel=n)

while True:
    radio.send("Marc")
    sleep(400)
    incoming = radio.receive()
    while True:
        for n in range(1, 20):
            radio.config(channel=n)
            msg = radio.receive()
            if msg:
                print(msg)
                sleep(500)

