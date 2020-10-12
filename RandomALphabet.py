from random import randint

alphabetTable = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
randomLetter = randint(0,26)
chosenLetter = alphabetTable[randomLetter]
entry = 0
wrongTries = 0

def alphabetGame():
    entry = input("Entrez la lettre " + chosenLetter + " : ")

    if entry == chosenLetter:
        print("OK!")
    elif wrongTries < 5:
        wrongTries += 1
        alphabetGame()

alphabetGame()
