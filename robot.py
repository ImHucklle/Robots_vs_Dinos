from weapons import Weapons

class Robots:
    def __init__(self, name, weapon):
        self.name = name
        self.health = 1500
        self.weapon = Weapons(weapon, 200)

    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power