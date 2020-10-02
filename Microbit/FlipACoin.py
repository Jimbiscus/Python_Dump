import requests
import serial

port = "COM3"
conn = serial.Serial(port, 115200)


while True:
    data = conn.readline()

    if data:
        data = data.decode().strip()
        if data == "flipCoin":
            print("Press Enter to flip a coin : ")
            if data:
                r = requests.get("http://flipacoinapi.com/txt")
                result = r.text
                msg = result.encode()
                msg = msg.strip()
                print(msg)
                conn.write(msg)





#     msg = conn.readline()
#     if msg:
#         msg = msg.decode()
#         msg = msg.strip()
#         input("Press enter to flip a coin!")
#         msg = conn.readline()
#         if msg:
#             msg = msg.decode()
#             msg = msg.strip()
#         r = requests.get("http://flipacoinapi.com/txt")
#         result = r.text
#         result_bytes = (result).encode()
#         conn.write(result_bytes)
#         print(result)




