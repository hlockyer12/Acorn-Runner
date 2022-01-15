class Player:
    def __init__(self):
        self.display = 'A'
        self.num_water_buckets = 0
        self.start = 0 
        # self.start will move to 1 when the grid is first populated
        self.row = 0
        self.col = 0

    def move(self, move):
        """ 
        Move the player in the direction of the input, making 
        sure that the player will not move out of bounds.
        """
        if move == 'w':
            self.row -= 1
            if self.row < 0:
                self.row = 0
                return 'out'
        elif move == 'a':
            self.col -= 1
            if self.col < 0:
                self.col = 0
                return 'out'
        elif move == 's':
            self.row += 1
        elif move == 'd':
            self.col += 1
