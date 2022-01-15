from game import Game


def test_game():
    """
    Testing the game_move function to make sure that the 
    expected string will be returned to the run.py program 
    using a dummy Game instance of board_testing.txt
    """

    testgame = Game('board_testing.txt')

    # Game-1: Moving into wall from starting position
    assert testgame.game_move('s') == '\n\nYou walked into a wall. Oof!', 'Test Case Game-1 failed'

    # Game-2: Moving onto air space
    assert testgame.game_move('d') == '', 'Test Case Game-2 failed' 

    # Game-3: Moving onto air space in same direction as Test Case Game-1
    assert testgame.game_move('s') == '', 'Test Case Game-3 failed' 

    # Game-4: Moving back onto starting position
    testgame.game_move('w')
    assert testgame.game_move('a') == '', 'Test Case Game-4 failed' 

    # Game-5: Attempting to move out of bounds past starting position
    assert testgame.game_move('a') == '\n\nYou walked into a wall. Oof!', 'Test Case Game-5 failed'

    # Game-6: Using an invalid move
    assert testgame.game_move('r') == 'Invalid move', 'Test Case Game-6 failed' 

    # Game-7: Using an integer as a move
    assert testgame.game_move(1) == 'Invalid move', 'Test Case Game-7 failed'

    print('All game.py Test Cases passed!')   


def run_tests():
    test_game()

