# TODO: Создайть генераторы для создания продуктов

class IdCounter:
    id_generator = 0

    @classmethod
    def get_id(cls):
        cls.id_generator += 1
        yield cls.id_generator


class Password:
    pass


class Product:
    def __init__(self, name, price, rating):
        self.__id = None  # TODO: При инициализации должен сам определяться.
        self.__name = name
        self._price = price
        self._rating = rating

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
        return f"{self.id}_{self.__name}"

    def __repr__(self):
        return f"{__class__.__name__}({self.__name}, {self.price}, {self.rating})"


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
    pass
