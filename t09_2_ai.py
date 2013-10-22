import grid

B = '_'
defend_grid = [[B,B,B,B,B,B,B,B,B,B], \
               [B,B,B,B,B,B,B,B,B,B], \
               [B,B,B,B,B,B,B,B,B,B], \
               [B,B,B,B,B,B,B,B,B,B], \
               [B,B,B,B,B,B,B,B,B,B], \
               [B,B,B,B,B,B,B,B,B,B], \
               [B,B,B,B,B,B,B,B,B,B], \
               [B,B,B,B,B,B,B,B,B,B], \
               [B,B,B,B,B,B,B,B,B,B], \
               [B,B,B,B,B,B,B,B,B,B]]

def info() :
    print ('----------------------------------')
    print ('Captain! Ready to play Battleship?')
    print ('----------------------------------')

def get_location(vessel_index) :
    global column
    global row
    global direction
    
    import random
    
    name = grid.VESSEL_NAMES[vessel_index]
    size = grid.VESSEL_SIZES[vessel_index]

    column = random.choice('ABCDEFGHIJ')
    row = random.randint(1,10)
    direction = random.choice('hv')
    
    column = ord(column) - ord('A')
    row = row - 1
    
    if(column >= grid.GRID_WIDTH or column < 0) :
        get_location(vessel_index)
    elif(row >= grid.GRID_HEIGHT or row < 0) :
        get_location(vessel_index)
    else :
        if (direction == 'h' and column + size > grid.GRID_WIDTH) :
            get_location(vessel_index)
        elif (direction == 'v' and row + size > grid.GRID_HEIGHT) :
            get_location(vessel_index)
        else :
            if (direction != 'h' and direction != 'v') :
                get_location(vessel_index)
            else :
                overlap = grid.has_overlap(vessel_index, row, column, direction, defend_grid)
                if(overlap == True) :
                    get_location(vessel_index)
                else :
                    grid.add_vessel(vessel_index, row, column, direction, defend_grid)
                    grid.print_grid(defend_grid)               
        
def enter_choice() :
    global exit
    exit = 1
    while (exit != 'q') :
        exit = input('Enter choice: ')
