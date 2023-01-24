from typing import Union


class House:
    """Класс, который описывает дом. """

    def __init__(self, type_of_house: str, area_of_the_house: int, price: Union[int, float]):
        """
        Инициализация объекта "Дом"

        :param type_of_house: Тип дома (кирпичный, шлакоблочный, из бруса и т.д.)
        :param area_of_the_house: Площадь дома, в кв.м
        :param price: Цена дома
        """
        self.type_of_house = type_of_house
        self.area_of_the_house = area_of_the_house
        self.price = None
        self.is_valid_price(price)

    def is_valid_price(self, price: Union[int, float]) -> None:
        """
        Проверка корректности ввода цены дома
        :param price: Цена дома
        :return: None
        """
        if not isinstance(price, (int, float)):
            raise TypeError(f"Введен неверный тип данных для price: {price}")

        if price <= 0:
            raise ValueError(f"Введено неверное значение для price: {price}.")

        self.price = price

    def build_second_floor(self) -> None:
        """
        Строит второй этаж, при этом площадь и цена дома увеличиваются

        :return: None

        house = House("brick", 120, 15000000)
        house.build_second_floor()
        """
        ...

    def build_balcony(self, balcony_area: int, balcony_price: Union[int, float]) -> None:
        """
        Строит балкон, при этом площадь и цена дома увеличиваются

        :param balcony_area: Площадь балкона
        :param balcony_price: Цена балкона
        :return: None

        Пример:
        house = House("brick", 120, 15000000)
        house.build_balcony(6, 300000)
        """
        ...


if __name__ == "__main__":
    house = House("brick", 120, 15000000)
