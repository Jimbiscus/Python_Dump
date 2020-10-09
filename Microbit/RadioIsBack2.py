# SCRIPT DE RECEPTION

from microbit import *
import radio

radio.config(channel=22)
radio_status = False
emission_status = False
while True:
    if button_a.was_pressed():
        if radio_status == False:
            radio.on()
            display.show(Image.YES)
            radio_status = True
            sleep(300)
            display.clear()
        else:
            radio.off()
            display.show(Image.NO)
            radio_status = False
            sleep(300)
            display.clear()

    if radio_status == True:
        if emission_status == False:
            incoming = radio.receive()
        if incoming:
            if incoming == "OK":
                emission_status = False
            if emission_status == True:
                radio.send("OK")
