class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(book, "added successfully")

    def show_books(self):
        if len(self.books) == 0:
            print("No books in library")
        else:
            print("Available books:")
            for i in self.books:
                print(i)

    def issue_book(self, i):
        if i in self.books:
            self.books.remove(i)
            print(i, "issued successfully")
        else:
            print("Book not available")


lib = Library()   # Object creation

lib.add_book("Python")
lib.add_book("C Programming")
lib.show_books()
lib.issue_book("Python")
lib.show_books()