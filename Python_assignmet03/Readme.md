# Library Inventory Manager

## Project Overview

This is a lightweight command-line Library Inventory Manager application developed using Python and Object-Oriented Programming principles. It helps campus library staff to track book statuses (issued/available), search catalog entries, maintain persistent records in a `.txt` file, and manage the book inventory easily.

---

## Features

- Add new books with title, author, and ISBN.
- Issue and return books with status updates.
- Search books by title or ISBN.
- View all books in the inventory.
- Persistent storage of book records in a text file (`books.txt`).
- Robust handling of missing files.
- Modular code structure with clear separation of concerns.
- Simple and interactive command-line interface (CLI).

---

## Project Structure

library_inventory_project/
│
├── library_manager/
│ ├── init.py
│ ├── book.py
│ └── inventory.py
│
├── cli/
│ └── main.py
│
├── books.txt
├── README.md
└── requirements.txt


- `library_manager/` : Package containing `Book` and `LibraryInventory` classes.
- `cli/` : Contains the `main.py` CLI interface.
- `books.txt` : Stores the current book catalog in text format.
- `README.md` : This documentation file.
- `requirements.txt` : Lists project dependencies (none external for this project).

---
## Usage Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/library-inventory-manager-yourname.git
cd library-inventory-manager-yourname
python cli/main.py


<img width="1102" height="915" alt="image" src="https://github.com/user-attachments/assets/ce64075f-2d93-428a-8deb-bc1223ad7d93" />

