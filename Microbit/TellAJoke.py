import requests
import serial

port = "COM5"
conn = serial.Serial(port, 115200)

while True:
    input("Press enter to flip a coin!")
    r = requests.get("http://flipacoinapi.com/txt")
    result = r.text
    result_bytes = (result + ",").encode()
    conn.write(result_bytes)


