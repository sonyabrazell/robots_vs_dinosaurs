from fleet import Fleet
from herd import Herd
from weapon import Weapon

class Robot:
    def __init__(self, name, weapon):
        self.name = name
        self.heath = 10
        self.weapon = weapon

    def attack(self, dinosaur):