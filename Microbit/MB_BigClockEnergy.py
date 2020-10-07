from microbit import *
n = 0
while True:
    display.show(Image.ALL_CLOCKS[n%12])
    while button_b.was_pressed():
        n+=1
    while button_a.was_pressed():
        n-=1


