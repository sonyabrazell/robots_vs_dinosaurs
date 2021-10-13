from fleet import Fleet
from herd import Herd
from weapon import Weapon
from dinosaur import Dinosaur

class Robot:
    def __init__(self, name, weapon):
        self.name = name
        self.heath = 10
        self.weapon = weapon

    def attack(self, dinosaur):
        #need to have robot attack dinosaur and calculate what the dinosaurs new health score
        #after subracting the attacking robot's attack score. does not need to specify which robot
        #or which dinosaur. information can be called in battle.
        dinosaur = Dinosaur.name
        dinosaur_health = Dinosaur.health
        weapon_strength = Weapon.attack_power
        remaining_health = dinosaur_health - weapon_strength
        print('After robot attack, the dinosaur now has ',remaining_health,' health remaining.')