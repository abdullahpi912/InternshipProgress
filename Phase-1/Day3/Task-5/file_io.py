# ============================================================
# File I/O — read, write, append
# ============================================================
with open("study_log.txt", "w") as f:  # "w" overwrites the file each time
    f.write("Started Python basics\nCompleted control flow\n")

print(open("study_log.txt").read())  # read whole file at once

with open("study_log.txt", "r") as f:  # read line by line
    for line in f: print("LOG:", line.strip())

with open("study_log.txt", "a") as f:  # "a" appends, doesn't erase existing content
    f.write("Started functions & modules\n")

try:  # handle a missing file safely
    open("missing_log.txt", "r").read()
except FileNotFoundError:
    print("That file doesn't exist yet -- handled gracefully.")

# 'with' auto-closes the file, even if an error happens partway through.
