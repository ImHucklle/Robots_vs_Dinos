from dinosaur import Dinosaurs

class Herd:
    def __init__(self):
        self.dinosaur = ["Godzilla", "Indominus Rex", "Drogon"]
    
    def create_herd(self):
        dinosaur_one = Dinosaurs("Godzilla", 2000, 125)
        self.dinosaur.append(dinosaur_one)

        dinosaur_two = Dinosaurs("Indominus Rex", 1500, 150)
        self.dinosaur.append(dinosaur_two)

        dinosaur_three = Dinosaurs("Drogon", 1700, 200)
        self.dinosaur.append(dinosaur_three)
        
        print(f"{dinosaur_one.name}, {dinosaur_two.name} and {dinosaur_three.name} have entered the Battlefield!")
