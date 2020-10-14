from random import randint

class Aventurier:
    def __init__(self, name,job, hp, atk, res, gold):
        self.name = name
        self.job = job
        self.hp = hp
        self.atk = atk
        self.res = res
        self.gold = gold

    def fullname(self):
       return f"{self.name} the {self.job}"
    def levelUp(self):
        self.hp = int(self.hp * 1.05)
        self.atk = int(self.atk + 3)
        self.res = int(self.res + 1)
        self.gold = int(self.gold + 100)
    def showStats(self):
        print(self.fullname())
        print("hp : " + str(self.hp))
        print("atk : " + str(self.atk))
        print("def : " + str(self.res))
        print("gold : " + str(self.gold))

Av1 = Aventurier("Thomas", "Wizard", 150, 9, 3, 0)
Av2 = Aventurier("Bastien", "Barbarian", 140, 9.5, 4, 0)
Av3 = Aventurier("Marcus", "Barde", 140, 9.5, 4, 0)
Av4 = Aventurier("Jolan", "Necromancien", 140, 9.5, 4, 0)
Av5 = Aventurier("Gimli", "Nain", 140, 9.5, 4, 0)
Av6 = Aventurier("Legolas", "Elfe", 140, 9.5, 4, 0)


def fight1():
    atkvalue = Av2.atk + randint(0, 5)
    Av1.hp -= atkvalue
    atkvalue = Av1.atk + randint(0, 5)
    Av2.hp -= atkvalue
    print(f"{Av2.fullname()} frappe !")
    print( f"{Av1.fullname()} a perdu {atkvalue} hp ! Hp restants : {Av1.hp}")
    print(f"{Av1.fullname()} frappe !")
    print( f"{Av2.fullname()} a perdu {atkvalue} hp ! Hp restants : {Av2.hp}")

def chooseCharacter():
    print ("Choose your Hero :")
    for n in Aventurier:
        print(Aventurier.fullname(n))


chooseCharacter()

Av2.showStats()
print("VERSUS")
Av1.levelUp()
Av1.showStats()
n = 0
while Av1.hp > 0 and Av2.hp > 0:
    fight1()
if Av1.hp <= 0 or Av2.hp <= 0:
    print("Un des aventuriers a été vaincu...")
