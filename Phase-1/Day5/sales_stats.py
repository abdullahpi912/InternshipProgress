import numpy as np

sales = np.array([25000, 32000, 15000, 40000, 45000, 30000, 34000])

print(f"Mean of sales : {sales.mean():.2f}")
print(f"Max of sales : {sales.max()}")
print(f"Min of sales : {sales.min()}")
print(f"7 days total of sales : {sales.sum()}")

# Boolean mask to find and count how many days were above the weekly average
above_average = sales > sales.mean()
print(f"Above-average mask: {above_average}")
print(f"Days above average: {above_average.sum()}")