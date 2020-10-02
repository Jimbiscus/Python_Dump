import serial
import requests
import json

# heads = ["00500:","05050:","50505:","05050:","00500"]
# tails = ["00500:","05050:","50005:","05050:","00500"]

port = "COM5"
conn = serial.Serial(port, 115200)

r = requests.get("https://official-joke-api.appspot.com/random_joke")

joke = json.loads(r.text)


msg = joke["setup"]



print(msg)


conn.write(msg.encode())

input("Press Enter to load punchline.")
msg = joke["punchline"]
print(msg)


