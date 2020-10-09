from microbit import *
import radio
radio.on()
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","?"]
n = 0

while True:
    incoming = radio.receive()
    display.show(alpha[n%27])
    if button_a.is_pressed():
        n += 1
        display.show(alpha[n%27])
        sleep(333)
    if button_b.was_pressed():
        display.show(Image.ARROW_N)
        sleep(333)
        display.clear()
        radio.send(alpha[n])
    if incoming:
        display.scroll(incoming)

