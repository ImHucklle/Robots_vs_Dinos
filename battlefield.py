from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self):
        pass

    def display_welcome(self):
        print ("Hello, welcome to the carnage!")

#user picks team then starts, 1 for robots, 2 for dinos

    def run_game(self):
        team_select = input("Choose yout side! 1 for Team Robots or 2 for Team Dino")
        if team_select.battle(self) == '1':
            print('You chose Team Robots!')
        elif team_select.battle(self) == '2':
            print('You chose Team Dino!')
        else:
            print("Invalid entry, try again")
        return team_select

        


    def battle(self):
        if dinosaur.turn < robot.turn:
            dinosaur.attack()

            if robot.health > 0:
                robot.attack()
            else:
                robot.health = 0
                return robot.health

        elif dinosaur.turn > robot.turn:
            robot.attack()

            if dinosaur.health > 0:
                dinosaur.attack(Player1,Player2)
            else:
                dinosaur.health = 0
                return Player1.health

            # Any one dies use random.()
            

    def display_winners(self):
        if self.dinosaur() < 1 and self.robots() > 0:
            self.gameOver = True
            print("Team Robots WIN!")
        elif self.robots(self) < 1 and self.dinosaur() > 0:
            self.gameOver = True
            print("Team Dino WINS")
        #which robots or dinosaurs died
        #declared winner/ validate winner