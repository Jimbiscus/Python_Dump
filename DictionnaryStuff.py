from random import randint

runners = {
"Jimmy": 0,
"Jimbert": 0,
"Jimbus": 0}


win = False

while win == False:

    for key in runners:
        pointdeCote = randint(0, 2)
        if pointdeCote == 2:
            runners[key] += (randint(2,5) / 2)
            print("Point de coté pour " + key)
            print(str(key) +" : " + str(runners[key]))

        else:
            runners[key] += randint(2,5)
            print(str(key) + " : " +  str(runners[key]))

        if runners[key] >= 100:
            print("Le gagnant est : " + key)
            win = True
            break
