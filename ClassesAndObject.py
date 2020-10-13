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
        print(self.name + " the " + self.job)
        print("hp : " + str(self.hp))
        print("atk : " + str(self.atk))
        print("def : " + str(self.res))
        print("gold : " + str(self.gold))


Av1 = Aventurier("Jim", "Wizard", 40, 3, 3, 0)
Av2 = Aventurier("Jolan", "Necromancer", 30, 5, 4, 0)

Av2.showStats()
print("VERSUS")
Av1.showStats()
Av1.levelUp()
Av1.showStats()


Av1.hp = 10000000
Av1.showStats()
