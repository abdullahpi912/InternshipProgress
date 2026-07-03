# ============================================================
# Local vs Global scope
# ============================================================
attendance = 20  # global variable

def show_attendance_wrong():
    attendance = 0  # creates a NEW local variable, doesn't touch the global one
    print(f"Inside function: {attendance}")

show_attendance_wrong()
print(f"Outside function (unchanged): {attendance}")  # still 20

# def mark_present_wrong():
#     attendance = attendance + 1  # UnboundLocalError -- Python sees 'attendance' as local

def mark_present(current_count): return current_count + 1  # take it, return it
attendance = mark_present(attendance)
print(f"Correct pattern: {attendance}")  # 21

# Rule: functions take what they need as parameters and return results --
# avoid relying on global variables.
