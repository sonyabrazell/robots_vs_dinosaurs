from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self):
        weapon1 = Weapon('lightsaber', 3)
        robot1 = Robot('Lucius', weapon1)
        robot2 = Robot('Narcissa', weapon1)
        robot3 = Robot('Draco', weapon1)
        self.robots.append(robot1)
        self.robots.append(robot2)
        self.robots.append(robot3)