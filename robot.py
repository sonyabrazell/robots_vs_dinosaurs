from weapon import Weapon

class Robot:
    def __init__(self, name, weapon):
        self.name = name
        self.health = 10
        self.weapon = weapon

    def robot_attack(self, dinosaur):
        dinosaur_health = dinosaur.health
        weapon_strength = Weapon.attack_power
        remaining_health = dinosaur_health - weapon_strength
        print('After robot attack,', dinosaur.name,' now has',remaining_health,' health remaining.')
        return remaining_health