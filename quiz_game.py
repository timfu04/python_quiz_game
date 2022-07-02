import sys
import csv
import os
import time
import inspect





def read_csv():
    pass
    

def clear_screen():
    time.sleep(0.75)
    os.system("cls")
    time.sleep(0.25)    

def main ():
    welcome_msg = f"""
    {"#"*50}
    ##{" "*46}##
    ##{" "*9}Welcome to Python Quiz Game!{" "*9}##
    ##{" "*46}##
    {"#"*50}
    """   
    welcome_msg = inspect.cleandoc(welcome_msg)
    print(welcome_msg,'\n')
    
    invalid_input_msg = "INVALID INPUT. PLEASE TRY AGAIN."
    while True:
        play_input = input("Do you want to start the game (Y/N)?\n").lower()
        if play_input.isalpha(): # if all the characters are alphabet letters
            if play_input in ["yes","y"]:
                break
            elif play_input in ["no",'n']:
                print("quit game")
                sys.exit()
            else:
                print(invalid_input_msg)
                clear_screen()
        else:
            print(invalid_input_msg)
            clear_screen()
           
            



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

