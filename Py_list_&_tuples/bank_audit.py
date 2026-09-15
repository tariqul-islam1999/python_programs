"""
Bank Ledger Audit System
-------------------------
Audits transaction histories using a list of transaction tuples
tracks running balances, flags overdrawn states and generate an 
audit report with fees 

"""
account_holder = "Tariqul Islam"
account_number = "ACC-20260915"
starting_balance = 15000.00
overdraft_fee = 15 # penalty for negative transactions

# Transaction Details
transactions = [
    ("TXN-101", "2026-09-01 10:00", "Deposit", 700.00),
    ("TXN-102", "2026-09-12 13:15", "Withdrawal", 12000.00),
    ("TXN-103", "2026-09-14 16:50", "Withdrawal", 4000.00),
    ("TXN-104", "2026-09-01 10:00", "Deposit", 500.00),
    ("TXN-105", "2026-09-12 13:15", "Withdrawal", 200.00)
]

# Audit Variables
running_balance = starting_balance
flagged_transactions = []
total_deposits = 0.0
total_withdrawals = 0.0
penalty_count = 0

print("=========================================================================")
print(f"AUDIT REPORT FOR : {account_holder} | Acct No. : {account_number}")
print(f"Starting Balance : ${starting_balance}")
print("========================================================================\n")

for trans in transactions:
    trans_id,trans_date,trans_type,amount = trans # unpacking the tuple

    if trans_type == "Deposit":
        running_balance += amount
        total_deposits += amount
        status = "OK"

    elif trans_type == "Withdrawal":
        running_balance -= amount
        total_withdrawals += amount

        # checking for the negative withdrawal
        if running_balance <0:
            status = "FLAGGED (OVERDRAFT)"
            penalty_count += 1
            running_balance -= overdraft_fee # apply penalty
            flagged_transactions.append((trans_id,amount,running_balance))

        else:
            status = "OK"

    print(f"[{trans_date}] {trans_id} | {trans_type:<10} | Amt : ${amount:>7.2f} | Bal : ${running_balance:>8.2f} | Status : {status} ") 

print("\n======================================================================")
print("                                 AUDIT SUMMARY                           ")
print("========================================================================")
print(f"Total Deposits      : ${total_deposits:.2f}")
print(f"Total Withdrawals   : ${total_withdrawals:.2f}")
print(f"Overdraft Penalties ({penalty_count}) : ${penalty_count*overdraft_fee:.2f}")
print(f"Final Account Balance : ${running_balance:.2f}")

# flagged transactions
if flagged_transactions:
    print("\n[!] WARNING: Account violated minimum balance rules.")
    print("    Flagged Transactions : ")
    for flag in flagged_transactions:
        print(f"    ID: {flag[0]} | Requested : ${flag[1]:.2f} | Post-Fee Balance: ${flag[2]:.2f}")
print("=========================================================================")
