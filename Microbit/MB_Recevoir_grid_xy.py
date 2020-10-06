from microbit import *

def set_pixel(data):
    x = chr(data[0])
    x = int(x)

    y = chr(data[1])
    y = int(y)

    intensity = chr(data[2])
    intensity = int(intensity)

    if display.get_pixel(x, y) > 0:
        return "NOT OK"
    else:
        display.set_pixel(x, y, intensity)
        return "OK"

while True:
    data = uart.read()
    if data:
        result = set_pixel(data)
        print(result)

