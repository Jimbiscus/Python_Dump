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
numbers = [number]

while number != 0:
    number = input("n: ")
    number = int(number)
    numbers.append(number)

print("min :" + str(min(numbers)))
print("max :" + str(max(numbers)))
