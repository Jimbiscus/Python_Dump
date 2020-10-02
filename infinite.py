from random import randint


while True:
    number = randint(0, 100)
    print(number)
    if number == 0:
        break
# Le résultat s'affiche lorsque le randint génère un 0
print("Tadaaaam !")
