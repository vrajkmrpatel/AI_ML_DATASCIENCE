""" 
Library management system
 
Create class LibraryItem
    Attributes: title, author, item_id, item_type
    method: calculate_late_fee(days)
Create subclasses:
    Book
    Magazine
    DVD
Each subclass:
    Implements different late fee logic.
    Keeps track of borrowed status.
    Raises exception if trying to borrow an already borrowed item.
Create a Library class that:
    Stores collection of items
    Allows:
        add_item()
        borrow_item()
        return_item()
        search_by_title()
"""


class LibraryItem:
    """"Base class for library items."""

    def __init__(self, title: str, author: str, item_id: int, item_type: str):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.item_type = item_type
        self.is_borrowed = False
    
    def calculate_late_fee(self, days: int) -> float:
        """Calculate late fee based on item type."""
        raise NotImplementedError("Subclasses must implement this method.")

class Book(LibraryItem):
    """Class representing a book in the library."""

    def __init__(self, title, author, item_id, item_type):
        super().__init__(title, author, item_id, item_type)
    
    def calculate_late_fee(self, days: int) -> float:
        return days * 0.5

class Magazine(LibraryItem):
    """Class representing a magazine in the library."""

    def __init__(self, title, author, item_id, item_type):
        super().__init__(title, author, item_id, item_type)
    
    def calculate_late_fee(self, days: int) -> float:
        return days * 0.25

class DVD(LibraryItem):
    """Class representing a DVD in the library."""

    def __init__(self, title, author, item_id, item_type):
        super().__init__(title, author, item_id, item_type)
    
    def calculate_late_fee(self, days: int) -> float:
        return days * 1.0


class Library:
    """Class representing the library."""

    def __init__(self, items: list[LibraryItem] = None):
        self.items = items if items is not None else [] 
    
    def add_item(self, item: LibraryItem):
        print(f"Adding item: {item.title}")
        self.items.append(item)
    
    def borrow_item(self, item: LibraryItem):
        if self.is_empty():
            raise ValueError("No items available in the library.")
        if item.is_borrowed:
            raise ValueError("Item is already borrowed.")
        item.is_borrowed = True
        print(f"Borrowing item: {item.title}")
        self.items.remove(item)
        
    def return_item(self, item: LibraryItem):
        if not item.is_borrowed:
            raise ValueError("Item was not borrowed.")
        print(f"Returning item: {item.title}")
        item.is_borrowed = False
        self.items.append(item)
    
    def search_by_title(self, title: str):
        for item in self.items:
            if item.title == title:
                print(f"Found item: {item.title}, Author: {item.author}, Type: {item.item_type}")
                return item
        print("Item not found.")
        return None
    
    def list_details(self):
        # Borrowed items will not be listed
        if self.is_empty():
            print("No items available in the library.")
            return
        print(f"{'-'*100}")
        for item in self.items:
            print(f"ID: {item.item_id}, Title: {item.title}, Author: {item.author}, Item-type: {item.item_type}, Borrowed: {item.is_borrowed}")
        print(f"{'-'*100}")

    def is_empty(self) -> bool:
        return len(self.items) == 0


b1: Book = Book("Harry Potter and the Chamber of Secrets", "J.K. Rowling", 1, "Book")
b2: Book = Book("Harry Potter and the Half-Blood Prince", "J.K. Rowling", 2, "Book")

m1: Magazine = Magazine("National Geographic", "Various", 3, "Magazine")
m2: Magazine = Magazine("Time", "Various", 4, "Magazine")

d1: DVD = DVD("Inception", "Christopher Nolan", 5, "DVD")
d2: DVD = DVD("The Matrix", "The Wachowskis", 6, "DVD")

# Library instance
library_items: list[LibraryItem] = [b1, b2, m1, m2, d1, d2]
l : Library = Library(library_items)

# search item
# l.search_by_title("Inception")

# adding new item 
# b3: Book = Book("The Hobbit", "J.R.R. Tolkien", 7, "Book")
# l.add_item(b3)
# l.list_details()

# borrow item
# l.borrow_item(b1)
# l.list_details()

# l.borrow_item(b1)

# Return item
# l.return_item(b1)
# l.list_details()

# Calculate late fee
# print(f"Late fee for {b1.title} for 5 days: ${b1.calculate_late_fee(5)}")
# print(f"Late fee for {m1.title} for 2 days: ${m1.calculate_late_fee(2)}")