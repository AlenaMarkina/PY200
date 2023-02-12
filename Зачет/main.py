import re
import random
import hashlib
from typing import Union

from food_generator import gen_food


class IdCounter:
    """Класс, в котором хранится генератор значений id. """
    def __init__(self):

        self._id = 0

    @property
    def id(self):
        return self._id

    def id_generator(self):
        self._id += 1
        yield self._id


class Password:

    def get_hash(self, password: str) -> str:
        """
        Возвращает хэш-значение введенного пароля.
        Пароль должен соответствовать определенным критериям.

        :param password: Пароль, для которого нужно получить хэш-значение
        :return: str
        """
        self.is_valid_password(password)
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def is_valid_password(password: str):
        """
        Проверяет, отвечает ли пароль следующим критериям:
        - пароль строкового типа;
        - длина не менее 8 символов;
        - имеются как цифры так и буквы.

        :param password: Пароль, который необходимо проверить
        :return: None
        """
        if not isinstance(password, str):
            raise TypeError(f"Неверный тип данных для пароля: {password}, ожидается str")

        pattern = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")
        if not bool(pattern.search(password)):
            raise ValueError(f"Введенный пароль не отвечает требованиям!")

    def check(self):
        """Проверяет соотносится ли передаваемый пароль с его хэш-значением"""

        # TODO: честно говоря, не поняла что нужно сделать


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
            raise TypeError(f"Неверный тип данных для name: {name}, ожидается str")

    @staticmethod
    def is_valid_int_or_float(number):
        if not isinstance(number, (int, float)):
            raise TypeError(f"Неверный тип данных для number: {number}, ожидается int")
        if number < 0:
            raise ValueError(f"Неверное значение для number: {number}, ожидается > 0")


class Cart:
    """Класс, в котором хранится информация о списке продуктов покупателя. """

    def __init__(self):
        """
        Инициализация объекта "Корзина". Содержит пустую корзину покупателя.
        """
        self.__product_cart = []  # список продуктов покупателя

    @property
    def product_cart(self):
        return self.__product_cart

    def add_product(self, product: str) -> None:
        """
        Добавление продукта в корзину

        :param product: Продукт, который нужно положить в корзину
        :return: None
        """
        self.product_cart.append(product)

    def del_product(self, product: str) -> None:
        """
        Удаление продукта из корзины

        :param product: Продукт, который нужно удалить из корзины
        :return: None
        """
        try:
            self.product_cart.remove(product)
        except ValueError:
            print(f"Продукт '{product}' не может быть удален из корзины, так как его там нет.")


class User(Cart, Password):
    """Класс, описывающий пользователя. """

    def __init__(self, username, password):
        """
        Инициализация пользователя

        :param username: Имя пользователя
        :param password: Пароль пользователя
        """
        super().__init__()
        self.id = self.id_init()
        self.is_valid_username(username)
        self.__username = username
        self.__password_hash = self.get_hash(password=password)

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password_hash

    @staticmethod
    def id_init():
        return random.randint(1, 1000)

    @staticmethod
    def is_valid_username(username):
        if not isinstance(username, str):
            raise TypeError(f"Неверный тип данных для username: {username}, ожидается str")

    def __str__(self):
        return f"Класс {__class__.__name__}, id:{self.id}, имя пользователя: {self.username}, пароль: 'password1"

    def __repr__(self):
        return f"{__class__.__name__}(id={self.id}, username={self.username}, password='password1')"


class Store:
    """Класс, описывающий магазин. """

    def __init__(self, products_in_store: list):
        """
        Инициализация объекта "Магазин"

        :param products_in_store: Список продуктов
        """
        self.products_in_store = products_in_store
        self.users = []  # список пользователей магазина

    def create_user(self) -> None:
        """
        Запрашивает у пользователя имя и пароль.
        Создает и добавляет нового пользователя магазина в список.

        :return: None
        """
        uname, pword = input('Введите имя пользователя и пароль:  ').split(' ')
        self.users.append(User(uname, pword))

    def add_product_to_cart(self) -> None:
        """
        Добавляет случайный продукт из магазина в корзину пользователя.
        Пользователь также выбирается случайным образом из списка пользователей магазина.

        :return: None
        """
        product_idx = random.randint(0, len(self.products_in_store) - 1)
        user_idx = self.get_user_idx()

        self.users[user_idx].add_product(self.products_in_store[product_idx])

    def get_cart(self) -> None:
        """
        Выводит состояние корзины пользователя

        :return: None
        """
        idx = self.get_user_idx()
        print(f"Состояние корзины пользователя {self.users[idx].username}: {self.users[idx].product_cart}")

    def get_user_idx(self) -> int:
        """
        Случайным образом возвращает индекс пользователя из списка пользователей магазина.
        :return: Индекс пользователя
        """
        user_idx = random.randint(0, len(self.users) - 1)
        return user_idx


if __name__ == '__main__':

    product_database = [next(gen_food()) for i in range(50)]  # [{'name': 'Corella Pear', 'price': 176.55, 'rating': 2.38}, {'name': 'Goji Berry', 'price': 1557.78, 'rating': 1.41}]

    list_of_objects = [Product(name=dict_["name"], price=dict_["price"], rating=dict_["rating"]) for dict_ in product_database]

    store = Store(list_of_objects)

    store.create_user()
    store.create_user()

    for _ in range(10):
        store.add_product_to_cart()

    store.get_cart()



