import serial

port = "COM4"
conn = serial.Serial(port, 115200)

while True:
    msg = input("Message : ")
    msg = msg.encode()
    msg = conn.write(msg)
