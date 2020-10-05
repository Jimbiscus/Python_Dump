import serial

port = "COM4"
conn = serial.Serial(port, 115200)



while True:
    print("1. Ecrire : ")
    print("2. Lire : ")
    choice = input("")
    if choice == "1":
        channel = input("channel : ")
        msg = input("Message : ")
        if int(channel) < 10:
            channel = "0" + channel
        msg = msg.encode()
        conn.write(msg)
    else:
        while True:
            data = conn.readline()
            if data:
                print(data.decode())
