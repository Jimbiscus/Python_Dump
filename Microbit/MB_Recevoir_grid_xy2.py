from microbit import *

def set_pixel(data):
    x = chr(data[0])
    x = int(x)

    y = chr(data[1])
    y = int(y)

    player = chr(data[2])
    player = int(player)

    P1I = 9
    P2I = 5
    if player == 1:
        z = P1I
    else:
        z = P2I
    if display.get_pixel(x, y) > 0:
        return "NOT OK"
    else:
        display.set_pixel(x, y, z)
        return "OK"

while True:
    data = uart.read()
    if data:
        result = set_pixel(data)
        print(result)

