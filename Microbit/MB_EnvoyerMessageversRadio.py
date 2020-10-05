import serial

port = "COM4"
conn = serial.Serial(port, 115200)

def get_data_from_microbit():
    msg = conn.readline()
    if msg:
        msg = msg.decode()
        return msg.strip()


while True:
    result = get_data_from_microbit()
    if result:
        print(result)
        sleep(100)
