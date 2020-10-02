import requests
import json
import serial
from random import randint


port = "COM3"
conn = serial.Serial(port, 115200)

while True:
    data = conn.readline().strip().decode()
    print(data)
    r = requests.get("https://official-joke-api.appspot.com/jokes/" + str(data) + "/random")
    joke = json.loads(r.text)
    print(joke[0])
