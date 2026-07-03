# ============================================================
# Importing OUR OWN module
# bank_utils.py must be in the same folder as this file.
# ============================================================
import bank_utils
from bank_utils import format_currency  # cleaner import -- only what you need

print(bank_utils.format_currency(2500))          # Rs. 2,500.00
print(bank_utils.is_valid_amount(-100))          # False
print(bank_utils.build_log_line("WITHDRAW", 750, 1750))
print(format_currency(9999.9))                   # Rs. 9,999.90
