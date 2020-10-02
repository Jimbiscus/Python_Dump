# my_list = ["Jean", "Jeanne", "Jimbo", "Jimbus", "Jimbert", "Jimmothy"]
# my_list.append("Jimbiscus")
# print(my_list)
# index = int(input("Veuillez entrez un nombre : "))

# print(my_list[index])

# ajout = input("Veuillez rajouter une valeur à la liste ")
# my_list.append(ajout)
# print(my_list)

# my_list.remove("Jean")
# print(my_list)
# del my_list[2]
# print(my_list)

# nom = my_list.pop(0)
# print(nom)
# print(my_list)



# my_list[0]="PYTHON"
# print(my_list)

#### Petits exemples d'opérations sur une liste
a = 1
print(a)
l = [1, 2, 3, 4, 5, 3]
del(l[2])
a = l.pop(-1) # enleve la valeur a l'index 1 (peut se stocker dans une variable)
l.remove(5) # enleve la première itération de 5
l.insert(3, 8) #insérer un 8 a l'index 3
b = l.index(4, 2) #A partir de l'index 2, récupérer la valeur de l'index
print(b)
print(l)
print(a)

d = 6
n = 8
l1 = [4, 5, 6, 8, 8, 8, 8, 4, 9, 0]
while n in l1:
    l1.remove(n)
e = l1[2:6] # de l'index 2 au 6
f = l1[2:6:2] #de l'index 2 au 6 par pas de 2dd

print(e)

print(l1)


