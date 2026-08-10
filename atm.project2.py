balance = 5000 
def show_menu():
    print("1 : check balance")
    print("2 : deposit")
    print("3 : withdraw")
    print("4 : exit")
show_menu()  

def check_balance(balance):
    print("Current balance :", balance)

def deposit(balance):
    amount = int(input("enter the deposit amount : "))
    balance = balance + amount
    return balance

def withdraw(balance):
    print("your balance is :", balance)
    withdraw_amount=int(input("enter withdraw amount :" ))
    balance=balance - withdraw_amount
    return balance

while True:
    choice =int(input("select your number :"))

    if choice == 1 :
        check_balance(balance)
    elif choice == 2 :
        balance=deposit(balance)
    elif choice == 3 :
        balance=withdraw(balance)
    else :
        print("exit")