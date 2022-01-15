# You may need this if you really want to use a recursive solution!
# It raises the cap on how many recursions can happen. Use this at your own risk!

# sys.setrecursionlimit(100000)
from game import Game
import sys

def solvebfs(game):
    
    result = [game.num_moves, game.moves_made, False]
    if game.finished == 'win':
        result [2] = True
    return result

def solvedfs(game):
    result = [game.num_moves, game.moves_made, False]
    if game.finished == 'win':
        result [2] = True
    return result

def solve(mode):
    game = Game(sys.argv[1])
    if mode == 'bfs':
        return solvebfs(game)
    elif mode == 'dfs':
        return solvedfs(game)
    else:
        return False

def find_start(game):
    top = game.lines[0]
    i = 0
    while i < len(top):
        if top[i].display == "X":
            return [0, i]
        i += 1

def find_end(game):
    bottom = game.lines[-1]
    i = 0
    while i < len(bottom):
        if bottom[i].display == "Y":
            return [(len(game.lines) - 1), i]
        i += 1

def list_to_string(ls):
    i = 1
    string = ''
    while i < len(ls):
        string = string + ls[i] + ', '
        i += 2
    string = string[:-2]
    return string

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 <filename> <mode>")
        sys.exit()
    mode = sys.argv[2].lower()
    result = solve(mode)
    if result == False:
        print("Usage: python3 <filename> <mode>")
        sys.exit()
    solution_found = result[2]
    result[1] = list_to_string(result[1])
    if solution_found:
        print('Path has {} moves'.format(result[0]))
        print('Path: {}'.format(result[1]))
    else:
        print("There is no possible path.")


