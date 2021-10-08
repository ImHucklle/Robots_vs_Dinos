from robot import Robots
from weapons import Weapons

class Fleet:
    def __init__(self):
        self.robots = ["Megatron", "Optimus", "Atraks"]

    def create_fleet(self):
        robot_one = Robots("Megatron", 1500, Weapons ("Lightsaber", 225))
        self.robots.append(robot_one)

        robot_two = Robots("Optimus", 1400, Weapons ("BFG 9000", 250))
        self.robots.append(robot_two)

        robot_three = Robots("Atraks", 1250, Weapons ("Energy Sword", 200))
        self.robots.append(robot_three)

        print(f"{robot_one.name}, {robot_two.name} and {robot_three.name} have entered the Battlefield!")