from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):
        stegosaurus = Dinosaur('James', 3)
        triceratops = Dinosaur('Lily', 3)
        brontosaurus = Dinosaur('Harry', 2)
        self.dinosaurs.append(stegosaurus)
        self.dinosaurs.append(triceratops)
        self.dinosaurs.append(brontosaurus)