from .book import Book

class LibraryInventory:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def search_by_isbn(self, isbn):
        return [book for book in self.books if book.isbn == isbn]

    def display_all(self):
        if not self.books:
            print("No books in library.")
            return
        
        for book in self.books:
            print(book)

    #  FILE HANDLING 

    def save_to_file(self, filename):
        try:
            with open(filename, "w") as f:
                for book in self.books:
                    line = f"{book.title}|{book.author}|{book.isbn}|{book.status}\n"
                    f.write(line)
        except Exception as e:
            print("Error saving file:", e)

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as f:
                for line in f:
                    if line.strip() == "":
                        continue
                    title, author, isbn, status = line.strip().split("|")
                    self.books.append(Book(title, author, isbn, status))
        except FileNotFoundError:
            print("No existing file found — starting with an empty library.")
        except Exception as e:
            print("Error loading file:", e)
