from random import randint
import time
import sys
heelCritical = 1
heroCritical = 1
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
    def __init__(self, name, job, hp, atk, res, gold, luck):
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


    def attack(self, opponent):
      print(f"You are attacking {opponent.full_name()}")

      while Hero.hp > 0 and Heel.hp > 0:
        # WHERE THE FIGHT TAKES PLACE
        # The Hero attacks


        HeroAtkValue = Hero.atk - Heel.res
        HeroCriticalAtk()
        if heroCritical > 1:
            HeroAtkValue *= heroCritical
            print("Critique !")
        else:
            HeroAtkValue *= heroCritical
            print("Nope !")
        Heel.hp -= HeroAtkValue
        ###############################
        dprintf(f"{Hero.name} attacks !")
        dprintf(f"{Heel.name} takes {HeroAtkValue} DMG ! HP : {Heel.hp}")
        ################################
        # The Heel attacks

        HeelAtkValue = Heel.atk - Hero.res
        HeelCriticalAtk()
        if heelCritical > 1:
            HeelAtkValue *= heelCritical
            print("Critique !")
        elif heelCritical == 1:
            HeelAtkValue *= heelCritical
            print("Nope !")
        Hero.hp -= HeelAtkValue
        dprintf(f"{Heel.name} attacks !")
        dprintf(f"{Hero.name} takes {HeelAtkValue} DMG ! HP : {Hero.hp}")
      if Hero.hp <= 0:
        dprint("You lost !")
      elif Heel.hp <=0:
        dprintf("You won !")



characters = [
    Aventureer("Jolan", "Necromancer", 90, 11, 2, 100, 2),
    Aventureer("Allan", "Rogue", 100, 12, 1, 100, 1),
    Aventureer("Marcus", "Barbarian", 110, 9, 3, 100, 0),
    Aventureer("Arnaud", "Bard", 50, 9, 3, 100, 7 ),
    Aventureer("Bastien", "Wizard", 110, 5, 0, 100, 6),
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

def HeroCriticalAtk():
    heroCritical = 1
    randomChance = randint(1,10)
    if Hero.luck not in range(randomChance):
        heroCritical = 2
        return heroCritical
    else:
        heroCritical = 1
        return heroCritical

def HeelCriticalAtk():
    heelCritical = 1
    randomChance = randint(1,10)
    if Heel.luck not in range(randomChance):
        heelCritical = 2
        return heelCritical
    else:
        heelCritical = 1
        return heelCritical

show_chars()
Hero = choose_character()
Heel = choose_ennemy()

# Show the stats
Hero.show_stats()

# Attack an ennemy
Hero.attack(Heel)
