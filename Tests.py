from random import randint
import time
import sys


class Aventureer:
    def __init__(self, name, job, hp, atk, res, gold):
        self.name = name
        self.job = job
        self.hp = hp
        self.atk = atk
        self.res = res
        self.gold = gold

    def full_name(self):
        return f"{self.name} the {self.job}"

    def level_up(self):
        self.hp = int(self.hp * 1.05)
        self.atk = int(self.atk + 3)
        self.res = int(self.res + 1)
        self.gold = int(self.gold + 100)

    def show_stats(self):
        print(f"Stats of {self.full_name()}")
        print(":-=-=-=-=-=-=-=-=-=-=-=-=-=-:")
        print("hp : " + str(self.hp))
        print("atk : " + str(self.atk))
        print("def : " + str(self.res))
        print("gold : " + str(self.gold))
        print(":-=-=-=-=-=-=-=-=-=-=-=-=-=-:")

    def attack(self, opponent):
      print(f"You are attacking {opponent.full_name()}")

      battle_issue = randint(0, 1)

      if battle_issue == 1:
        print("You won !")
      else:
        print("You lost !")



characters = [
    Aventureer("Jolan", "Necromancer", 100, 50, 20, 100),
    Aventureer("Allan", "Rogue", 100, 50, 20, 100),
    Aventureer("Marcus", "Barbarian", 100, 50, 20, 100),
    Aventureer("Arnaud", "Bard", 100, 50, 20, 100),
    Aventureer("Bastien", "Wizard", 100, 50, 20, 100),
]

def choose_character(character_name):
        if Aven == Hero:
            return character
def show_characters():
    print("xxxxxx")
    for character in characters:
        print(character.name)
    print("xxxxx")


show_characters()

Hero = choose_character(input("Choose your Hero : "))
# Heel = choose_character(input("Choose your Nemesis : "))

# Show the stats
Hero.show_stats()

# Attack an ennemy
Hero.attack(Heel)
