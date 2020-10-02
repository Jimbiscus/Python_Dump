# Ecrit ton programme ici ;-)
#On importe la fonction randint depuis une librairie
from random import randint

d6 = randint(1, 6)
print(d6)

a = (9)
b = input("Entrez une valeur pour b : ")

if a == int(b):
    print("gagné !")
else:
    print("perdu !")

print("Niveau 2!")

c = randint (1, 10)

print(c)
if b == c:
    print("Bien joué !")
else:
    print("Perdu!")
