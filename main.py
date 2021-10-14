from battlefield import Battlefield
from herd import Herd 
from fleet import Fleet
from dinosaur import Dinosaur
from robot import Robot

intro_message = Battlefield.display_name(Battlefield)
print(intro_message)

begin_battle = Battlefield.run_game(Battlefield)
print(begin_battle)

dino_fighters = Battlefield.show_dino_opponent_options(Battlefield)
print(dino_fighters)

robo_fighters = Battlefield.show_robo_opponent_options(Battlefield)
print(robo_fighters)

dino_fighting_stance1 = Battlefield.dino_turn(Battlefield, Herd.dinosaurs[1])
print(dino_fighting_stance1)

robo_fighting_stance1 = Battlefield.robo_turn(Battlefield, Fleet.robots[1])
print(robo_fighting_stance1)

dino_attack1 = Dinosaur.dinosaur_attack(Dinosaur, Fleet.robots[1])
print(dino_attack1)

robot_attack1 = Robot.robot_attack(Robot, Herd.dinosaurs[1])
print(robot_attack1)

dino_fighting_stance2 = Battlefield.dino_turn(Battlefield, Herd.dinosaurs[2])
print(dino_fighting_stance2)

robo_fighting_stance2 = Battlefield.robo_turn(Battlefield, Fleet.robots[2])
print(robo_fighting_stance2)

dino_attack2 = Dinosaur.dinosaur_attack(Dinosaur, Fleet.robots[2])
print(dino_attack2)

robot_attack2 = Robot.robot_attack(Robot, Herd.dinosaurs[2])
print(robot_attack2)

dino_fighting_stance3 = Battlefield.dino_turn(Battlefield, Herd.dinosaurs[3])
print(dino_fighting_stance1)

robo_fighting_stance3 = Battlefield.robo_turn(Battlefield, Fleet.robots[3])
print(robo_fighting_stance1)

dino_attack3 = Dinosaur.dinosaur_attack(Dinosaur, Fleet.robots[3])
print(dino_attack3)

robot_attack3 = Robot.robot_attack(Robot, Herd.dinosaurs[3])
print(robot_attack3)

game_over = Battlefield.display_winners(Battlefield)
print(game_over)






