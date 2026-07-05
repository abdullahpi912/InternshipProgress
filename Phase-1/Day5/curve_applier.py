import numpy as np

raw_scores = np.array([58, 72, 65, 80, 45, 90, 68])  # exam scores before curve
curved_scores = raw_scores + 4  # vectorized -- adds 4 to every score at once, no loop

print("Raw scores:", raw_scores)
print("Curved scores:", curved_scores)

#Print the original mean and the curved mean side by side.
print(f"Raw mean: {raw_scores.mean():.2f} | Curved mean: {curved_scores.mean():.2f}")
