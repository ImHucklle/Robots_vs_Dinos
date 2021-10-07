from robot import Robots

class Fleet:
    def __init__(self):
        self.robot = []

    def create_fleet(self):
        robot_one = Robots("Megatron", 1500)
        self.robots.append(robot_one)

        robot_two = Robots("Optimus", 1300)
        self.robots.append(robot_two)

        robot_three = Robots("Cayde-6", 1250)
        self.robots.append(robot_three)
        
        print(f"{robot_one.name}, {robot_two.name} and {robot_three.name} have entered the Battlefield!")