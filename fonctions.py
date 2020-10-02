from random import randint
from time import sleep

def bingo():
    g = randint(1,10)
    print(g)
    h = int(input("Entrez un nombre"))

    if g == h:
        print("Gagné !")
    elif g > h:
        print("Votre nombre est trop petit !")
    else:
        print("Votre nombre est trop grand !")


def Jimbo():
    a = int(input("Entrez un nombre : "))
    b = int(input("Entrez un nombre : "))
    c = a * b
    print(c)

def hello():
    print("Hello World!")
    print("~~~~~~~~~~~~~")

def countdown():
    for i in range(10,-1,-1):
        print(i)
        sleep(1)

bingo()

