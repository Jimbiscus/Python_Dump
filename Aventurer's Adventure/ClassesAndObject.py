from random import randint
from random import choice
import time
import sys

# Display char by char functions, a normal a fast one with a line break between each print
# by andrew-walker on stackoverflow

# WIP



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
global heel
intro()
hero = choose_character()
heel = choose_ennemy()
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

        heel.is_dead = False
    if heel.is_dead == False:
        print("Ok")
        heel.level_up(1)
        hero.show_stats()
        hero.attack(heel)
        initGame()





initGame()
