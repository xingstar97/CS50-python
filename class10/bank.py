# WRONG: 
balance = 0

def main():
    # WRONG: balance = 0
    print("Balance: ", balance)
    deposit(100)
    withdraw(50)
    print("Balance: ", balance)

def deposit(n):
    global balance
    balance +=n
    # without global, this function declare a local variable called balance and change the local variable
    


def withdraw(n):
    global balance
    balance -=n

if __name__=="__main__":
    main()