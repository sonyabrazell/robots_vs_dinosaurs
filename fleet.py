from robot import Robot

class Fleet:
    def __init__(self,name):
        self.robots = []

    def create_fleet(self):
        robot1 = Robot('Lucius')
        robot2 = Robot('Narcissa')
        robot3 = Robot('Draco')
        self.robots.append(robot1)
        self.robots.append(robot2)
        self.robots.append(robot3)