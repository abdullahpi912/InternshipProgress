# receipt_practice.py

def build_receipt(**details):
    receipt = ""
    for key, value in details.items():
        receipt += f"{key}: {value}\n"
    return receipt


# Call it with different sets of details each time
print(build_receipt(name="Abdullah", amount=250, type="Deposit"))

print(build_receipt(name="Noor", amount=1000, type="Withdrawal", branch="Chennai"))

print(build_receipt(item="Notebook", price=45))