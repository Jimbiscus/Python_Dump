# mylist = []


# while 0 not in mylist:
#     newinput = input("Entrez un nombre : ")
#     newinput = int(newinput)
#     mylist.append(newinput)
# else:
#     print(min(mylist))
#     print(max(mylist))

number = input("n: ")
number = int(number)

pg = number
pp = number

while number != 0:
    number = input("n: ")
    number = int(number)

    if number > pg:
        pg = number
    elif number < pp:
        pp = number

print("min: " + str(pp))
print("max: " + str(pg))
