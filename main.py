import random


MAX_LINES=3
MAX_BET=100            #global values which can be used anywhere withought changing them
MIN_BET=1

ROWS=3
COLS=3

symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":20
}
symbol_value={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}
def check_winnigs(columns,lines,bet,values):
    winnings=0
    winning_line=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings+= values[symbol]*bet
            winning_line.append(line+1)

    return winnings,winning_line




def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):     #when we only want to iterate without having to do with any task we use _
            all_symbols.append(symbol)

    columns=[]
    for _ in range(cols):
        column=[]
        current_symbols=all_symbols[:]        #slice operator coz cur_sum would store reference of all_sumrather than value 
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,col in enumerate(columns):
            if(i != len(columns)-1):
                print(col[row], end=" | ")
            else:
                print(col[row],end="")
        print()

def deposit():
    while True:
        amount=input("What would you like to deposte ? $")
        if amount.isdigit():
            amount=int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero")
        else:
            print("please enter a number")
    return amount


def get_bet():
    while True:
        amount=input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET<=amount<= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET}-{MAX_BET}")
        else:
            print("please enter a number")
    return amount

def get_number_of_lines():
    while True:
        # lines=input("How many lines you wanna bet on (1-" + str(MAX_LINES) + ")? " )
        lines=input(f"How many lines you wanna bet on (1-{MAX_LINES})? " )

        if lines.isdigit():
            lines=int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("please enter a number")
    return lines

def spin(balance):
    lines=get_number_of_lines()

    while True:
        bet=get_bet()
        total_bet=lines*bet
        if(total_bet>balance):
            print("you are out of balance")
        else:
            break
        
    print(f"you are betting ${bet} on {lines} lines, total bet is ${total_bet}")


    slots=get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings, winning_line=check_winnigs(slots,lines,bet,symbol_value)
    print(f"you won {winnings} ")
    print(f"you won on lines " ,*winning_line)

    return winnings-total_bet


def main():
    balance= deposit()
    while True:
        print(f"current balance is {balance}")
        answer=input("press enter to play (q to quit)")
        if answer=="q":
           break
        balance+=spin(balance)

    print(f"you left with {balance}")
    

main()