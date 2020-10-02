from random import randint

nbr = randint(1, 10)
print(nbr)
# On demande a l'utilisateur de rentrer sa réponse, qui est ensuite convertie en nombre entier
user_nbr = input("Donne un nombre entre 1 et 10 : ")
user_nbr = int(user_nbr)

if user_nbr == nbr:
    print("Bravo !!!")
elif user_nbr < nbr:
    print("Ton nombre est trop petit !")
elif:
    print("Ton nombre est trop grand !")
    user_nbr = input("Réessaye : ")
if user_nbr == nbr:
            print("Bravo !!!")
else:
 if user_nbr < nbr:
                print("Ton nombre est trop petit !#2")
else:
            print("Ton nombre est trop grand !#2")
        user_nbr = input("Réessaye : #2")
        if user_nbr == nbr:
            print("Bravo !!!")
        else:
            print("Le nombre était" + str(nbr))

