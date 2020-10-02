a=6
b=9

print (not(a > b and a == 9 or b < 10))
#Priorités des opérations : NOT, AND et puis OR

if a < 10:
    print(str(a) + " est plus petit que 10 !")

if b == 9:
    print( "b est égal à 9 !")

if "Jimbo":
    print("Une chaine de caractères est toujours vraie si elle n'est pas vide !")

if a > b:
    print("a est plus grand que a !")
else:
    print("b est plus grand que a !")


# ET SI ON A PLUSIEURS CONDITIONS A TESTER

if a < b:
    print(str(a) + " plus petit que " + str (b))
elif a == b:
    print(str(a) + " est égal à " + str(b))
else:
    print(str(a) + " plus grand que " + str(b))



