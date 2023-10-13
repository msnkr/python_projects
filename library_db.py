
class Library():
    def __init__(self):
        self.books = []

    def add_books(self, book):
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return True
        return False

    def list_books(self):
        if not self.books:
            print("The library is empty")
        else:
            print("Library catalag")
            for i, book in enumerate(self.books):
                print(f"{i}. Title: {book.title}, Author: {book.author}")


class Book():
    def __init__(self, author, title):
        self.author = author
        self.title = title


def main():
    library = Library()

    while True:

        print("1. Add a book: ")
        print("2. View all books: ")
        print("3. Delete a book: ")
        print("4. Quit: ")

        choice = int(input("Make a choice: "))

        if choice == 1:
            author = input("Authors name: ")
            title = input("Title name: ")

            book = Book(author, title)
            library.add_books(book)

        elif choice == 2:
            library.list_books()

        elif choice == 3:
            title = input("Enter the title: ")
            library.remove_book(title)

        elif choice == 4:
            print("Goodbye")
            break


if __name__ == "__main__":
    main()
