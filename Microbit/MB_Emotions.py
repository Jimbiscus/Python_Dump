from microbit import *
import radio
n = 0
emotions = [Image.HAPPY, Image.SAD, Image.SKULL]

radio.on()
radio.config(channel=44)




while True:
    incoming = radio.receive()
    if incoming:
        n = int(incoming)
        display.show(emotions[n % len(emotions)])
    else:
        if button_a.was_pressed():
            n += 1
            display.show(emotions[n % len(emotions)])
        if button_b.was_pressed():
            n -= 1
            display.show(emotions[n % len(emotions)])
        elif accelerometer.was_gesture("shake"):
            radio.send(str(n))
            display.scroll("SENT !")
