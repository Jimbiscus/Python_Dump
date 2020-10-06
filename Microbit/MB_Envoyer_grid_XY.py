import serial

port = "COM5"
conn = serial.Serial(port, 115200)

def ask_position():
    x = int(input("x: "))
    y = int(input("y: "))
    intensity = int(input("intensity: "))

    data = str(x) + str(y) + str(intensity)
    return data

while True:

    position = ask_position()
    conn.write(position.encode())

    incoming = conn.readline()
    if incoming.decode().strip() == "OK":
        print("Pixel bien placé")
    else:
        print("Erreur")

