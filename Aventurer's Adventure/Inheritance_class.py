from secrets import choice

class Character:
    def __init__(self, name, attack_points, defense_points, life):
        self.name           = name
        self.attack_points  = attack_points
        self.defense_points = defense_points
        self.life           = life

    def attack(self, opponent):
        attack_damage = self.attack_points - opponent.defense_points

        if opponent.life >= attack_damage:
            opponent.life -= attack_damage
        else:
            opponent.life = 0
        
        print(f"{self.name} attacked {opponent.name} for {attack_damage} damage(s)")
        print(f"{opponent.life} remaining")
    
    def is_dead(self):
        if self.life <= 0:
            print(f"{self.name} is dead")
            return True
        else:
            return False

class Hero(Character):
    def __init__(self, name, attack_points, defense_points, life, amount_gold):
        self.name           = name
        self.attack_points  = attack_points
        self.defense_points = defense_points
        self.life           = life
        self.amount_gold    = amount_gold

class Ennemy(Character):
    def __init__(self, name, attack_points, defense_points, life, amount_of_scalps):
        self.name             = name
        self.attack_points    = attack_points
        self.defense_points   = defense_points
        self.life             = life
        self.amount_of_scalps = amount_of_scalps
  

hero = Hero("Jolan", 11, 15, 100, 10)
ennemy = Ennemy("Blurg", 6, 4, 20, 12)

should_continue = True

names = ["Blurg", "Blorg", "Blerg", "Blarg", "Blyrk"]

while should_continue:
  hero.attack(ennemy)

  if(ennemy.is_dead() and not hero.is_dead()):
    should_continue = True
    ennemy = Ennemy(choice(names), 6, 4, 20, 12)
    print("========= A NEW ENNEMY APPEARED ============")

  if hero.is_dead():
      should_continue = False