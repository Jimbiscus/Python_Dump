f = open("recette.txt", "r")
recette = f.read()
eList = []
f.close()

lines = recette.split("\n")
lines = lines.split(" ")
#remove unnecessary characters
removable_character = ["(", ")", ".", "'","-", ",",":","Ã©","Ã¨","Ã\xa0"]

for index in range(len(lines)):
    word = lines[index]
    for character in removable_character:
        word = word.replace(character, "")
    lines[index] = word

