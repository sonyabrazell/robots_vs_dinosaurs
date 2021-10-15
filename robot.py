from weapon import Weapon

class Robot:
    def __init__(self, name, weapon):
        self.name = name
        self.health = 10
        self.weapon = weapon

    def robot_attack(self, dinosaur):
        dinosaur.health = dinosaur.health - self.weapon.attack_power
        print('After robot attack,', dinosaur.name,' now has',dinosaur.health,' health remaining.')
        
        