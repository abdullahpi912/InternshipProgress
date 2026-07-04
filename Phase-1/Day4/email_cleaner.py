# ============================================================
# email_cleaner.py -- Task 4: Duplicate Email Cleaner (Set)
# ============================================================
signup_list = [
    "abd@example.com",
    "priya@example.com",
    "rahul@example.com",
    "abd@example.com",       # duplicate
    "sneha@example.com",
    "rahul@example.com",     # duplicate
    "kavya@example.com",
    "arjun@example.com",
    "priya@example.com",     # duplicate
]

unique_emails = set(signup_list)  # sets automatically drop duplicates, order not kept

duplicates_removed = len(signup_list) - len(unique_emails)

print(f"Original entries: {len(signup_list)}")
print(f"Unique emails: {len(unique_emails)}")
print(f"Duplicates removed: {duplicates_removed}")
