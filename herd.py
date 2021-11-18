from dinosaur import Dinosaurs

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()
    
    def create_herd(self):
        dino0 = Dinosaurs("Indominus Rex", 150)
        dino1 = Dinosaurs("Godzilla", 170)
        dino2 = Dinosaurs("Blue", 180)
        self.dinosaurs.append(dino0)
        self.dinosaurs.append(dino1)
        self.dinosaurs.append(dino2)
