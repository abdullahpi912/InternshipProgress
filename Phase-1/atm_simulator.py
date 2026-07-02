balance = 0
#ATM Simulator - Loop until user chooses to exit
while True:
    print("\nWelcome to the Pybank ATM ")
    print("1.check balance")
    print("2.deposit")
    print("3.withdraw")
    print("4.exit")

    #choice input from user
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print("Your balance is: ", balance)
    
    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print("Amount deposited. New balance is: ", balance)
    
    #Checking for sufficient balance before withdrawal
    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print("Amount withdrawn. New balance is: ", balance)
    elif choice == 4:
        print("Exiting...")
        break