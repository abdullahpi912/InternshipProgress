# ============================================================
# todo_manager.py -- Task 1: To-Do List Manager (List)
# ============================================================
tasks = ["Finish Day 4 README", "Practice list comprehensions"]  # starting tasks

def add_task(task):
    tasks.append(task)  # lists are editable -- just append to the end
def complete_task(task):
    if task in tasks:
        tasks.remove(task)  # removes the first matching item

def pending_count():
    return len(tasks)

def show_pending():
    # Print the list, numbered, using a loop
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

# --- Demo run ---
add_task("Submit GradeVault")
complete_task("Practice list comprehensions")

print("Pending tasks:")
show_pending()
print(f"Total pending: {pending_count()}")
