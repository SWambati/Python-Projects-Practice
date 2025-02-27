
balance = 3400
option = input("Please select option: check_balance, withdrawal, deposits...")
if option == "withdrawal":
    withdraw = int(input("Enter the amount you'd like to withdraw: "))
    if withdraw > balance:
        print("You have insufficient funds")
    else:
        new_balance = balance - withdraw
        print(new_balance)
elif option == "deposits":
    deposit = int(input("How much would you like to deposit? "))
    new_balance = balance + deposit
    print(new_balance)
else:
    print(balance)


