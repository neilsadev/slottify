from model.const import *

def get_number_of_lines():
    while True:
        lines = input("Number of lines you want to bet on (1=" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines. ")
        else:
            print("Please enter a number.")
    
    return lines