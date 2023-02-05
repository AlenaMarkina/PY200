class Cat:
    """Класс, который описывает кошку. """

    def __init__(self, name: str, energy: int, satiety: int):
        """
        Инициализация объекта "Кошка"

        :param name: Имя кошки
        :param energy: Количество энергии кошки, в процентах
        :param satiety: Сытость кошки, в процентах
        """

        self.name = None
        self.is_valid_name(name)

        self.energy = energy
        self.satiety = satiety

    def is_valid_name(self, name: str) -> None:
        """
        Проверка корректности ввода имени кошки

        :param name: Имя кошки
        :return: None
        """
        if not isinstance(name, str):
            raise TypeError(f"Введен неверный тип данных для name: {name}")

        self.name = name

    def get_eat(self, increased_energy: int, increased_satiety: int) -> None:
        """
        Кошка ест.
        В результате она увеличивает энергию и сытость на increased_energy и increased_satiety соответственно

        :param increased_energy: Значение, на которое кошка увеличивает энергию, в процентах
        :param increased_satiety: Значение, на которое кошка увеличивает сытость, в процентах
        :return: None

        Пример:
        cat = Cat("Dilma", energy=60, satiety=40)
        cat.get_eat(15, 20)
        """
        ...

    def get_play(self, spent_energy: int, spent_satiety: int) -> None:
        """
        Кошка играет.
        В результате она тратит энергию и сытость на spent_energy и spent_satiety соответственно

        :param spent_energy: Значение, на которе кошка тратит энергию, в процентах
        :param spent_satiety: Значение, на которе кошка тратит сытость, в процентах
        :return: None

        Пример:
        cat = Cat("Dilma", energy=60, satiety=40)
        cat.get_play(10, 15)
        """
        ...

    def get_sleep(self, increased_energy: int, spent_satiety: int) -> None:
        """
        Кошка спит.
        В результате она увеличивает энергию и тратит сытость на increased_energy и spent_satiety соответственно

        :param increased_energy: Значение, на которое кошка увеличивает энергию, в процентах
        :param spent_satiety: Значение, на которе кошка тратит сытость, в процентах
        :return: None

        Пример:
        cat = Cat("Dilma", energy=60, satiety=40)
        cat.get_sleep(30, 10)
        """
        ...


if __name__ == "__main__":
    pass
