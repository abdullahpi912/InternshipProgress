# ============================================================
# fittrack_analytics.py -- Task 5: FitTrack Analytics
# Reads a week of step data and builds a full fitness report
# using NumPy (mean, normalization, boolean masks, argsort).
# ============================================================
import numpy as np
import time
 
LOG_FILE = "steps_log.txt"
GOAL = 8000  # daily step goal
 
# --- Step 1: Create a sample log file if one doesn't already exist ---
with open(LOG_FILE, "w") as f:
    f.write("Monday:8500\nTuesday:7000\nWednesday:9100\nThursday:6800\n"
             "Friday:12000\nSaturday:5500\nSunday:9800")
 
# --- Step 2: Read the file safely, falling back to sample data if missing ---
try:
    with open(LOG_FILE, "r") as f:
        lines = f.readlines()
except FileNotFoundError:
    print(f"{LOG_FILE} not found. Using sample data instead.")
    lines = ["Monday:8500", "Tuesday:7000", "Wednesday:9100", "Thursday:6800",
              "Friday:12000", "Saturday:5500", "Sunday:9800"]
 
# --- Step 3: Parse each line into a dictionary of {day: steps} ---
fit_dict = {}
for line in lines:
    day, steps = line.strip().split(":")
    fit_dict[day] = int(steps)
 
days = list(fit_dict.keys())            # keeps Monday->Sunday order
steps_arr = np.array(list(fit_dict.values()))  # convert values to a NumPy array
 
# --- Step 4: Core stats -- mean, max, min ---
mean_steps = steps_arr.mean()
max_steps = steps_arr.max()
min_steps = steps_arr.min()
 
# --- Step 5: Normalize every value to a 0-1 range (vectorized, no loop) ---
normalized = (steps_arr - min_steps) / (max_steps - min_steps)
 
def goal_rate(arr, goal):
    # Boolean mask: True for each day that hit the goal, then % of Trues
    hit_goal = arr >= goal
    return hit_goal.mean() * 100
 
# --- Step 6: argmax/argmin -- most and least active day ---
most_active_day = days[steps_arr.argmax()]
least_active_day = days[steps_arr.argmin()]
 
# --- Step 7: argsort -- rank the whole week highest to lowest ---
rank_order = steps_arr.argsort()[::-1]  # argsort is ascending by default, so reverse it
 
# --- Step 8: Build the report ---
print("===== FITTRACK WEEKLY REPORT =====")
print(f"Mean steps   : {mean_steps:.2f}")
print(f"Max steps    : {max_steps} ({most_active_day})")
print(f"Min steps    : {min_steps} ({least_active_day})")
print(f"Goal rate    : {goal_rate(steps_arr, GOAL):.1f}% of days hit {GOAL} steps")
 
print("\nNormalized scores (0-1):")
for day, score in zip(days, normalized):
    print(f"  {day:<10}: {score:.2f}")
 
print("\nWeekly ranking (highest to lowest):")
for rank, idx in enumerate(rank_order, start=1):
    print(f"  {rank}. {days[idx]:<10} - {steps_arr[idx]} steps")
 
# --- Bonus: NumPy vs plain loop speed comparison ---
big_data = np.random.randint(1000, 15000, size=1_000_000)  # large dataset to make the gap visible
 
start = time.perf_counter()
_ = big_data.mean()  # vectorized NumPy mean
numpy_time = time.perf_counter() - start
 
start = time.perf_counter()
total = 0
for val in big_data:      # plain Python loop doing the same sum
    total += val
_ = total / len(big_data)
loop_time = time.perf_counter() - start
 
print("\n===== BONUS: NumPy vs Loop Speed =====")
print(f"NumPy time : {numpy_time:.5f} sec")
print(f"Loop time  : {loop_time:.5f} sec")
print(f"NumPy was {loop_time / numpy_time:.1f}x faster")