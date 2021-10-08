from weapons import Weapons

class Robots:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.weapon = Weapons

    def attack(self, dinosaur):
        self.attack = self.weapon - dinosaur(0)