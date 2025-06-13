class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
        
    def isCheckedOut(self):
        return self._is_checked_out
    
    def check_out(self):
        self._is_checked_out = True
        
    def return_book(self):
        self._is_checked_out = False
        
class Library:
    def __init__(self):
        self._books = []
        
    def add_book(self, Book):
        self._books.append(Book)
        
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                book.check_out()
                
    def return_book(self, title):
        for book in self._books:
            if book.title == title and book.isCheckedOut():
                book.return_book()
                
    def list_available_books(self):
        for book in self._books:
            if not book.isCheckedOut():
                print(f"{book.title} by {book.author}")