from random import choice

alphabetTable = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

character = choice(alphabetTable)
answer = input("Tapez la lettre '" + character + "'. ")

while (answer != character):
    answer = input("Tapez la lettre '" + character + "'. ")
