# ============================================================
# atm_simulator_v3.py — LIVE BUILD for Day 3
# Refactors the Day 2 ATM Simulator into functions + a custom
# module + file-based transaction logging.
# ============================================================
from bank_utils import format_currency, is_valid_amount, build_log_line

LOG_FILE = "transactions.log"

def show_menu():
    print("\n===== WELCOME TO PYBANK ATM =====")
    print("1. Check Balance   2. Deposit")
    print("3. Withdraw        4. View Transaction History")
    print("5. Exit")

def log_transaction(txn_type, amount, balance_after):
    # Append a formatted transaction line to the log file
    with open(LOG_FILE, "a") as f:
        f.write(build_log_line(txn_type, amount, balance_after))

def check_balance(balance):
    print(f"Balance: {format_currency(balance)}")

def deposit(balance):
    amount = float(input("Enter deposit amount: "))
    if not is_valid_amount(amount):
        print("Deposit must be a positive amount.")
        return balance
    balance += amount
    log_transaction("DEPOSIT", amount, balance)
    print(f"Deposit successful! New balance: {format_currency(balance)}")
    return balance

def withdraw(balance):
    amount = float(input("Enter withdrawal amount: "))
    if not is_valid_amount(amount) or amount > balance:
        print("Invalid withdrawal amount.")
        return balance
    balance -= amount
    log_transaction("WITHDRAW", amount, balance)
    print(f"Withdrawal successful! New balance: {format_currency(balance)}")
    return balance

def view_history():
    # Print every logged transaction, or a message if none exist
    print("\n--- Transaction History ---")
    try:
        with open(LOG_FILE, "r") as f:
            lines = f.readlines()
        print("No transactions yet." if not lines else "".join(lines))
    except FileNotFoundError:
        print("No transactions yet.")

def run_atm():
    balance, transaction_count = 5000, 0

    actions = {"1": check_balance, "2": deposit, "3": withdraw}

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice in ("2", "3"):
            new_balance = actions[choice](balance)
            transaction_count += new_balance != balance
            balance = new_balance
        elif choice == "1":
            check_balance(balance)
        elif choice == "4":
            view_history()
        elif choice == "5":
            print(f"Total transactions this session: {transaction_count}")
            print("Thank you for using PyBank ATM.")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    run_atm()