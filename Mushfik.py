class Book:
    def __init__(self, title, author, isbn):
        """Initialize book details."""
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        """Display book information."""
        print(f"\nTitle: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")


class Library:
    def __init__(self):
        """Initialize book collection."""
        self.books = []

    def add_book(self):
        """Add a new book."""
        title = input("\nEnter Book Title: ")
        author = input("Enter Author: ")
        isbn = input("Enter ISBN: ")
        book = Book(title, author, isbn)
        self.books.append(book)
        print("Book added successfully!")

    def view_books(self):
        """Display all books."""
        if not self.books:
            print("\nNo books available.")
            return
        print("\nLibrary Books:")
        for book in self.books:
            book.display_info()

    def delete_book(self):
        """Delete a book by ISBN."""
        if not self.books:
            print("\nNo books available to delete.")
            return
        isbn = input("\nEnter ISBN to delete: ")
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book with ISBN {isbn} deleted successfully!")
                return
        print("Book not found!")

    def run(self):
        """Main loop with options."""
        while True:
            print("\n========================")
            print(" Library Management")
            print("========================")
            print("1. Add Book")
            print("2. View Books")
            print("3. Delete Book")
            print("4. Exit")
            print("========================")
            choice = input("Select an option: ")
            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.view_books()
            elif choice == "3":
                self.delete_book()
            elif choice == "4":
                print("Exiting program... Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    library = Library()
    while True:  # Infinite loop to restart after exiting main menu
        library.run()
        restart = input("\nDo you want to restart the Library Manager? (yes/no): ").strip().lower()
        if restart != "yes":
            print("Goodbye!")
            break

