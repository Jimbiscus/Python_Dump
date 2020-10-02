from fighters import fighter1, fighter2
from random import choice

print(fighter1)
print(fighter2)



while fighter1["hp"] > 0 and fighter2["hp"] > 0:
    attacks = ["poing", "pied", "morsure"]
    attacks2 = ["poing", "pied", "morsure"]
    attack_name = choice(attacks)
    attack_name2 = choice(attacks2)

    attack = fighter1[attack_name]  # On assigne a la clé de l'attaque la valeur contenue dans la librairie
    attack -= fighter2["defense"]
    attack2 = fighter2[attack_name2]
    attack2 -= fighter2["defense"]
    if attack2 < 0:
        attack2 = 0

#   attack = max(attack, 0)
    if attack < 0:
        attack = 0
    fighter2["hp"] -= attack
    fighter1["hp"] -= attack2

    if fighter1["hp"] < 0:
        fighter1["hp"] = 0
    if fighter2["hp"] < 0:
        fighter2["hp"] = 0
    print(fighter1["nom"] + " a utilisé " + attack_name + "! HP Restant à l'ennemi : " + str((fighter2["hp"])))
    print(fighter2["nom"] + " a utilisé " + attack_name2 + "! HP Restant à l'ennemi : " + str((fighter1["hp"])))

if fighter1["hp"] == 0 and fighter2["hp"] == 0:
    print("Double K.O !")
elif fighter2["hp"] == 0:
    print(fighter1["nom"] + " a gagné le combat !")
else:
    print(fighter2["nom"] + " a gagné le combat !")
