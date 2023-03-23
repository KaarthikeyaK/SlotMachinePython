MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

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
    bet = getBet()
    totalBet = bet * lines
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${totalBet}")
    print(balance, lines)

main()