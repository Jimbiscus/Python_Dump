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
    
    def __init__(self, name, job, hp, atk, res, gold, luck, crit):
        self.name = name
        self.job = job
        self.hp = hp
        self.atk = atk
        self.res = res
        self.gold = gold
        self.luck = luck

    def full_name(self):
        return f"{self.name} the {self.job}"

    def level_up(self):
        self.hp = int(self.hp * 1.05)
        self.atk = int(self.atk + 3)
        self.res = int(self.res + 1)
        self.gold = int(self.gold + 100)

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
        randomChance = randint(1,10)
        if self.luck >= randomChance:
            self.atk *= 2
            print(f"---------------- Critique pour {self.name}")
            self.crit = True
        else:
            pass
        return self.atk
    def attack(self, opponent):
      print(f"You are attacking {opponent.full_name()}")

      while Hero.hp > 0 and Heel.hp > 0:
        # WHERE THE FIGHT TAKES PLACE

        # The Hero attacks
        dprintf(f"{Hero.name} attacks !")
        Hero.calculate_critical()
      
        HeroAtkValue = Hero.atk - Heel.res
        Heel.hp -= HeroAtkValue

        # What is shown during combat
        
        dprintf(f"{Heel.name} takes {HeroAtkValue} DMG ! HP : {Heel.hp}")
        #
        if Hero.crit == True:
            Hero.crit == False
            Hero.atk //= 2
            

        # The Heel attacks
        dprintf(f"{Heel.name} attacks !")
        Heel.calculate_critical()
        
        HeelAtkValue = Heel.atk - Hero.res
        Hero.hp -= HeelAtkValue
        # What is shown during combat
        
        dprintf(f"{Hero.name} takes {HeelAtkValue} DMG ! HP : {Hero.hp}")
        #
        if Heel.crit == True:
            Heel.crit = False
            Heel.atk //= 2
      if Hero.hp <= 0:
        Hero.hp = 0
        dprint("You lost !")
      elif Heel.hp <=0:
        Heel.hp = 0
        dprint("You won !")



characters = [
    Aventureer("Jolan", "Necromancer", 90, 11, 2, 100, 2, crit=False),
    Aventureer("Allan", "Rogue", 100, 12, 1, 100, 1, crit=False),
    Aventureer("Marcus", "Barbarian", 1100, 9, 3, 100, 5, crit=False),
    Aventureer("Arnaud", "Bard", 50, 9, 3, 100, 7, crit=False),
    Aventureer("C", "Crit Maker", 1100, 5, 0, 100, 5, crit=False)
]

def choose_character():
    Hero = input("Choose your Hero : ")
    for character in characters:
        if character.name == Hero:
            return character

def choose_ennemy():
    Heel = input("Choose your Nemesis : ")
    for character in characters:
        if character.name == Heel:
            return character

def show_chars():
    print(":-=-=-=-=-:")
    for character in characters:
        print(f"  {character.name}")
    print(":-=-=-=-=-:")


show_chars()
Hero = choose_character()
Heel = choose_ennemy()
print(Hero.luck)

# Show the stats
Hero.show_stats()

# Attack an ennemy
Hero.attack(Heel)
