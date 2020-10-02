# mylist = []


# while "end" not in mylist:
    # newinput = input("Entrez un mot : ")
    # mylist.append(newinput)

# mylist.pop(-1)
# mylist.reverse()
# print(mylist)

words = []
word = input("Mot: ")

while word != "end":
    words.append(word)
    word = input("Mot: ")

for word in words[::-1]:
    print(word)
