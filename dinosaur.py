class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 10

    def attack(self, robot):
        robot_health = robot.health
        dinosaur_power = self.attack_power
        remaining_health = robot_health - dinosaur_power
        print('After dinosaur attack,', robot.name,' now has ',remaining_health,' health remaining.')
        return remaining_health
