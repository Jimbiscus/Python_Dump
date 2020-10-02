from random import randint
liste1 = [100, 22, 3, 4, 4, 5, 204, 4201]

def supersomme(n):
    total = 0
    for n in liste1:
        total += n
    return total

print(supersomme(liste1))

def dice_simulation(faces=6):
    dice = randint(1, faces)
    return dice

print(dice_simulation(20))
