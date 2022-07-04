# def print_msg_box(msg, indent=1, width=None, title=None):
#     """Print message-box with optional title."""
#     lines = msg.split('\n')
#     space = " " * indent
#     if not width:
#         width = max(map(len, lines))
#     box = f'╔{"═" * (width + indent * 0)}╗\n'  # upper_border
#     if title:
#         box += f'║{space}{title:<{width}}{space}║\n'  # title
#         box += f'║{space}{"-" * len(title):<{width}}{space}║\n'  # underscore



#     box += ''.join([f'║{space}{line:<{width}}{space}║\n' for line in lines])
#     box += f'╚{"═" * (width + indent * 2)}╝'  # lower_border
#     print(box)
    
    

# print_msg_box("Hello everyone\nhahaha\nyerrrrrrr")


# split lines by newline (if got multiple lines)
# take the maximum length among these lines




# def print_msg_box(msg : str, index : int):
#     '''
#     Print message with box
#     '''
#     padding = 1
#     space = " " * padding
#     title = f"Question {index}"
#     lines = msg.split("\n")
#     length = max(map(len, lines))
    
#     box = f"╔{'═'*(length + padding * 2)}╗\n" # top border
#     box += f"║{space}\033[1m{title:<{length}}\033[0m{space}║\n" # title
#     box += f'║{space}{"-" * len(title):<{length}}{space}║\n'  # title underscore
#     box += "".join([f"║{space}{line:<{length}}{space}║\n" for line in lines]) # content
#     box += f"╚{'═'*(length + padding * 2)}╝\n" # bottom border
#     print(box)
     
# print_msg_box("What is your name harrr?\nHEHEBOI\nhuehuehue", 1)


    


    
# print('\033[1m'+ 'Hello World !' + '\033[0m') 
# print(f"\033[1mTHISISTHESTRING\033[0m")
    
    
    

a = "chicken"
b = "little"

print("Hello" + " " +  a + " " + b)

print("Hello {0} {1}".format(a, b))

print(f"Hello {a} {b}")



