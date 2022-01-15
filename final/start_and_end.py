from game import Game
import os

# Functions created for the two endgame posibilities and to create an intro to the game (see run.py - Intro mode)

def endgame(game):
    print('\n\nYou conquer the treacherous maze set up by the Fire Nation and reclaim the Honourable Furious Forest Throne, restoring your hometown back to its former glory of rainbow and sunshine! Peace reigns over the lands.\n')
    if game.num_moves == 1:
        print('You made {} move.\nYour move: {}'.format(game.num_moves, game.move_string()))
    else:
        print('You made {} moves.\nYour moves: {}'.format(game.num_moves, game.move_string()))
    print('\n=====================')
    print('====== YOU WIN! =====')
    print('=====================')

def burntup(game):
    print('\n\nYou step into the fires and watch your dreams disappear :(.\n')
    print('The Fire Nation triumphs! The Honourable Furious Forest is reduced to a pile of ash and is scattered to the winds by the next storm... You have been roasted.\n')
    if game.num_moves == 1:
        print('You made {} move.\nYour move: {}'.format(game.num_moves, game.move_string()))
    else:
        print('You made {} moves.\nYour moves: {}'.format(game.num_moves, game.move_string()))
    print('\n=====================')
    print('===== GAME OVER =====')
    print('=====================')

def intro():
    os.system('clear')
    filename = 'intro.txt'
    file = open(filename)
    line = file.readline().strip()
    while line != '':
        print(line)
        line = file.readline().strip()
    file.close()
    input("")
