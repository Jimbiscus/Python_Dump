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

Av1 = Aventurier("Jim", "Wizard", 40, 3, 3, 0)
Av2 = Aventurier("Jolan", "Necromancer", 30, 5, 4, 0)

print(Av2.name)

print(Av1.name)
print(Av2.fullname())

print(Av1.fullname())
print(Aventurier.fullname(Av1))
