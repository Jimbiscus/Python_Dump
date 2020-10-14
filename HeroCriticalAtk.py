from random import randint
luck = 7

def HeroCriticalAtk():
    heroCritical = 1
    randomChance = randint(1,10)
    if luck not in range(randomChance):
        heroCritical = 2
        print("Critique !")
    else:
        heroCritical = 1
        print("Pas critique")
while True:
    HeroCriticalAtk()
