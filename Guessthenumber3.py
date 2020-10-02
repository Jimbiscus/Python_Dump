from random import randint

def bingo():
    print("Bingo !")

def entree():
    answer = int(input("Entrez un nombre entre 1 et 10 : "))
    return answer

user = entree()

nbr = randint(1, 10)
chance = 1


if user == nbr:
    bingo()
elif user < nbr:
    print("Ton nombre est trop petit.")
else:
    print("Ton nombre est trop grand.")


# Ecrit ton programme ici ;-)
