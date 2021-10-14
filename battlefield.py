from robot import Robot
from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = []
        self.herd = []

def run_game(self):
    fleet = Fleet()
    fleet.create_fleet()
    herd = Herd()
    herd.create_herd()

def display_welcome(self):
    print("Welcome to the battle.")

def battle(self):
    robot_battle = Robot()
    robot_battle.attack()
    dinosaur_battle = Dinosaur()
    dinosaur_battle.attack()
    return(robot_battle,dinosaur_battle)

def dino_turn(self, dinosaur):
    turning_dino = Dinosaur()
    if dinosaur.turning_dino == True:
        print(dinosaur, ' has turned.')
    
def robo_turn(self, robot):
    turning_robo = Robot()
    if robot.turning_robo == True:
        print(robot, " has turned.")

def show_dino_opponent_options(self):
    for dinosaur in self.herd:
        print(dinosaur)

def show_robo_opponent_options(self):
    for robot in self.fleet:
        print(robot)

def display_winners(self):
    for robot in Dinosaur.attack:
        robot_remaining_health = Dinosaur.remaining_health
        if robot_remaining_health > 0:
            battle()
        if robot_remaining_health <= 0:
            print("Dinosaurs win.")
    for dinosaur in Robot.attack:
        dinosaur_remaining_health = Robot.remaining_health
        if dinosaur_remaining_health > 0:
            battle()
        if dinosaur_remaining_health <= 0:
            print("Robots win.")
