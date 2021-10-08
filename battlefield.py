from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self):
        self.battlefield = battlefield
        pass

    def display_welcome(self):
        print ("Hello, welcome to the carnage!")


    def run_game(self):
        team_select = input("Choose yout side! 1 for Team Robots or 2 for Team Dino")
        if team_select.battle(self) == '1':
            print('You chose Team Robots!')
        elif team_select.battle(self) == '2':
            print('You chose Team Dino!')
        else:
            print("Invalid entry, try again")
        return team_select

        #user picks team then starts, 1 for robots, 2 for dinos

        #

    
    def battle(self):
        pass
        #user (player 1) goes first


    def dino_turn(self, dinosaur):
        pass
        #attack


    def robo_turn(self, robot):
        pass
        #attack


    def show_dino_opponent_options(self):
        pass
        #display opponent health and attack power
        #attack which opponent


    def show_robo_opponent_options(self):
        pass
        #display opponent health and attack power
        #attack which opponent

    def display_winners(self):
        if self.dinosaur() < 1 and self.robots() > 0:
            self.gameOver = True
            print("Team Robots WIN!")
        elif self.robots(self) < 1 and self.dinosaur() > 0:
            self.gameOver = True
            print("Team Dino WINS")
        #which robots or dinosaurs died
        #declared winner/ validate winner