from typing import Any, Union

from book_generator import get_random_book


class Book:
    """Класс, который описывает книгу. """

    def __init__(self, id_: Union[int, str], name: str, pages: int):
        """
        Инициализация объекта "Книга"

        :param id_: уникальный идентификатор книги
        :param name: название книги
        :param pages: количество страниц в книге
        """

        self.id_ = None
        self.is_valid_id(id_)

        self.name = None
        self.is_valid_name(name)

        self.pages = None
        self.is_valid_pages(pages)

    def is_valid_id(self, id_: Union[int, str]) -> None:
        """
        Проверка корректности ввода идентификатора книги

        :param id_: уникальный идентификатор книги
        :return: None
        """
        if not isinstance(id_, (int, str)):
            raise TypeError("Введен неверный тип данных для id_")

        self.id_ = id_

    def is_valid_name(self, name: str) -> None:
        """
        Проверка корректности ввода названия книги

        :param name: название книги
        :return: None
        """
        if not isinstance(name, str):
            raise TypeError("Введен неверный тип данных для name")

        self.name = name

    def is_valid_pages(self, pages: int) -> None:
        """
        Проверка корректности ввода количества страниц в книге

        :param pages: количество страниц в книге
        :return: None
        """
        if not isinstance(pages, int):
            raise TypeError("Введен неверный тип данных для pages")
        if pages <= 0:
            raise ValueError("В книге должно быть положительное количество странциц")

        self.pages = pages

    def __str__(self):
        return f"Название класса: {__class__.__name__}, id книги: {self.id_}, название книги: '{self.name}', " \
               f"{self.pages} стр."

    def __repr__(self):
        return f"{__class__.__name__}(id_={self.id_}, name='{self.name}', pages={self.pages})"


class Library:
    """Класс, который описывает библиотеку. """

    def __init__(self, books=None):
        """
        Инициализация объекта "Библиотека"

        :param books: Список книг (список из объектов)
        """
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Метод, возвращающий идентификатор для добавления новой книги в библиотеку.
        Если книг в библиотеке нет, то вернуть 1.
        Если книги есть, то вернуть идентификатор последней книги увеличенный на 1.
        :return: id для будущей книги
        """

        if self.books is not None:
            last_book_id = len(self.books)  # идентификатор последней книги
            next_book_id = last_book_id + 1
            return next_book_id
        else:
            return 1

    def get_index_by_book_id(self, book_id: Union[int, str]) -> Any:
        """
        Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса.
        Если книга существует, то вернуть индекс из списка.
        Если книги нет, то вызвать ошибку ValueError с сообщением: "Книги с запрашиваемым id не существует.

        :param book_id: id книги (идентификатор книги), которую нужно найти в библиотеке
        :return: Индекс книги в списке или ValueError
        """

        list_of_idx = [book.id_ for book in self.books]  # список из id книг

        for idx in range(len(list_of_idx)):
            if book_id == list_of_idx[idx]:
                return f"Индекс книги в списке - {idx}"

        if book_id not in list_of_idx:
            raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':

    books_database = [get_random_book() for _ in range(10)]

    list_books = [Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in books_database]

    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки
    print(library_with_books.get_index_by_book_id('95253334-cb20-46d9-ad89-656a1c27d937'))  # проверяем индекс книги

