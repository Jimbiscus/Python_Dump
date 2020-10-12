# Write your code here :-)
from random import randint
runners = {
"Didier": 5,
"Arouf": 5,
"Michel": 5}

win = False
while win == False:
    for key in runners:
        runners[key] += randint(2, 5)
        print(key + ": " + str(runners[key]))

        if runners[key] >= 100:
            print("Le gagnant est: " + key)
            win = True
            break
