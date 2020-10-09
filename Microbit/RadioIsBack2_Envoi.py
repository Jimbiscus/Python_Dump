# SCRIPT D ENVOI

from microbit import *
import radio

radio.config(channel=22)
radio_status = False
emission_status = True

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
        incoming = radio.receive()
        if incoming:
            if incoming == "OK":
                display.scroll(incoming)
                emission_status = True
            if emission_status == True:
                radio.send("Ok")
