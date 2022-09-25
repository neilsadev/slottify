MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def depos():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    
    return amount

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

def main():
    balacnce = depos()
    lines = get_number_of_lines()
    print(balacnce, lines)

main()