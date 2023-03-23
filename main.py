
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
    return

def main():
    balance = deposit()

main()