# Ecrit ton programme ici ;-)
# Instruction d'entrée, saisie clavier.
hero_name = input("Entrez le nom de votre personnage : ")
print ("Bienvenue, " + hero_name + ".")
# L'input renvoie toujours une variable de type string
# voici comment transformer une chaine de caractères en nombre entier
a = "11"
a = int(a)

#les types de bases de Python sont les suivants :
#int pour les nombres entier
#float pour les nombres à virgule
#str pour les chaînes de caractère
#bool pour les variables booléennes

age = input("Entrez votre age : ")
age = int(age)
print("Le double de votre est " + str(age * 2))
