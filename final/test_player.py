from player import Player

def test_player():
    """
    Tests the move method for the player, checking that the player.row 
    and player.col attributes will change and not move below 0 (out of bounds).
    """

    player = Player()
    move_set = ['d', 's', 'a', 'a', 'w', 'w', 'r', 1]
    # Player-1: Move player 1 column to the right
    player.move('d')
    assert player.col == 1, 'Test Case Player-1 Failed'

    # Player-2: Move the player 1 row down
    player.move('s')
    assert player.row == 1, 'Test Case Player-2 Failed'

    # PLayer-3: Try to move the player out of bounds to the left
    # player.col should not move below 0
    player.move('a')
    assert player.col == 0, 'Test Case Player-3a Failed'
    player.move('a')
    assert player.col == 0, 'Test Case Player-3b Failed'

    # Player-4: Try to move the player up and out of bounds
    # player.row should not move below 0
    player.move('w')
    assert player.row == 0, 'Test Case Player-4a Failed'
    player.move('w')
    assert player.row == 0, 'Test Case Player-4b Failed'

    # Player-5: Try an invalid input into the move method
    # Neither player.row or player.col should change
    player.move('r')
    assert player.row == 0, 'Test Case Player-5a Failed'
    assert player.col == 0, 'Test Case Player-5b Failed'

    # Player-6: Try an input of a different type into move method
    # Should have same result as Player-5
    player.move(1)
    assert player.row == 0, 'Test Case Player-6a Failed'
    assert player.col == 0, 'Test Case Player-6b Failed'

    # Player-7: Try moving the player very far right and down
    i = 0
    j = 100
    while i < j:
        player.move('d')
        player.move('s')
        i += 1
    assert player.col == 100, 'Test Case Player-7a Failed'
    assert player.row == 100, 'Test Case Player-7b Failed'

    print('All player.py Test cases passed!')

def run_tests():
    test_player()
