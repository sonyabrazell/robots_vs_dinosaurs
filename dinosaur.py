from herd import Herd
from fleet import Fleet
from robot import Robot

class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 10

    def attack(self, robot):
        robot_health = Robot.health
        dinosaur_power = Herd.attack_power
        remaining_health = robot_health - dinosaur_power
        