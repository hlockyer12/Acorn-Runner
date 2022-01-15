from game import Game
import start_and_end
from game_parser import read_lines
import os
import sys
    
# 1. Check command line arguments are valid and what mode the game is being played in
#   Play mode: Will clear the OS and reprint the maze after each move by the user
#   Intro mode: Will provide intro text for the user then move onto Play mode
osclear = False
modes = ['play', 'intro']
if len(sys.argv) != 2 and not (len(sys.argv) == 3 and sys.argv[2] in modes):
    print('Usage: python3 run.py <filename> [play/intro]')
    sys.exit()
elif len(sys.argv) == 3:
    if sys.argv[2] == 'play':
        osclear = True
    elif sys.argv[2] == 'intro':
        osclear = True
        start_and_end.intro()

# 2. Create a Game instance for the supplied filename
filename = str(sys.argv[1])
game = Game(filename)
game.lines = read_lines(game.filename)

# 3. Run the game on a loop until the player quits, they complete the maze or they burn in the fire
while True:
    if osclear:
        os.system('clear')
    extras = game.extralines
    print(game.grid + game.extralines)
    game.extralines = ''
    print()
    move = (input("Input a move: ")).lower()
    valid_moves = ['w', 'a', 's', 'd', 'e', 'q']
    if move not in valid_moves:
        game.extralines = "\n\nPlease enter a valid move (w, a, s, d, e, q)."
        continue
    game.current_move = move
    printout = game.game_move(move)
    if printout == 'quit':
        print("\nBye!")
        sys.exit()
    elif game.finished == 'win':
        if osclear:
            os.system('clear')
        print(game.grid + game.extralines)
        start_and_end.endgame(game)
        sys.exit()
    elif game.finished == 'burnt':
        if osclear:
            os.system('clear')
        print(game.grid + game.extralines)
        start_and_end.burntup(game)
        sys.exit()
    elif printout != '':
        game.extralines = printout



    
