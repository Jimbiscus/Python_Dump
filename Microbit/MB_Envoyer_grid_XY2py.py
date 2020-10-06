import serial

port = "COM5"
conn = serial.Serial(port, 115200)

player1 = 1
player2 = 2
players = [player1, player2]
def ask_position():
    x = int(input("x: "))
    y = int(input("y: "))
#     intensity = int(input("intensity: "))

    data = str(x) + str(y)
    return data

while True:
    for player in players:
        print("Player " + str(player) + " : ")
        position = ask_position()
        data = position + str(player)
        conn.write(data.encode())
        incoming = conn.readline()
        if incoming.decode().strip() == "OK":
            print("Pixel bien placé")
        else:
            print("Erreur")

