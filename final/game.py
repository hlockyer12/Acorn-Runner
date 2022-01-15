from game_parser import read_lines
from grid import grid_to_string
from player import Player
import cells


class Game:
    def __init__(self, filename):
        self.filename = filename
        self.num_moves = 0 
        self.moves_made = [] 
        self.lines = read_lines(filename)
        self.player = Player() 
        self.grid = grid_to_string(self.lines, self.player) 
        
        # extra lines to print in certain circumstances i.e. picked up a water bucket, walked into a wall
        self.extralines = '' 
        
        # 'playing' if game instance is still going, 'win' if the end has been reached or 'burnt' if acorn has walked into fire without water
        self.finished = 'playing' 
        
        # stored current move to record in moves_made
        self.current_move = '' 
        

    def game_move(self, move):
        """
        Used to check that the move entered is valid and will return a 
        string for run.py to print
        """
        if move == 'q':
            return 'quit'
        valid_moves = ['w', 'a', 's', 'd', 'e']
        if move not in valid_moves:
            return 'Invalid move'
        player = self.player
        x, y, m = player.col, player.row, player.move(move)
        printout = ''
        if player.row >= len(self.lines):
            player.row -= 1
        elif player.col >= len(self.lines[player.row]):
            player.col -= 1
        cell = self.lines[player.row][player.col]

        # Check what cell has the player moved onto
        react = cell.step(self) 

        # 1. Wall Cell
        # If player moves out of bounds, remove last move and act as a wall
        if m == 'out': 
            react = 'oof'
            self.moves_made[:-1]
            self.num_moves -= 1

        # Push player back if they move into wall
        if react == 'oof': 
            player.col = x
            player.row = y
            printout = '\n\nYou walked into a wall. Oof!'

        # 2. Start Cell
        # Player walked back onto starting position
        elif react == 'start': 
            printout = '\n\nYou walked into a wall. Oof!'

        # 3. Water Cell
        # Player has collected water
        elif react == 'water': 
            printout = "\n\nThank the Honourable Furious Forest, you've found a bucket of water!"

        # 4. Teleport Cell
        # Player has moved onto teleport space
        elif react == 'tele': 
            player.col = cell.pair_x
            player.row = cell.pair_y
            printout = "\n\nWhoosh! The magical gates break Physics as we know it and opens a wormhole through space and time."

        # 5. Fire Cell
        # Player walked onto fire with no water buckets
        elif react == 'burnt': 
            printout = 'You are all burnt up'

        # Player walked onto fire with water bucket
        elif react == 'doused': 
            printout = '\n\nWith your strong acorn arms, you throw a water bucket at the fire. You acorn roll your way through the extinguished flames!'
        
        # 6. Air Cell
        # Player moved into an air space
        elif react == 'air': 
            printout = ''

        # 7. End Cell
        # Player has reached end space
        elif react == 'win': 
            self.moves_made.append(move)
            return
        
        self.grid = grid_to_string(self.lines, self.player)
        return printout

    def move_string(self):
        """ Convert the list of moves made into a printable string """
        move_string = ''
        i = 0
        while i < len(self.moves_made):
            move_string += str(self.moves_made[i]) + ', '
            i += 1
        return move_string[:-2]


