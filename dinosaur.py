

class Dinosaurs:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, robot):
        self.attack = self.attack_power - robot(0)
