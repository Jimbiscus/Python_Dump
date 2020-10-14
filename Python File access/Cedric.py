fichier = open("file_4.txt", "r")
numbers = fichier.readlines()
fichier.close()
fichier = open("file_7somme.txt", "w")

somme = 0
result = ""
for line in numbers:
    print(line.split(" "))
    for chiffre in line.split(" ")[:-1]:
        somme += int(chiffre)
    result += str(somme) + "-"
    somme = 0
fichier.write(result[:-1])

fichier.close()
