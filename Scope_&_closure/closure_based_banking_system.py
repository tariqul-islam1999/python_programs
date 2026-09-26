"""
Closure-Based Bank Account System
----------------------------------
simulated a closure-based bank account system without class. Balance is encapsulated
inside closure as a "private" state. It can't give access from outside, only deposit,
withdraw & check_balance function can get access.

"""
from datetime import datetime
def create_account(owner_name,initial_balance=0):
    balance = initial_balance
    transaction_log= []

    def log(action,amount):
        transaction_log.append({
            "action" : action,
            "amount" : amount,
            "balance_after" : balance,
            "time" : datetime.now().strftime("%H:%M:%S")
        })

    def deposit(amount):
        nonlocal balance

        if(amount<0):
            print("Deposit must be positive amount")
            return balance
        balance += amount
        log("DEPOSIT",amount)
        print(f"Deposited : {amount} | New Balance : {balance}")
        return balance

    def withdraw(amount):
        nonlocal balance

        if(amount<0):
            print("Withdrawal must be positive amount")
            return balance
        if(amount>balance):
            print(f"Insufficient funds. Current balance: {balance}")
            return balance
        balance -= amount
        log("WITHDRAW",amount)
        print(f"Withdrew : {amount} | New Balance : {balance}")

    def check_balance():
        print(f"{owner_name}'s Balance : {balance}")

    def print_statement():
        print(f"======================= Statement For {owner_name} =======================")
        for transaction in transaction_log:
            print(f"[{transaction['time']}] | {transaction['action']} | {transaction['amount']} | {transaction['balance_after']}")
            print("========================================================================")

    return{
        "deposit" : deposit,
        "withdraw" : withdraw,
        "check_balance" : check_balance,
        "print_statement" : print_statement
    }


print("=== Demo: Closure-based Bank Account ===\n")

rahim_account = create_account("Rahim", initial_balance=1000)
karim_account = create_account("Karim", initial_balance=500)

rahim_account["deposit"](500)
rahim_account["withdraw"](200)
rahim_account["check_balance"]()

karim_account["deposit"](100)
karim_account["withdraw"](10000)  # will fail - insufficient funds
karim_account["check_balance"]()

rahim_account["print_statement"]()
karim_account["print_statement"]()
        
