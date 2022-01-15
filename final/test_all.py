""" Runs all unit and e2e tests for the Acorn Runner program """

import subprocess
from test_game import run_tests as test_game
from test_grid import run_tests as test_grid
from test_parser import run_tests as test_parser
from test_cells import run_tests as test_cells
from test_player import run_tests as test_player

# 1. Units tests for each module
#   - game.py
#   - grid.py
#   - game_parser.py
#   - cell.py
#   - player.py
print("#############################")
print("#### Running unit tests! ####")
print("#############################\n")

test_game()
test_grid()
test_parser()
test_cells()
test_player()
print()

# 2. e2e tests for the game
#   - e2e Test files found in tests_e2e folder
#   - e2e subprocess found in test_e2e.sh

# e2e Test reference (all using board_e2e_test.txt):
#   1. Quit program immediately after starting
#   2. Move one space then quit
#   3. Reach the end cell
#   4. Invalid move, then quit
#   5. Walk into wall, then quit
#   6. Pick up water, extinguish fire then move to end cell
#   7. Walking onto fire without a water bucket, then to end cell
#   8. Walking onto a teleport pad then quitting

# These e2e tests were chosen as they represent all the mechanics within the game:
#   - Quitting the game
#   - Walking into a wall
#   - The Fire/Water mechanic
#   - Teleport pads
#   - Finishing the game
subprocess.call(['./test_e2e.sh'])
