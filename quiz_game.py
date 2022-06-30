import sys
import csv

def main():
    print(f"{'#'*25} Welcome to Python Quiz Game! {'#'*25}\n")
    
    while True:
        play_input = input(f"{'#'*10} Do you want to start the game? (Y/N) {'#'*10}\n").lower()
        if play_input.isalpha(): # if all the characters are alphabet letters
            if play_input in ["yes","y"]:
                break
            else:
                sys.exit()
        else:
            print(f"{'#'*10} Invalid input. Please try again. {'#'*10}\n")
    


        
    
    
    
    
        
        

        
# use init for every code?
# 10 questions
# ask whether player wanna start the quiz?
# 30 secs timer for each questions or skip to next questions



if __name__ == '__main__':
    main()
    
    print("Proceed to play game, happy happy")
    
    # with open("dataset/quiz_game_dataset.csv", "r") as csv_file:
    #     csv_obj = csv.reader(csv_file)
        
    #     for i in csv_obj:
    #         pass
    #         print(i)
    #         print(type(i))
            

# testing second push

