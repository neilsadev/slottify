from model.const import *
from controller.bet import get_bet
from controller.depos import depos
from controller.lines import get_number_of_lines
from controller.get_lines import get_slot_spin, print_slot_machine

def main():
    balacnce = depos()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet

        if total_bet > balacnce:
            print(f"You do not have enough balance to bet that amount, your current balance is ${balacnce}")
        else:
            break

    slots = get_slot_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    print(f"You are betting ${bet} on {lines} lines. Your total bet is: ${total_bet}")
    