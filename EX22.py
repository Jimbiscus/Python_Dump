
mylist = []
while len(mylist) < 5:
    newinput = int(input("Entrez un nombre : "))
    if newinput > 10 or newinput < 1:
        print("ce nombre n'est pas accepté")
    else:
        mylist.append(newinput)
if len(mylist) == 5:
    print(mylist)

