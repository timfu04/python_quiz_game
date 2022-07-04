import sys
import csv
import os
import time
import inspect
import random

def clear_screen(s1 : int, s2 : int):
    time.sleep(s1)
    os.system("cls")
    time.sleep(s2)
    
def main ():
    clear_screen(0, 0.1)
    welcome_msg = f"""
    {"#"*50}
    ##{" "*46}##
    ##{" "*9}Welcome to Python Quiz Game!{" "*9}##
    ##{" "*46}##
    {"#"*50}
    """   
    welcome_msg = inspect.cleandoc(welcome_msg)
    print(welcome_msg,'\n')
    
    invalid_input_msg = "\033[1mINVALID INPUT. PLEASE TRY AGAIN.\033[0m"
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
                clear_screen(0.75, 0.25)
        else:
            print(invalid_input_msg)
            clear_screen(0.75, 0.25)
           
def timer_in_secs(s : int, length : int, padding : int) -> bool:
    '''
    Countdown timer in seconds.
    '''
    timer_ended = False
    while s:
        print(f"{f'00:{s:02}':^{length + padding * 2}}", end="\r")
        time.sleep(1)
        s -= 1
        if s == 0:
            timer_ended = True
    return timer_ended

def print_msg_box(msg : str, index : int):
    '''
    Print message with box
    '''
    padding = 1
    space = " " * padding
    title = f"Question {index}"
    lines = msg.split("\n")
    length = max(map(len, lines))
    
    box = f"╔{'═'*(length + padding * 2)}╗\n" # top border
    box += f"║{space}\033[1m{title:<{length}}\033[0m{space}║\n" # title
    box += f'║{space}{"-" * len(title):<{length}}{space}║\n'  # title underscore
    box += "".join([f"║{space}{line:<{length}}{space}║\n" for line in lines]) # content
    box += f"╚{'═'*(length + padding * 2)}╝" # bottom border
    print(box)
    return length, padding




def display_ques(csv_data: list):
    '''
    Shuffle and display questions.
    '''
    random.shuffle(csv_data)
    clear_screen(0, 0)
    
    for index, data in enumerate(csv_data):
        length, padding = print_msg_box(data["question"], index + 1)
        timer_in_secs(10, length, padding)
        clear_screen(0, 1)
        
        
    
    
    




if __name__ == '__main__':
    main()
    
    # Read dataset into list of dictionaries 
    csv_data_list = []
    with open("dataset/quiz_game_dataset.csv", "r") as csv_file:
        csv_obj = csv.DictReader(csv_file)
        
        for data in csv_obj:
            csv_data_list.append({"question":data["ques"], "options":[data["opt_1"], data["opt_2"], data["opt_3"], data["opt_4"]], "answer":data["ans"]})
      
      
      
      
      
      
    display_ques(csv_data_list)