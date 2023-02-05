from typing import Union


class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        """
        Инициализация объекта "Книга"

        :param name: название книги
        :param author: автор книги
        """
        self.__name = name
        self.__author = author

    @property
    def name(self):
        return self.__name

    @property
    def author(self):
        return self.__author

    def __str__(self):
        return f'{self.__author} - "{self.__name}".'

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__name!r}, {self.__author!r})"


class PaperBook(Book):
    """Класс, описывающий бумажную книгу. """

    def __init__(self, name: str, author: str, pages: int):
        """
        Инициализация объекта "Бумажная книга"

        :param name: название книги
        :param author: автор книги
        :param pages: количество страниц в книге
        """
        super().__init__(name, author)
        self.is_valid_pages(pages)
        self._pages = pages

    @staticmethod
    def is_valid_pages(pages):
        if not isinstance(pages, int):
            raise TypeError("Неверный тип данных для pages")
        if pages <= 0:
            raise ValueError("Неверное значение для pages: не может быть меньше или равно 0")

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        self.is_valid_pages(pages)
        self._pages = pages

    def __str__(self):
        return f'{self.author} - "{self.name}", {self.pages} стр.'

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r}, {self.author!r}, {self.pages})"


class AudioBook(Book):
    """Класс, описывающий аудио книгу. """

    def __init__(self, name: str, author: str, duration: Union[int, float]):
        """
        Инициализация объекта "Аудио книга"

        :param name: название книги
        :param author: автор книги
        :param duration: продолжительность книги, в часах
        """
        super().__init__(name, author)
        self.is_valid_duration(duration)
        self._duration = duration

    @staticmethod
    def is_valid_duration(duration):
        if not isinstance(duration, (int, float)):
            raise TypeError("Неверный тип данных для duration")

        if duration <= 0:
            raise ValueError("Неверное значение для duration: не может быть меньше или равно 0")

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        self.is_valid_duration(duration)
        self._duration = duration

    def __str__(self):
        return f'{self.author} - "{self.name}", {self._duration} ч.'

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r}, {self.author!r}, {self._duration})"


if __name__ == "__main__":
    book = Book('Тайна голубого поезда', 'Агата Кристи')
    # book.name = 'Десять негретят'  выдаст ошибку AttributeError: can't set attribute
    #                                так как атрибут name - приватный и мы не можем его изменять
    # book.__name = 'Десять негретят'  создаст новый атрибут, а не изменит существующий

    # paper_book = PaperBook('Тайна голубого поезда', 'Агата Кристи', 320)
    # print(paper_book)

    audio_book = AudioBook('Тайна голубого поезда', 'Агата Кристи', 6)
    print(audio_book)


