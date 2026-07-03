# ============================================================
# Importing built-in modules
# ============================================================
import math, random
from datetime import datetime

print(math.sqrt(81), math.floor(7.8), round(math.pi, 3))  # 9.0 7 3.142
print(random.randint(1, 50), random.choice(["Python", "SQL", "Git"]))  # random values

print(datetime.now().strftime("%d-%m-%Y %I:%M %p"))  # today's date/time, 12-hour format
