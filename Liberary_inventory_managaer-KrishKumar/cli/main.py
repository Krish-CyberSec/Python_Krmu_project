import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library_manager import Book, LibraryInventory

FILENAME = "books.txt"

def menu():
    print("\n===== Library Inventory Manager =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")
    return input("Enter your choice: ")

def main():
    inventory = LibraryInventory()
    inventory.load_from_file(FILENAME)

    while True:
        choice = menu()

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN number: ")

            inventory.add_book(Book(title, author, isbn))
            print("Book added successfully.")

        elif choice == "2":
            isbn = input("Enter ISBN to issue: ")
            books = inventory.search_by_isbn(isbn)

            if books:
                try:
                    books[0].issue()
                    print("Book issued successfully.")
                except Exception as e:
                    print(e)
            else:
                print("Book not found.")

        elif choice == "3":
            isbn = input("Enter ISBN to return: ")
            books = inventory.search_by_isbn(isbn)

            if books:
                try:
                    books[0].return_book()
                    print("Book returned successfully.")
                except Exception as e:
                    print(e)
            else:
                print("Book not found.")

        elif choice == "4":
            inventory.display_all()

        elif choice == "5":
            title = input("Enter title to search: ")
            results = inventory.search_by_title(title)

            if results:
                for book in results:
                    print(book)
            else:
                print("No matching book found.")

        elif choice == "6":
            inventory.save_to_file(FILENAME)
            print("Library saved. Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
