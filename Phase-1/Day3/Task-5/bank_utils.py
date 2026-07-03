# ============================================================
# bank_utils.py — a CUSTOM MODULE, imported into atm_simulator_v3.py
# ============================================================
from datetime import datetime

def format_currency(amount):
    # Format a number as currency, e.g. 5000 -> 'Rs. 5,000.00'
    return f"Rs. {amount:,.2f}"

def is_valid_amount(amount):
    return amount > 0  # True if amount is positive

def build_log_line(txn_type, amount, balance_after):
    # Build one formatted, fixed-decimal line for the transaction log
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"{timestamp} | {txn_type:<10} | amount={amount:<10.2f} | balance={balance_after:.2f}\n"