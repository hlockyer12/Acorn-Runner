from grid import grid_to_string
from game import Game

def test_grid():
    """
    Test the grid_to_string function, using a dummy Game instance
    to make sure that the function will return the correct string
    representing the maze and water buckets statement.
    """
    gridtest = Game('board_testing.txt')
    lines = gridtest.lines
    player = gridtest.player

    # Grid-1: Check function will return correct maze and water buckets statement
    assert grid_to_string(lines, player) == '***\nA *\n* Y\n***\n\nYou have 0 water buckets.', 'Test Case Grid-1 failed'

    # Grid-2: Try changing the water buckets to singular
    player.num_water_buckets = 1 
    assert grid_to_string(lines, player) == '***\nA *\n* Y\n***\n\nYou have 1 water bucket.', 'Test Case Grid-2 failed'

    # Grid-3: Try changing water buckets to a large number
    player.num_water_buckets = 1000 
    assert grid_to_string(lines, player) == '***\nA *\n* Y\n***\n\nYou have 1000 water buckets.', 'Test Case Grid-3 failed'

    # Grid-4: grid_to_string should still print the water buckets, 
    # even if it is in the wrong format (function will not recognize 'one' as singular)
    player.num_water_buckets = 'one' 
    assert grid_to_string(lines, player) == '***\nA *\n* Y\n***\n\nYou have one water buckets.', 'Test Case Grid-4 failed'

    # Grid-5: Try moving the player into another space
    player.num_water_buckets = 0
    gridtest.game_move('d')
    assert grid_to_string(lines, player) == '***\nXA*\n* Y\n***\n\nYou have 0 water buckets.', 'Test Case Grid-5 failed'

    # Grid-6: Try moving the player into the wall, should not work
    gridtest.game_move('d') 
    assert grid_to_string(lines, player) == '***\nXA*\n* Y\n***\n\nYou have 0 water buckets.', 'Test Case Grid-6 failed'

    print('All grid.py Test Cases passed!')


def run_tests():
    test_grid()

