class MyBankAccount:
    def withdraw(self):
        print("withdraw successfull")

    def verify_pin(self):
        print("pin verified")

    def check_balance(self):
        print("balance checked")

    def update_server(self):
        print("server updated")

atm = MyBankAccount

atm.verify_pin()
atm.check_balance()
atm.update_server()
atm.withdraw()