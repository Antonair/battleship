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
    
    name = grid.VESSEL_NAMES[vessel_index]
    size = grid.VESSEL_SIZES[vessel_index]

    print('Enter placement of your', name, '(', size,  'spaces)')
    column = input('\tLeft Column (A-J): ')
    row = int(input('\tTop Row (1-10): '))
    direction = input('\tDirection (h)orizontal or (v)ertical: ')
    
    column = ord(column) - ord('A')
    row = row - 1
    
    if(column >= grid.GRID_WIDTH or column < 0) :
        print('The column entered is invalid, it must be a value between A and J.')
        get_location(vessel_index)
    elif(row >= grid.GRID_HEIGHT or row < 0) :
        print('The row entered is invalid, it must be between 1 and 10.')
        get_location(vessel_index)
    else :
        if (direction == 'h' and column + size > grid.GRID_WIDTH) :
            print('Invalid column. The vessel is directed horizontally to the right')
            print('and does not fit on the grid with this starting column.')
            get_location(vessel_index)
        elif (direction == 'v' and row + size > grid.GRID_HEIGHT) :
            print('Invalid row. The vessel is directed vertically downwards')
            print('and does not fit on the grid with this starting now.')
            get_location(vessel_index)
        else :
            if (direction != 'h' and direction != 'v') :
                print('The direction entered is invalid, it must be either (h)orizontal or (v)ertical.')
                get_location(vessel_index)
            else :
                overlap = grid.has_overlap(vessel_index, row, column, direction, defend_grid)
                if(overlap == True) :
                    print('The vessel entered overlaps another one! Please place your new vessel elsewhere.')
                    get_location(vessel_index)
                else :
                    grid.add_vessel(vessel_index, row, column, direction, defend_grid)           
                    grid.print_grid(defend_grid)     
        
def enter_choice() :
    global exit
    exit = 1
    while (exit != 'q') :
        exit = input('Enter choice: ')
