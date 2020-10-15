from random import randint
from random import choice
import time
import sys

# Display char by char functions, a normal a fast one with a line break between each print
# by andrew-walker on stackoverflow
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
        time.sleep(0.005)
    sys.stdout.write("\n")
# this defines the color codes for the text
# by samat-jain on stackoverflow
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
# WIP
class Character:
    def __init__(self,name, hp, defaultHp, atk, res):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.res = res
        self.defaultHp = defaultHp

    def is_dead(self):
        if self.hp <= 0:
            print(f"{self.name} is dead")
            self.hp = self.defaultHp
class Aventureer(Character):
    # TODO : IMPLEMENT MAX XP VALUES PER LEVEL 
    def __init__(self, name, job, hp, defaultHp, atk, res, gold, luck,is_dead):
        self.name = name
        self.job  = job
        self.hp   = hp
        self.defaultHp = defaultHp
        self.atk  = atk
        self.defaultAtk = hp
        self.res  = res
        self.defaultRes = res
        self.gold = gold
        self.luck = luck
        self.is_dead = is_dead
        # Would make sense to keep track of the level
        # Since every Aventureer starts at level 1, we can assign it by default without
        # passing it as parameter to the constructor
        self.level = 1
    def heal(self):
        self.hp = self.defaultHp

    def full_name(self):
        return f"{self.name} the {self.job}"

    def level_up(self, levelAmount):
        self.hp   = int(self.defaultHp * 1.05)
        self.atk  = int(self.defaultAtk + 3)
        self.res  = int(self.defaultRes + 1)
        self.gold = int(self.gold + 100)
        # Now here we can increment his level
        self.level += levelAmount

    def show_stats(self):
        dprintf(":-=-=-=-=-=-=-=-=-=-=-=-=-=-:".center(75))
        dprintf(f"Stats of {self.full_name()}".center(75))
        dprintf(":-=-=-=-=-=-=-=-=-=-=-=-=-=-:".center(75))
        dprintf(f"LEVEL :  {self.level}".center(75))
        dprintf(f"HP : {self.hp} / {self.hp} ".center(75))
        dprintf(f"STR :  {self.atk}".center(75))
        dprintf(f"DEF :  {self.res} ".center(75))
        dprintf(f"Gold : {self.gold} ".center(75))
        dprintf(f"Luck : {self.luck} ".center(75))

        dprintf(":-=-=-=-=-=-=-=-=-=-=-=-=-=-:".center(75))

    def calculate_critical(self):
        random_chance = randint(1, 10)

        if self.luck >= random_chance:
            self.atk *= 1.5
            print(f"⚡ Critique pour {self.name}")
        else:
            return
        return round(self.atk, 1)

    def attack(self, opponent):
            print(f"{bcolors.WARNING}       You are attacking {opponent.full_name()}{bcolors.ENDC}".center(75))

            while self.hp > 0 and opponent.hp > 0:
                input(f"- - - - - - -".center(75))
                # WHERE THE FIGHT TAKES PLACE
                dprintf(f"{self.name} 🗡️ {opponent.name} ☠️")
                
                # Calculate if the next hit will be critical, since calculate_critical modify the self.atk itself
                self.calculate_critical()
            
                hero_attack_dmg = self.atk - opponent.res
                if hero_attack_dmg < 0:
                    hero_attack_dmg = 0
                opponent.hp -= hero_attack_dmg
                dprintf(f"{opponent.name} takes {hero_attack_dmg} DMG from {self.name} !")
                dprintf(f"☠️  {opponent.name} : {opponent.hp} / {opponent.defaultHp} HP")
                if opponent.hp > 0:
                        dprintf(f"{bcolors.FAIL}☠️  {opponent.name} 🗡️ {self.name}{bcolors.ENDC}")             
                        opponent.calculate_critical()                   
                        heel_attack_dmg = opponent.atk - self.res
                        if heel_attack_dmg < 0:
                            heel_attack_dmg = 0
                        self.hp -= heel_attack_dmg
                    # What is shown during combat
                
                        dprintf(f"{self.name} takes {heel_attack_dmg} DMG from {opponent.name} !")
                        dprintf(f"❤️  {self.name} : {self.hp} / {self.defaultHp} HP")
                        

                if self.hp <= 0:
                    dprint("You lose !")
                    dprint(f"{self.name} : 0 HP")
                    hero.is_dead = True
                    
                    
                if opponent.hp <= 0:
                        heel.is_dead = True
                        dprint("You won !")
                        dprint(f"{opponent.name} : 0 HP")
                        self.level_up(1)
                        
                        
                        


class Ennemy(Character):
    def __init__(self, name, hp, atk, res):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.res = res


characters = [
    #           (self, name, job, hp, defaultHp, atk, res, gold, luck,is_dead):
    Aventureer("Jolan", "Necromancer", 25, 25, 11, 2, 100, 2, False),
    Aventureer("Allan", "Rogue", 28, 28, 12, 1, 100, 1, False),
    Aventureer("Marcus", "Barbarian", 30, 30, 9, 3, 100, 1, False),
    Aventureer("Arnaud", "Bard", 15, 15, 18, 3, 100, 7, False),
    Aventureer("Stalin", "Unbending", 25, 25, 15, 3, 100, 5, False),
    Aventureer("Bastien", "Magicien", 25, 25, 20, 3, 100, 6, False),
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
def set_ennemy():
    opponent = choice(characters)
    return opponent

def show_chars():
    print(":-=-=-=-=-:".center(75))
    for character in characters:
        print(f"  {character.name}.".center(75))
    print(":-=-=-=-=-:".center(75))


def intro():
    print("""                                                                           
     /\                            | |                                      
    /  \    __   __   ___   _ __   | |_   _   _   _ __    ___    ___   _ __ 
   / /\ \   \ \ / /  / _ \ | '_ \  | __| | | | | | '__|  / _ \  / _ \ | '__|
  / ____ \   \ V /  |  __/ | | | | | |_  | |_| | | |    |  __/ |  __/ | |   
 /_/    \_\   \_/    \___| |_| |_|  \__|  \__,_| |_|     \___|  \___| |_|   
                                                                            
                                                                            """)
    show_chars()

def initGame():
    hero.show_stats()
    input(f"Ready to go on an adventure ? Press [ENTER]".center(75))
    hero.attack(heel)
    if hero.is_dead == True:
        print(f"Vous êtes mort !")
        hero.is_dead == False
        hero.heal()
    if heel.is_dead == True:
        print(f"{heel.name} est mort")
        heel.heal()
        heel = choose_ennemy()
        4

        heel.is_dead = False
    if heel.is_dead == False:
        print("Ok")
        heel.level_up(1)
        hero.show_stats()
        hero.attack(heel)
        initGame()



intro()

hero = Aventureer("Jimmy")
heel = choose_ennemy()

initGame()