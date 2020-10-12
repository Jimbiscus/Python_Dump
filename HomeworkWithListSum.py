
l = []
somme = 0
numbersStored = 0
while somme <= 20:
    entry = input("Entrez un nombre : ")
    entry = int(entry)
    somme += entry
    l.append(entry)
    numbersStored += 1
else:
    l.sort()
    print("plus petit nombre : " + str(l[0]))
    print("plus grand nombre : " + str(l[-1]))
    print("vous avez entré " + str(numbersStored) + " nombres.")
