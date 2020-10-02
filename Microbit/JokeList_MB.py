from microbit import *
joketype = ["general", "knock-knock", "programming"]


index = 0
display.scroll(joketype[index],delay = 70)
while True:
    if button_a.was_pressed():
        index = (index + 1) % len(joketype)
        sendit = joketype[index]
        display.scroll(sendit,delay = 70)
        sleep(250)
    if button_b.was_pressed():
        print(sendit)
