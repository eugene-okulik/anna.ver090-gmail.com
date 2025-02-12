# The first class
class Book:
    page_material = 'бумага'
    text_presence = True

    def __init__(self, book_name, book_author,
                 page_number, ISBN, is_reserved=False):
        self.book_name = book_name
        self.book_author = book_author
        self.page_number = page_number
        self.ISBN = ISBN
        self.is_reserved = is_reserved

# The second class
class SchoolBook(Book):

    def __init__(self, book_name, book_author, page_number,
                 ISBN, subject, class_number, has_tasks=True):
        super().__init__(book_name, book_author, page_number,
                         ISBN, is_reserved=False)
        self.subject = subject
        self.class_number = class_number
        self.has_tasks = has_tasks


# The objects for the first class
books = [
    Book('Идиот', 'Достоевский', 500, 9788420608051),
    Book('Мастер и Маргарита', 'Булгаков', 350, 9788420606840),
    Book('Бег', 'Булгаков', 200, 9788420663577),
    Book('Война и Мир', 'Толстой', 1000, 978886830059),
    Book('На дне', 'Горький', 325, 97888685678)
]

books[-1].is_reserved = True

# The objects for the second class
text_books = [
    SchoolBook('Алгебра', 'Иванов', 200,
               9781234567890, 'Математика', 9),
    SchoolBook('Геометрия', 'Атанасян', 180,
               9780987654321, 'Математика', 8),
    SchoolBook('Русский язык', 'Коровин', 250,
               9781112223334, 'Литература', 7, has_tasks=False),
]

text_books[0].is_reserved = True

# The first print
print(*[
    f"Название: {book.book_name}, "
    f"Автор: {book.book_author}, "
    f"страниц: {book.page_number}, "
    f"материал: {book.page_material}"
    + (", зарезервирована" if book.is_reserved else "")
    for book in books
], sep='\n')

print()
# The second print
print(*[
    f"Название: {tbook.book_name}, "
    f"Автор: {tbook.book_author}, "
    f"страниц: {tbook.page_number}, "
    f"предмет: {tbook.subject}, "
    f"класс: {tbook.class_number}"
    + (", зарезервирована" if tbook.is_reserved else "")
    for tbook in text_books
], sep='\n')
