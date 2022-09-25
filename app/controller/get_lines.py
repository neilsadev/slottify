import random

from model.const import *

def get_slot_spin(rows, cols, syms):
    all_symbols = []
    for symbol, symbol_count in syms.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = [[],[],[]]
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(column) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()
