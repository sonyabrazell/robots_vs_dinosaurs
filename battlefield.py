from robot import Robot
from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.fleet.create_fleet()
        self.herd.create_herd()
       

    def display_welcome(self):
        print("Welcome to the battle.")

    def battle(self):
        robot_attack1 = self.fleet.robots[1].robot_attack(self.herd.dinosaurs[1])
        dino_attack1 = self.herd.dinosaurs[1].dinosaur_attack(self.fleet.robots[1])
        robot_attack2 = self.fleet.robots[2].robot_attack(self.herd.dinosaurs[2])
        dino_attack2 = self.herd.dinosaurs[2].dinosaur_attack(self.fleet.robots[2])
        robot_attack1 = self.fleet.robots[3].robot_attack(self.herd.dinosaurs[3])
        dino_attack1 = self.herd.dinosaurs[3].dinosaur_attack(self.fleet.robots[3])


    def dino_turn(self, dinosaur):
        turning_dino1 = self.herd.dinosaurs[1]
        turning_dino1 == True
        turning_dino2 = self.herd.dinosaurs[2]
        turning_dino2 == True
        turning_dino3 = self.herd.dinosaurs[3]
        turning_dino3 == True

        
    def robo_turn(self, robot):
        turning_robo1 = self.fleet.robots[1]
        turning_robo1 == True
        turning_robo2 = self.fleet.robots[2]
        turning_robo2 == True
        turning_robo3 = self.fleet.robots[3]
        turning_robo3 == True

    def show_dino_opponent_options(self):
        for dinosaur in self.herd:
            print(dinosaur)

    def show_robo_opponent_options(self):
        for robot in self.fleet:
            print(robot)

    def display_winners(self):
        for robot in self.herd.dinosaurs.dinosaur_attack:
            if robot.health > 0:
                battle()
            if robot.health <= 0:
                print("Dinosaurs win.")
        for dinosaur in self.fleet.robots.robot_attack:
            if dinosaur.health > 0:
                battle()
            if dinosaur.health <= 0:
                print("Robots win.")
