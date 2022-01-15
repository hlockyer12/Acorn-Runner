from game_parser import parse
import cells

def test_parser():
    """ 
    Test the parse function to make sure the provided string 
    (usually from a board text file) will be returned as a list of 
    list of cells of the correct class. 
    
    The provided string was chosen as it represents 1 of each cell 
    Class that can be in the board text files. 
    """

    # Parser Test Cases Reference:
    # Parser-1 = Wall Cell
    # Parser-2 = Start Cell
    # Parser-3 = End Cell
    # Parser-4 = Water Cell
    # Parser-5 = Fire Cell
    # Parser-6 = Teleport Cell
    # Parser-7 = Teleport Cell (must have a pair of Teleport Cells)

    parsetest = parse(['*XYWF11'])
    cell_list = [cells.Wall(),
                cells.Start(), 
                cells.End(), 
                cells.Water(), 
                cells.Fire(),
                cells.Teleport(),
                cells.Teleport()]
    cell_list[5].display = cell_list[6].display = '1'

    # Check all cell types have correct display (proving they are the correct type)
    i = 0
    while i < len(parsetest[0]):
        assert parsetest[0][i].display == cell_list[i].display, 'Test Case Parser-{} failed'.format(i+1)
        i += 1

    print('All game_parser.py Test Cases passed!')
    

def run_tests():
    test_parser()

