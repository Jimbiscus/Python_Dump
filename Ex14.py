from random import randint

mob_hp = 30

while mob_hp > 0:
    attack = randint(5, 10)
    mob_hp = mob_hp - attack
    print("Le monstre subit un attaque de " + str(attack) + " HP, il lui reste " + str(mob_hp) + " HP.")

print("Le monstre est mort")
