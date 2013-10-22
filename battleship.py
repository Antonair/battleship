import grid
import human
import t09_2_ai

def main() :
    human.info()
    
    human.get_location(0)
    for num in range(1, grid.NUM_OF_VESSELS) :
        human.get_location(num)
        
    print("====================================")    
    print("The AI's grid will now be displayed.")
    print("====================================")
        
    t09_2_ai.get_location(0)
    for num in range(1, grid.NUM_OF_VESSELS) :
        t09_2_ai.get_location(num)
    human.enter_choice()
    
main()
