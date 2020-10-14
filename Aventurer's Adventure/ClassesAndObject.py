from random import randint
import time
import sys

# Display char by char functions, a normal a fast one with a line break between each print
def dprint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
    sys.stdout.write("\n")

def dprintf(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
    sys.stdout.write("\n")


class Aventureer:
    # Removed the crit bool cause I think it's useless, you can deal with it differently
    def __init__(self, name, job, hp, atk, res, gold, luck):
        self.name = name
        self.job  = job
        self.hp   = hp
        self.atk  = atk
        self.res  = res
        self.gold = gold
        self.luck = luck
        # Would make sense to keep track of the level
        # Since every Aventureer starts at level 1, we can assign it by default without
        # passing it as parameter to the constructor
        self.level = 1

    def full_name(self):
        return f"{self.name} the {self.job}"

    def level_up(self):
        self.hp   = int(self.hp * 1.05)
        self.atk  = int(self.atk + 3)
        self.res  = int(self.res + 1)
        self.gold = int(self.gold + 100)
        # Now here we can increment his level
        self.level += 1

    def show_stats(self):
        dprintf(":-=-=-=-=-=-=-=-=-=-=-=-=-=-:")
        dprintf(f"Stats of {self.full_name()}")
        dprintf(":-=-=-=-=-=-=-=-=-=-=-=-=-=-:" + "")
        dprintf("hp : " + str(self.hp) + "")
        dprintf("atk : " + str(self.atk) + "")
        dprintf("def : " + str(self.res) + "")
        dprintf("gold : " + str(self.gold) + "")
        dprintf("luck : " + str(self.luck) + "")
        dprintf(":-=-=-=-=-=-=-=-=-=-=-=-=-=-:")

    def calculate_critical(self):
        random_chance = randint(1, 10)

        if self.luck >= random_chance:
            self.atk *= 2
            print(f"---------------- Critique pour {self.name}")
        else:
            return
        return self.atk

    def attack(self, opponent):
      print(f"You are attacking {opponent.full_name()}")

      while self.hp > 0 and opponent.hp > 0:
        # WHERE THE FIGHT TAKES PLACE
        dprintf(f"{self.name} attacks !")
        
        # Calculate if the next hit will be critical, since calculate_critical modify the self.atk itself
        self.calculate_critical()
      
        # Modified but left as a comment so you can compare, but think, you don't need that
        hero_attack_dmg = self.atk - opponent.res
        #HeroAtkValue = self.atk - opponent.res
        opponent.hp -= hero_attack_dmg

        # What is shown during combat
        
        dprintf(f"{opponent.name} takes {hero_attack_dmg} DMG ! HP : {opponent.hp}")
      
        # Now it's the turn of the opponent
        dprintf(f"{opponent.name} attacks !")
        
        opponent.calculate_critical()
        
        heel_attack_dmg = opponent.atk - self.res
        self.hp -= heel_attack_dmg
        
        # What is shown during combat
        dprintf(f"{self.name} takes {heel_attack_dmg} DMG ! HP : {self.hp}")
      if self.hp <= 0:
        self.hp = 0
        dprint("You lost !")
      elif opponent.hp <=0:
        self.hp = 0
        dprint("You won !")

# Removed crit from here, but does that make sense when reading it ? Creating a new
# character with a boolean flag for critical attacks ? 
characters = [
    Aventureer("Jolan", "Necromancer", 9000, 11, 2, 100, 2),
    Aventureer("Allan", "Rogue", 100, 12, 1, 100, 1),
    Aventureer("Marcus", "Barbarian", 11000, 9, 3, 100, 5),
    Aventureer("Arnaud", "Bard", 50, 9, 3, 100, 7),
    Aventureer("C", "Crit Maker", 1100, 5, 0, 100, 5)
]

def choose_character():
    hero = input("Choose your Hero : ")
    for character in characters:
        if character.name == hero:
            return character

def choose_ennemy():
    heel = input("Choose your Nemesis : ")
    for character in characters:
        if character.name == heel:
            return character

def show_chars():
    print(":-=-=-=-=-:")
    for character in characters:
        print(f"  {character.name}")
    print(":-=-=-=-=-:")


show_chars()
hero = choose_character()
heel = choose_ennemy()
print(hero.luck)

# Show the stats
hero.show_stats()

# Attack an ennemy
hero.attack(heel)