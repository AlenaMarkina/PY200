from typing import Union


class Film:
    """Класс, который описывает фильм. """

    def __init__(self, title: str, duration: Union[int, float], rating: Union[int, float]):
        """
        Инициализация объекта "Фильм"

        :param title: Название фильма
        :param duration: Продолжительность фильма
        :param rating: Рейтинг фильма от 0 до 10
        """

        self.name = title
        self.duration = duration
        self.rating = None
        self.is_valid_rating(rating)

    def is_valid_rating(self, rating: Union[int, float]) -> None:
        """
        Проверка правильности введения рейтинга.

        :param rating: Рейтинг фильма от 0 до 10
        :return: None
        """
        if not isinstance(rating, (int, float)):
            raise TypeError(f"Введен неверный тип данных для rating: {rating}")

        if not 0 <= rating <= 10:
            raise ValueError(f"Введено неверное значение для rating: {rating}.")

        self.rating = rating

    def rewind_film(self, rewind_minutes: int) -> None:
        """
        Перематывает фильм вперед от начала на заданное количество минут

        :param rewind_minutes: Количество минут, на которое нужно премотать
        :return: None

        Пример:
        film = Film("Harry Potter and Philosopher stone", 2, 8.2)
        film.rewind_film(34)
        """
        ...

    def set_rating(self, my_rating: Union[int, float]):
        """
        Устанавливает рейтинг фильма после просмотра

        :param my_rating: Рейтинг зрителя после просмотра фильма
        :return: None

        Пример:
        film = Film("Harry Potter and Philosopher stone", 2, 8.2)
        film.set_rating(9.0)
        """

        ...


if __name__ == "__main__":
    film = Film("Harry Potter", 2, 8.4)
