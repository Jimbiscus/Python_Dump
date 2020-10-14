f = open("chien.txt", "w")
word = []
def inputLetter():

    entry = input("Entrez une lettre : ")
    if len(entry) != 1:
        print("Invalid Input")
    else:
        word.append(entry)
        f.write(entry + "\n")

def checkListLength():

    while len(word) != 6:
        inputLetter()
    if len(word) == 6:
        "".join(word)
        print("".join(word))
        f.write("".join(word))


checkListLength()

f.close()
