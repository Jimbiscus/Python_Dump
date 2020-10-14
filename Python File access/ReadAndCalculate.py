f = open("file_4.txt", "r")
l = []
g = open("resultats.txt", "w")
pair = 0
impair = 0
for line in f.readlines():
    splitted_line = line.split(" ")
    l.append(splitted_line[:-1])
    for n in l:
        result = int(n[0]) + int(n[1]) + int(n[2]) + int(n[3]) + int(n[4])
    print(str(n[0]) +"+" + str(n[1]) +"+" + str(n[2]) +"+" + str(n[3]) + "+" + str(n[4]) + " = " + str(result))
    if result % 2 == 0:
        print("Pair !")
        pair += 1
        g.write(str(result) + "\n")
    else:
        print("Impair !")
        impair += 1
        g.write(str(result) + "\n")

print("Chiffres impairs : " + str(impair))
print("Chiffres pairs : " + str(pair))
f.close()
g.close()
