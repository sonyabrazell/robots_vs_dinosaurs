from weapon import Weapon
from dinosaur import Dinosaur

class Robot:
    def __init__(self, name, weapon):
        self.name = name
        self.health = 10
        self.weapon = weapon

    def attack(self, dinosaur):
        dinosaur_health = dinosaur.health
        weapon_strength = Weapon.attack_power
        remaining_health = dinosaur_health - weapon_strength
        print('After robot attack, the dinosaur now has ',remaining_health,' health remaining.')