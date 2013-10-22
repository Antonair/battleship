GRID_WIDTH = 10
GRID_HEIGHT = 10

NUM_OF_VESSELS = 4
VESSEL_NAMES = ['aircraft carrier', 'battleship', 'submarine', 'destroyer']
VESSEL_SIZES = [5,4,3,2]

def print_grid(defend_grid) :
    print('   A B C D E F G H I J')
    for row_index in range(0, GRID_HEIGHT) :
        print(row_index + 1, '', end="")
        if (row_index + 1 < 10) :
            print(' ', end="")
            
        for column_index in range(0, GRID_WIDTH) :
            print(defend_grid[row_index][column_index], '', end="")
            
        print()
        
def add_vessel(index, row, column, direction, defend_grid) :
    size = VESSEL_SIZES[index]
    
    if (direction == 'h') :
        for column_index in range(0, size) :
            defend_grid[row][column + column_index] = size
    if (direction == 'v') :
        for row_index in range(0, size) :
            defend_grid[row + row_index][column] = size 
            
def has_overlap(index, row, column, direction, defend_grid) :
    overlap = False
    size = VESSEL_SIZES[index]
    
    if(direction == 'h') :
        for num in range(0, size):
            if(defend_grid[row][column + num] != '_') :
                overlap = True
    
    elif(direction == 'v') :
        for num in range(0, size):
            if(defend_grid[row + num][column] != '_') :
                overlap = True
    return overlap
