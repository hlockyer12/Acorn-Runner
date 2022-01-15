def grid_to_string(grid, player):
    """
    Turns a grid and player into a string

    Arguments:
        grid -- list of list of Cells
        player -- a Player with water buckets

    Returns
        string: A string representation of the grid and player.
    """

    # 1. Build a string out of the list of list of cells
    string = ''
    i = 0
    while i < len(grid):
        j = 0
        while j < len(grid[i]):
            cell = grid[i][j]

    # 2. If this is the first read of the grid, set the player at the start cell
            if cell.display == 'X' and player.start == 0:
                string += player.display
                player.row = i
                player.col = j
                player.start = 1
    # 3. Otherwise, add the display attribute for the cell to the string
            else:
                string += cell.display

    # 4. If the last cell added matches the coordinates of the player, remove it and add in the
    # player's display attribute
            if i == player.row and j == player.col and player.start == 1:
                string = string[:-1] + player.display
            j += 1
        string += '\n'
        i += 1

    # 5. Check how many water buckets the player has and format appropriately before returning the string
    if player.num_water_buckets == 1:
        water_buckets = "\nYou have {} water bucket.".format(player.num_water_buckets)
    else:
        water_buckets = "\nYou have {} water buckets.".format(player.num_water_buckets)
    string += water_buckets
    return string



