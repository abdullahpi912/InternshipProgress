# ============================================================
# Functions — beyond the basics
# ============================================================
def add(a, b): return a + b
print(add(4, 5))  # 9

def greet(name, greeting="Hello"): return f"{greeting}, {name}!"  # default param
print(greet("Abd"), "|", greet("Abd", "Welcome back"))

def describe_transaction(amount, txn_type, note=""):  # keyword args, order-free
    return f"[{txn_type.upper()}] amount={amount} note={note}"
print(describe_transaction(txn_type="withdraw", amount=750, note="hostel fees"))

def average_and_range(numbers):  # multiple return values
    return sum(numbers) / len(numbers), max(numbers) - min(numbers)
avg, spread = average_and_range([72, 88, 91, 65, 80])
print(f"average={avg} range={spread}")

def total_marks(*scores): return sum(scores)  # *args -- any number of args
print(total_marks(85, 90, 78), total_marks(85, 90, 78, 92))

def build_profile(**info):  # **kwargs -- any number of named args
    return "\n".join(f"{k}: {v}" for k, v in info.items())
print(build_profile(name="Abd", course="AI & DS", year=2))
