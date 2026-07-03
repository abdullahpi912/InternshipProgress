# library_utils.py -- reusable helper functions for CampusLib

def find_book(books, title):
    # Looks through the book list and returns the matching book dict, or None
    for book in books:
        if book["title"].lower() == title.lower():
            return book
    return None

def format_book_line(book):
    # Formats a single book as a clean display line
    status = "Available" if book["available"] else "Borrowed"
    return f"{book['title']} by {book['author']} -- {status}"