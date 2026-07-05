import numpy as np

#NumPy array to store the prices and quantities of items

prices = np.array([2.99, 1.49, 3.99, 0.99, 5.49])  # Prices of items
quantities = np.array([2, 3, 1, 5, 2])  # Quantities of items

# Calculate the total cost for each item    
line_totals = prices * quantities

for i,total in enumerate(line_totals, start=1):
    print(f"Item {i}: ${total:.2f}")

# Calculate the total bill
grand_total = line_totals.sum()

print(f"Item Prices: {prices}")
print(f"Item Quantities: {quantities}")
print(f"Line Totals: {line_totals}")
print(f"Grand Total: ${grand_total:.2f}")