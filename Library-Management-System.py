class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")
    
    def __del__(self):
        self.file.close()
    
    def list_books(self):
        self.file.seek(0)
        content = self.file.read()
        books = content.splitlines()
        print("Books in the library:")
        for book in books:
            book_info = book.split(",")
            print(f"{book_info[0]}-{book_info[2]} by {book_info[1]}")
    
    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the book author: ")
        year = input("Enter the first release year: ")
        pages = input("Enter the number of pages: ")
        book = f"{title},{author},{year},{pages}\n"
        self.file.write(book)
        print(f"{title} by {author} added to the library.")
    
    def remove_book(self):
        title = input("Enter the book title to remove: ")
        self.file.seek(0)
        content = self.file.read()
        books = content.splitlines()
        index = -1
        for i, book in enumerate(books):
            book_info = book.split(",")
            if book_info[0] == title:
                index = i
                break
        if index != -1:
            books.pop(index)
            self.file.truncate(0)
            for book in books:
                self.file.write(book + "\n")
            print(f"{title} removed from the library.")
        else:
            print(f"{title} not found in the library.")

lib = Library()

while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
