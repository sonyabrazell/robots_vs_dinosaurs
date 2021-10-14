from battlefield import Battlefield, dino_turn, display_welcome, robo_turn, run_game, show_dino_opponent_options, show_robo_opponent_options
from herd import Herd
from fleet import Fleet
from dinosaur import Dinosaur
from robot import Robot

battle_import = Battlefield()

print(display_welcome(Battlefield))

run_game(Battlefield)

show_dino_opponent_options(Battlefield)

show_robo_opponent_options(Battlefield)

dino_turn(Herd)

robo_turn(Fleet)

attack(Robot, dinosaur)







