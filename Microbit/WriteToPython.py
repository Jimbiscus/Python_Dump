from microbit import *



while True:
    if button_a.was_pressed():
        print("flipCoin")
    msg = uart.read()
    if msg:
        if msg == b'Tails':
            display.show(Image.SKULL)
        elif msg == b'Heads':
            display.show(Image.TSHIRT)

#     if button_a.was_pressed():
#         print("a")
#         display.show("A")
#         sleep(500)
#         display.clear()
#     elif button_b.was_pressed():
#         print("b")
#         display.show("B")
#         sleep(500)
#         display.clear()
#     elif button_a.was_pressed() and button_b.was_pressed:
#         print("WTF ??")
#         display.show("C")
#         sleep(500)
#         display.clear()
