from microbit import *
import radio

radio.on()
radio.config(channel=1)

while True:
    pcwrite = uart.read()
    incoming = radio.receive()
    if pcwrite:
        ch = msg[:2]
        ch = int(channel)
        radio.config(channel=ch)
        display.scroll(pcwrite, delay=70)
        radio.send(pcwrite[2:])
    if incoming:
        print(incoming)
