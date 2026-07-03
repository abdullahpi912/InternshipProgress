# campus_lib.py -- CampusLib: a library borrow/return system
from datetime import datetime
import library_utils

books = []  # list of dicts: {"title", "author", "available"}

def add_book(title, author):
    books.append({"title": title, "author": author, "available": True})

def list_books():
    print("No books in catalog yet." if not books else "\n".join(library_utils.format_book_line(b) for b in books))

def log_action(action, title):
    # Append a timestamped record to borrow_log.txt
    with open("borrow_log.txt", "a") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | {action} | {title}\n")

def borrow_book(title):
    book = library_utils.find_book(books, title)
    if not book: print("Book not found.")
    elif not book["available"]: print("Book is already borrowed.")
    else:
        book["available"] = False
        log_action("BORROWED", title)
        print(f"You borrowed '{title}'.")

def return_book(title):
    book = library_utils.find_book(books, title)
    if not book: print("Book not found.")
    elif book["available"]: print("This book was not borrowed.")
    else:
        book["available"] = True
        log_action("RETURNED", title)
        print(f"You returned '{title}'.")

def view_log():
    # Read and print the full borrow/return history
    try:
        with open("borrow_log.txt", "r") as f:
            print("--- Borrow Log ---\n" + f.read())
    except FileNotFoundError:
        print("No borrow log yet -- borrow or return a book first.")

def summarize_library(**stats):
    # Bonus: end-of-day report using **kwargs
    print("===== END OF DAY REPORT =====")
    for k, v in stats.items():
        print(f"{k}: {v}")

def main():
    add_book("Clean Code", "Robert C. Martin")
    add_book("Atomic Habits", "James Clear")

    # Menu options mapped to their functions
    actions = {
        "1": lambda: list_books(),
        "2": lambda: borrow_book(input("Enter book title to borrow: ")),
        "3": lambda: return_book(input("Enter book title to return: ")),
        "4": lambda: view_log(),
    }

    while True:
        print("\n===== WELCOME TO CAMPUSLIB =====")
        print("1. List Books  2. Borrow  3. Return")
        print("4. View Borrow Log   5. Exit")
        choice = input("Choose an option: ")

        if choice == "5":
            available = sum(b["available"] for b in books)
            summarize_library(total_books=len(books), available=available, borrowed=len(books) - available)
            print("Exiting CampusLib...")
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Invalid choice, try again.")

main()