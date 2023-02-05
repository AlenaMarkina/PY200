import uuid
import random
import pprint

BOOK_TITLES = ["Убить пересмешника",
               "Гордость и предубеждение",
               "Гарри Поттер и философский камень",
               "Джейн Эйр",
               "Унесенные ветром",
               "Анна Каренина",
               "Десять негритят",
               "Приключения Шерлока Холмса",
               "Поющие в терновнике",
               "Братья Карамазовы",
               "Идиот",
               "Вечера на хуторе близь Диканьки"]


def get_book_title(titles: list) -> str:
    """
    Из переданного списка книг возвращает название книги, выбранное случайным образом.
    :param titles: список книг
    :return: название книги
    """

    idx = random.randint(0, len(titles) - 1)
    return titles[idx]


def get_pages() -> int:
    """Возвращает колчество страниц, сгенерированные случайным образом."""

    return random.randint(300, 1000)


def get_random_book() -> dict:
    """
    Функция-генератор, возвращает словарь заданного типа.
    :return: словарь типа:
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    }
    """

    dict_ = {"id": str(uuid.uuid4()),
             "name": get_book_title(BOOK_TITLES),
             "pages": get_pages()
             }

    return dict_


if __name__ == "__main__":

    list_of_5 = [get_random_book() for _ in range(5)]
    pprint.pprint(list_of_5)




