import random
from typing import Union

from food_generator import gen_food


class IdCounter:
    id_generator = 0

    @classmethod
    def get_id(cls):
        cls.id_generator += 1
        yield cls.id_generator


class Password:
    pass


class Product:
    """Класс, описывающий продукт питания. """

    def __init__(self, name: str, price: Union[int, float], rating: Union[int, float]):
        """
        Инициализация объекта "Продукт питания"

        :param name: Название продукта питания
        :param price: Цена продукта питания
        :param rating: Рейтинг продукта питания
        """
        self.__id = self.id_init()

        self.is_valid_name(name)
        self.__name = name

        self.is_valid_int_or_float(price)
        self._price = price

        self.is_valid_int_or_float(rating)
        self._rating = rating

    @staticmethod
    def id_init():
        return random.randint(1, 1000)

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        self._rating = rating

    def __str__(self):
        return f"{self.__id}_{self.__name}"

    def __repr__(self):
        return f"{__class__.__name__}({self.__name}, {self._price}, {self._rating})"

    @staticmethod
    def is_valid_name(name):
        if not isinstance(name, str):
            raise TypeError(f"Неверный тип данных: {name}, ожидается str")

    @staticmethod
    def is_valid_int_or_float(number):
        if not isinstance(number, (int, float)):
            raise TypeError(f"Неверный тип данных: {number}, ожидается int")
        if number < 0:
            raise ValueError(f"Неверное значение: {number}, ожидается > 0")


class Cart:
    def __init__(self, product_list):
        self.product_list = product_list

    def add_product(self):
        pass

    def del_product(self):
        pass


class User(Cart):
    def __init__(self, username, password, product_list):
        super().__init__(product_list)

        self.id = None  # TODO: При инициализации должен сам определяться.
        self.__username = username
        self.password = password

    def __str__(self):
        pass

    def __repr__(self):
        pass


class Store(User):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    a = Product('apple', 9, 3.0)
    a.price = 33333
    print(a.__dict__)
