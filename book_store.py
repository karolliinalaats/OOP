"""Book store."""


class Book:
    """Represent book model."""

    def __init__(self, title: str, author: str, price: float, rating: float):
        """
        Class constructor. Each book has title, author and price.

        :param title: book's title
        :param author: book's author
        :param price: book's price
        """
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating

    def __repr__(self):
        return f"(self.title) - (self.rating)"


class Store:
    """Represent book store model."""

    def __init__(self, name: str, rating: float):
        """
        Class constructor.

        Each book store has name.
        There also should be an overview of all books present in store

        :param name: book store name
        """
        pass

        self.name = name
        self.rating = rating
        self.books = []

    def can_add_book(self, book: Book) -> bool:
        """
        Check if book can be added.

        It is possible to add book to book store if:
        1. The book with the same author and title is not yet present in this book store
        2. book's own rating is >= than store's rating
        :return: bool
        """
        pass

        return not any(existing_book.title == book.title and existing_book.author == book.author for existing_book in self.books) and book.rating >= self.rating

    def add_book(self, book: Book):
        """
        Add new book to book store if possible.

        :param book: Book
        Function does not return anything
        """
        pass

        if self.can_add_book(book):
            self.books.append(book)
            print(f"Book '{book.title}' added to {self.name}'s inventory.")

    def can_remove_book(self, book: Book) -> bool:
        """
        Check if book can be removed from store.

        Book can be successfully removed if it is actually present in store

        :return: bool
        """
        pass

        return book in self.books

    def remove_book(self, book: Book):
        """
        Remove book from store if possible.

        Function does not return anything
        """
        pass

        if self.can_remove_book(book):
            self.books.remove(book)
            print(f"Book '{book.title}' removed from {self.name}'s inventory.")

    def get_all_books(self) -> list:
        """
        Return a list of all books in current store.

        :return: list of Book objects
        """
        pass

        return self.books

    def get_books_by_price(self) -> list:
        """
        Return a list of books ordered by price (from cheapest).

        :return: list of Book objects
        """
        pass

        return sorted(self.books, key=lambda x: x.price)

    def get_most_popular_book(self) -> list:
        """
        Return a list of book (books) with the highest rating.

        :return: list of Book objects
        """
        pass

        max_rating = max(book.rating for book in self.books)
        return [book for book in self.books if book.rating == max_rating]

