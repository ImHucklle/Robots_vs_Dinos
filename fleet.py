from robot import Robots

class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        robot0 = Robots('Optimus Prime', "Lightsaber")
        robot1 = Robots('Master Chief', "BR")
        robot2 = Robots('Megatron', "Potato Cannon")
        self.robots.append(robot0)
        self.robots.append(robot1)
        self.robots.append(robot2)