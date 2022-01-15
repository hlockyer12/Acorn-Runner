class Start:
    def __init__(self):
        self.display = 'X'
        self.depart = 0 # marker to check if the player is moving back onto the staring cell

    def step(self, game):
        """ 
        Treat the starting cell as an air cell but take note 
        if the player moves back onto the cell
        """
        if self.depart > 0:
            self.depart = 0
            return 'start' # player has moved back onto starting cell
        game.num_moves += 1
        game.moves_made.append(game.current_move)
        self.depart += 1
        return 'air' 

class End:
    def __init__(self):
        self.display = 'Y'

    def step(self, game):
        """ 
        Return the string to start the endgame sequence 
        """
        game.num_moves += 1
        game.moves_made.append(game.current_move)
        game.finished = 'win'
        return ''


class Air:
    def __init__(self):
        self.display = ' '

    def step(self, game):
        """
        Record the move and the move input from the user
        """
        game.num_moves += 1
        game.moves_made.append(game.current_move)
        return 'air'


class Wall:
    def __init__(self):
        self.display = '*'

    def step(self, game):
        """
        Return the string to move the player into their previous cell
        """
        return 'oof'


class Fire:
    def __init__(self):
        self.display = 'F'

    def step(self, game):
        """
        Check if the player has any water buckets and can douse the fire
        or if they burn, begin the game over sequence if true
        """
        game.num_moves += 1
        game.moves_made.append(game.current_move)
        if game.player.num_water_buckets <= 0:
            game.finished = 'burnt'
            return 'burnt'
        else:
            game.lines[game.player.row][game.player.col] = Air()
            game.player.num_water_buckets -= 1
            return 'doused'


class Water:
    def __init__(self):
        self.display = 'W'

    def step(self, game):
        """
        Increase the number of water buckets the player has 
        and turn the cel into an air cell
        """
        game.num_moves += 1
        game.moves_made.append(game.current_move)
        game.player.num_water_buckets += 1
        game.lines[game.player.row][game.player.col] = Air()
        return 'water'


class Teleport:
    def __init__(self):
        self.display = ''
        self.tele_num = 0
        self.x = ''
        self.y = ''
        self.pair_x = ''
        self.pair_y = ''

    def step(self, game):
        """
        Move the player to the corresponding teleport pad
        """
        game.num_moves += 1
        game.moves_made.append(game.current_move)
        if self.pair_x == '' and self.pair_y == '':
            self.pair_up(game)
        return 'tele'



    def pair_up(self, game):
        """
        Create the matching pairs of teleport pads, storing both coordinates
        in each cell
        """
        i = 0
        while i < len(game.lines):
            j = 0
            while j < len(game.lines[i]):
                t2 = game.lines[i][j]
                if self.display == t2.display and (self.x != t2.x or self.y != t2.y):
                    self.pair_x = t2.x
                    self.pair_y = t2.y
                    t2.pair_x = self.x
                    t2.pair_y = self.y
                    return True
                j += 1
            i += 1
        return False






