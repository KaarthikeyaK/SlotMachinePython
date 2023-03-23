import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbolCount = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def getSlotMachineSpin(rows, cols, symbols):
    allSymbols = []
    for symbol, symbolCount in symbols.items():
        for _ in range(symbolCount):
            allSymbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        currentSymbols = allSymbols[:]
        for _ in range(rows):
            value = random.choice(currentSymbols)
            currentSymbols.remove(value)
            column.append(value)
        columns.append(column)


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        #Checking if this is actually a number
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number")
    return amount

def getNumberOfLines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <=MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("please enter a number")
    return lines

def getBet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount


def main():
    balance = deposit()
    lines = getNumberOfLines()
    while True:
        bet = getBet()
        totalBet = bet * lines
        if totalBet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${totalBet}")
    print(balance, lines)

main()