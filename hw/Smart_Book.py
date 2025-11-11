
class Book:



    default_format = "бумажная"


    def __init__(self, title, author, pages, format=None):
        self.title = title
        self.author = author


        self.pages = int(pages)
        self.format = format if format is not None else Book.default_format

    def __str__(self):

        return f"\"{self.title}\" — {self.author}, {self.pages} стр."

    def __len__(self):
        return self.pages


    def __add__(self, other):
        total = self.pages + other.pages
        return f"Вместе: {total} страниц"


    def __eq__(self, other):
        return self.pages == other.pages

    def __getitem__(self, index):

        return f"Глава {index}: содержание книги '{self.title}'"

    @classmethod
    def from_string(cls, s):
        parts = s.split(", ")

        title, author, pages = parts[0], parts[1], parts[2]
        return cls(title, author, pages)

    @staticmethod
    def is_thick(pages):

        return pages > 500


if __name__ == "__main__":
    book1 = Book("1984", "Дж. Оруэлл", 328)

    book2 = Book.from_string("Гарри Поттер, Дж. Роулинг, 400")

    print(book1)

    print(len(book1))
    print(book1 + book2)
    print(book1 == book2)


    print(book1[5])

    print(Book.is_thick(600))
    print(Book.is_thick(300))

    book3 = Book("Python", "Гвидо", 200)
    print(book3.format)