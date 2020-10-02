# Ecrit ton programme ici ;-)
from random import randint

def dice_simulation(faces=6):
    dice = randint(1, faces)
    return dice

print(dice_simulation(450))
print(dice_simulation())



def dices_simulation(dice_number, faces=6):
    result = 0

    for n in range(dice_number):
        dice = randint(1, faces)
        result += dice
    return result

print(dices_simulation(3))

