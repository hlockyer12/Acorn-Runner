from game import Game
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)


def test_cells():
    """
    Testing the step methods for each cell to make sure they are 
    returning the correct strings to the game.game_move method.

    A dummy Game instance is created using the board_cell_test.txt file.
    """

    # Cell Test Case Reference:
    # Cell-1: Wall Cell
    # Cell-2: Start Cell
    # Cell-3: Air Cell
    # Cell-4: Fire Cell (no water buckets)
    # Cell-5: Water Cell
    # Cell-6: Fire Cell (1 water bucket)
    # Cell-7: Teleport Cell
    # Cell-8: Teleport Cell (must be in pairs in board file)
    # Cell-9: End Cell

    cell_test = Game('board_cell_test.txt')
    row = cell_test.lines[1]
    step_returns = ['oof', 'air', 'air', 'burnt', 'water', 'doused', 'tele', 'tele', '']
    i = 0
    while i < len(row):
        cell = row[i]
        assert cell.step(cell_test) == step_returns[i], 'Test Cell-{} failed'.format(i+1)
        i += 1

    print('All cells.py Test cases passed!')

def run_tests():
    test_cells()
