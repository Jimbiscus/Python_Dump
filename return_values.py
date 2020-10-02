from random import randint

def dice():
    dice = randint(1, 6)
    return dice

def one():
    return 1


def dico():
    fighter = {
        "key1": "value1",
        "key2": "value2"
    }
    return fighter

d = dico()["key2"]

print(d)
print(dico())

########################################################

def modulo():
    rep = int(input("Entrez un nombre : "))
    mod = rep % 2
    if mod == 0:
        return ("Le reste est : " + str(mod) + ". Pair ! #" + str(i))
    else:
        return ("Le reste est : " + str(mod) + ". Impair ! #" + str(i))

for i in range(1, 11):
    print(modulo())


