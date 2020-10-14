f = open("questions.txt", "r")
g = open("reponses.txt", "a")
for line in f.readlines():
    if line[-1] == "\n":
        line = line[:-1]
        print(line)
        entry = input(" : ")
        g.write(f"{line} {entry}\n" )


g.close()
f.close()
