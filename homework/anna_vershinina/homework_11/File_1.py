# The first class
class Book:
    page_material = "бумага"
    text_presence = True

    def __init__(
        self, book_name, book_author, page_number, ISBN, is_reserved=False
    ):
        self.book_name = book_name
        self.book_author = book_author
        self.page_number = page_number
        self.ISBN = ISBN
        self.is_reserved = is_reserved

    def display_books(self):
        result = (
            f"Название: {self.book_name}, "
            f"Автор: {self.book_author}, "
            f"страниц: {self.page_number}, "
            f"материал: {self.page_material}"
        )
        return result


# The second class
class SchoolBook(Book):

    def __init__(
        self,
        book_name,
        book_author,
        page_number,
        ISBN,
        subject,
        class_number,
        has_tasks=True,
    ):
        super().__init__(
            book_name, book_author, page_number, ISBN, is_reserved=False
        )
        self.subject = subject
        self.class_number = class_number
        self.has_tasks = has_tasks

    def display_books(self):
        book_info = super().display_books()
        result = (f"{book_info}, "
                  f"предмет: {self.subject}, "
                  f"класс: {self.class_number}")
        return result


def print_books(book_list):  # Accepts the passed list
    for book in book_list:
        result = book.display_books()
        if book.is_reserved:  # Check if the book is reserved
            result += ", зарезервирована"
        print(result)  # Return the adjusted result if reserved


# The objects for the first class
books = [
    Book("Идиот", "Достоевский", 500, 9788420608051),
    Book("Мастер и Маргарита", "Булгаков", 350, 9788420606840),
    Book("Бег", "Булгаков", 200, 9788420663577),
    Book("Война и Мир", "Толстой", 1000, 978886830059),
    Book("На дне", "Горький", 325, 97888685678),
]

books[-1].is_reserved = True

# The objects for the second class
text_books = [
    SchoolBook(
        "Алгебра",
        "Иванов",
        200,
        9781234567890,
        "Математика",
        9
    ),
    SchoolBook(
        "Геометрия",
        "Атанасян",
        180,
        9780987654321,
        "Математика",
        8
    ),
    SchoolBook(
        "Русский язык",
        "Коровин",
        250,
        9781112223334,
        "Литература",
        7,
        has_tasks=False,
    ),
]

text_books[0].is_reserved = True

# Print of 'books' list
print_books(books)

print()

# Print of 'text_books' list
print_books(text_books)
