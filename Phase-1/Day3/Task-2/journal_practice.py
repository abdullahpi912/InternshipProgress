# Function for append
from datetime import datetime

def add_entry(text):
    # Generate a timestamp for when the entry is added
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("journal.txt", "a") as f:
        f.write(f"{timestamp} | {text}\n")

def show_entries():
    # Read and print every line stored in journal.txt
    with open("journal.txt", "r") as f:
        for line in f:
            print(line.strip())

# Add three journal entries with different text
add_entry("This is my first journal entry.")
add_entry("This is my second journal entry.")
add_entry("This is my third journal entry.")

# Display all saved entries
show_entries()