from microbit import *
import radio

radio.config(channel=22)
radio_status = False
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
            display.scroll(incoming)
        if button_b.was_pressed():
            display.show(Image.ARROW_N)
            radio.send("Hello it's BIG MARCO")
            sleep(500)
            display.clear()
