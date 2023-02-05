from typing import Union


class WashingMachine:
    """Класс, который описывает стиральную машину. """

    def __init__(self, model: str, maximum_load: int, weight: int, price: Union[int, float]):
        """
        Инициализация объекта "Стиральная машина"

        :param model: Модель стиральной машины
        :param maximum_load: Максимальная загрузка, в кг
        :param weight: Вес стиральной машины, в кг
        :param price: Цена стиральной машины, в рублях
        """
        self.model = model
        self.maximum_load = maximum_load
        self.weight = weight
        self.price = price

    def put_washing_powder(self, powder_weight: int) -> None:
        """
        Кладет стриральный порошок в стиральную машину

        :param powder_weight: Вес стирального порошка, в гр
        :return: None
        """
        ...

    def put_clothes(self, clothes_weight: int) -> None:
        """
        Кладет вещи в стиральную машину для стирки

        :param clothes_weight: Вес вещей
        :return: None
        """
        ...


if __name__ == "__main__":
    machine = WashingMachine("LG", 6, 59, 30000)
