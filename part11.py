# Class Methods
# Assignment: Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book: 
    total_books = 0
    def __init__(self):
        Book.increment_book_count()
        
    @classmethod #a method that is bound to the class and not the instance of the class, we don't have to pass the first argument as self instead we pass class(cls) as first argument
    def increment_book_count(cls):
        cls.total_books += 1
        print(cls.total_books)
    

book1 = Book()
book2 = Book()
book3 = Book()
book4 = Book()
book5 = Book()