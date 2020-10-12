from random import choice

alphabetTable = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def keepPlaying():
    keepPlaying = input("Souhaitez vous continuer ? O/N ")
    if keepPlaying in ("o","O"):
        tries = 0
        alphabetGame()
    else:
        print("Bye!")

def alphabetGame():
    character = choice(alphabetTable)
    wrongTries = 0
    tries = 0
    while tries < 5:
            answer = input("Tapez la lettre '" + character + "'. ")
            if answer != character:
                wrongTries += 1

            else:
                character = choice(alphabetTable)
            tries +=1
    if tries == 5:
        print("Vous avez foiré " + str(wrongTries) + " fois")
        keepPlaying()

alphabetGame()

