from battlefield import Battlefield, dino_turn, display_welcome, display_winners, robo_turn, run_game, show_dino_opponent_options, show_robo_opponent_options
from herd import Herd
from fleet import Fleet
from dinosaur import Dinosaur
from robot import Robot

battle_import = Battlefield()

print(display_welcome(Battlefield))

run_game(Battlefield)

show_dino_opponent_options(Battlefield)

show_robo_opponent_options(Battlefield)

dino_turn(Battlefield, Herd.dinosaurs[1])

robo_turn(Battlefield, Fleet.robots[1])

Dinosaur.dinosaur_attack(Dinosaur, Fleet.robots[1])

Robot.robot_attack(Robot, Herd.dinosaurs[1])

dino_turn(Battlefield, Herd.dinosaurs[2])

robo_turn(Battlefield, Fleet.robots[2])

Dinosaur.dinosaur_attack(Dinosaur, Fleet.robots[2])

Robot.robot_attack(Robot, Herd.dinosaurs[2])

dino_turn(Battlefield, Herd.dinosaurs[3])

robo_turn(Battlefield, Fleet.robots[3])

Dinosaur.dinosaur_attack(Dinosaur, Fleet.robots[3])

Robot.robot_attack(Robot, Herd.dinosaurs[3])

display_winners(Battlefield)






