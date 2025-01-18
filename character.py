from health_bar import HealthBar
from mana_bar import ManaBar

class Character:
    def __init__(self, name, health, health_max, strength):
        self.name = name
        self.health = health
        self.health_max = health_max
        self.strength = strength

    def attack(self, target):
        damage = self.strength
        target.health = max(target.health - damage, 0)
        target.health_bar.update()
        print(f"{self.name} attacks {target.name} for {damage} damage!")

    def isAlive(self):
        return self.health > 0
    
class Hero(Character):
    def __init__(self, name, health, health_max, strength, mana):
        super().__init__(name, health, health_max, strength)
        self.mana = mana
        self.mana_max = mana
        self.health_bar = HealthBar(self, color="green")
        self.mana_bar = ManaBar(self)

    def special_attack(self, target):
        if self.mana >= 10:
            damage = self.strength * 2
            self.mana -= 10
            self.mana_bar.update()
            target.health = max(target.health - damage, 0)
            target.health_bar.update()
            print(f"{self.name} uses a special attack on {target.name} for {damage} damage!")
        else:
            print(f"{self.name} doesn't have enough mana for a special attack.")

    def heal(self):
        if self.mana >= 5:
            self.health = min(self.health + 15, self.health_max)
            self.health_bar.update()
            self.mana -= 5
            self.mana_bar.update()
            print(f"{self.name} heals for 15 health.")
        else:
            print(f"{self.name} doesn't have enough mana to heal.")


class Goblin(Character):
    def __init__(self):
        super().__init__("Goblin", 30, 30, 5)
        self.health_bar = HealthBar(self, color="red")

class Dragon(Character):
    def __init__(self):
        super().__init__("Dragon", 100, 100, 20)
        self.health_bar = HealthBar(self, color="red")