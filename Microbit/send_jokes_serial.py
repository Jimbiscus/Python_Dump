import serial
import requests
import json

port = "COM5"
conn = serial.Serial(port, 115200)





while True:
    r = requests.get("https://official-joke-api.appspot.com/random_joke")
    joke = json.loads(r.text)
    input("#####Press Enter to tell joke.######")
    if input:
        msg = joke["setup"]
        print(msg)
        conn.write(msg.encode())
        if input:
            input("#####Press Enter to tell punchline.######")
            msg = joke["punchline"]
            print(msg)
            conn.write(msg.encode())
