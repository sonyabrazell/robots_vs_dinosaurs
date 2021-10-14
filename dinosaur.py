class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 10

    def dinosaur_attack(self, robot):
        robot.health = robot.health - self.attack_power
        print('After robot attack,', robot.name,' now has',robot.health,' health remaining.')
