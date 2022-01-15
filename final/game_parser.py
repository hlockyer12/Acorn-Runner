from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)


def read_lines(filename):
    """Read in a file, process them using parse(),
    and return the contents as a list of list of cells."""
    try:
        file = open(filename, "r")
    except FileNotFoundError:
        print("{} does not exist!".format(filename))
        exit()
    gridlines = [] #Will become a list with each element being a row of the grid
    while True:
        line = file.readline()
        if line == "":
            break #Stop reading the file
        else:
            gridlines.append(line)
    file.close()
    cell_grid = parse(gridlines)
    return cell_grid

def parse(lines):
    """Transform the input into a grid.
    Arguments:
        lines -- list of strings representing the grid
    Returns:
        list -- contains list of lists of Cells
    """
    x_count = 0
    y_count = 0
    list_of_elements = []
    teleport_list = []
    i = 0
    while i < len(lines):
        element = []
        j = 0
        while j < len(lines[i]):
            cell = lines[i][j]
            if cell == "*":
                element.append(Wall()) 
            elif cell == "X":
                element.append(Start())
                x_count += 1   
            elif cell == "Y":
                element.append(End())
                y_count += 1   
            elif cell == " ":
                element.append(Air())   
            elif cell == "W":
                element.append(Water())
            elif cell == "F":
                element.append(Fire())
            elif cell.isdigit() and cell != "0":
                a = Teleport()
                a.display = cell
                a.x = j
                a.y = i
                element.append(a)
                if cell not in teleport_list:
                    teleport_list.append(cell)
                    teleport_list.sort()
                elif cell in teleport_list:
                    del teleport_list[int(cell)-1]   
            elif cell == "\n":
                break
            else:
                raise ValueError ("Bad letter in configuration file: {}.".format(cell))
            j += 1
        list_of_elements.append(element)
        i += 1            
    #Starting position, ending positions and teleporters error checking
    if x_count != 1:
        raise ValueError ("Expected 1 starting position, got {}.".format(x_count))
    if y_count != 1:
        raise ValueError ("Expected 1 ending position, got {}.".format(y_count))
    if len(teleport_list) != 0:
        raise ValueError ("Teleport pad {} does not have an exclusively matching pad.".format(teleport_list[0]))
    return list_of_elements
