from typing import Union


class Animal:
    """Класс, который описывает животное. """

    def __init__(self, type_of_animal: str, energy: int, satiety: int):
        """
        Инициализация объекта "Животное"

        :param type_of_animal: Вид животного
        :param energy: Количество энергии животного, в процентах
        :param satiety: Сытость животного, в процентах
        """
        self._type_of_animal = type_of_animal
        self._energy = energy
        self._satiety = satiety

    @property
    def type_of_animal(self):
        return self._type_of_animal

    @property
    def energy(self):
        return self._energy

    @property
    def satiety(self):
        return self._satiety

    @staticmethod
    def is_valid_for_str(srt_obj):
        if not isinstance(srt_obj, str):
            raise TypeError("Неверный тип данных, ожидается str")

    @staticmethod
    def is_valid_for_int(int_obj):
        if not isinstance(int_obj, int):
            raise TypeError("Неверный тип данных, ожидается int")

    def eat(self, increased_energy: int, increased_satiety: int) -> str:
        """
        Животное ест.
        В результате оно увеличивает энергию и сытость на increased_energy и increased_satiety соответственно

        :param increased_energy: Значение, на которое животное увеличивает энергию, в процентах
        :param increased_satiety: Значение, на которое животное увеличивает сытость, в процентах
        :return: Сообщение о состоянии животного после еды
        """
        self._energy += increased_energy
        self._satiety += increased_satiety

        return f"{self.type_of_animal} ест... Энергия животного {self.energy}%, сытость животного {self.satiety}%"

    def sleep(self, increased_energy: int, satiety_loss: int) -> str:
        """
        Животное спит.
        В результате оно увеличивает энергию и тратит сытость на increased_energy и satiety_loss соответственно

        :param increased_energy: Значение, на которое животное увеличивает энергию, в процентах
        :param satiety_loss: Значение, на которе которое животное тратит сытость, в процентах
        :return: Сообщение о состоянии животного после сна
        """
        self._energy += increased_energy
        self._satiety -= satiety_loss

        return f"Животное спит... Энергия животного {self.energy}%, сытость животного {self.satiety}%"


class Pet(Animal):
    """Класс, который описывает домашнее животное. """

    number_of_pets = 0

    def __init__(self, type_of_animal: str, energy: int, satiety: int, name: str, pet_breed: str):
        """
         Инициализация объекта "Домашнее животное"

        :param type_of_animal: Вид домашнего животного
        :param energy: Количество энергии домашнего животного, в процентах
        :param satiety: Сытость домашнего животного, в процентах
        :param name: Имя домашнего животного
        :param pet_breed: Порода домашнего животного
        """
        super().__init__(type_of_animal, energy, satiety)

        self.is_valid_for_str(name)
        self._name = name

        self.is_valid_for_str(pet_breed)
        self._pet_breed = pet_breed

    @classmethod
    def get_number_of_pets(cls):
        cls.number_of_pets += 1

    @staticmethod
    def get_price_of_pet_food(weight: Union[int, float], price=800) -> Union[int, float]:
        """
        Получаем цену корма для домашнего животного, исходя из цены за 1 кг

        :param weight: Вес корма, который нужно купить, в кг
        :param price: Цена корма за 1 кг, в рублях
        :return: Цену корма, исходя из цены за 1 кг
        """
        if not isinstance(weight, (int, float)):
            raise TypeError("Неверный тип данный, ожидается int или float")
        if weight <= 0:
            raise ValueError("Неверное значение, ожидается > 0")
        return weight * price

    @property
    def name(self):
        return self._name

    @property
    def pet_breed(self):
        return self._pet_breed

    @name.setter
    def name(self, name: str):
        self.is_valid_for_str(name)
        self._name = name

    @pet_breed.setter
    def pet_breed(self, pet_breed):
        self.is_valid_for_str(pet_breed)
        self._pet_breed = pet_breed

    def play(self, energy_loss: int, satiety_loss: int) -> str:
        """
        Домашнее животное играет.
        В результате оно тратит энергию и сытость на energy_loss и satiety_loss соответственно

        :param energy_loss: Значение, на которе домашнее животное тратит энергию, в процентах
        :param satiety_loss: Значение, на которе домашнее животное тратит сытость, в процентах
        :return: Сообщение о состоянии животного после игры
        """
        self.is_valid_for_int(energy_loss)
        self._energy -= energy_loss

        self.is_valid_for_int(satiety_loss)
        self._satiety -= satiety_loss

        return f"{self.type_of_animal} играет... Энергия животного {self.energy}%, сытость животного {self.satiety}%"


class WildAnimal(Animal):
    """
    Класс, который описывает дикое животное. """

    def __init__(self, type_of_animal: str, energy: int, satiety: int, habitat: str):
        """
         Инициализация объекта "Дикое животное"

        :param type_of_animal: Вид дикого животного
        :param energy: Количество энергии дикого животного, в процентах
        :param satiety: Сытость дикого животного, в процентах
        :param habitat: ареал обитания дикого животного
        """
        super().__init__(type_of_animal, energy, satiety)

        self.is_valid_for_str(habitat)
        self._habitat = habitat

    @property
    def habitat(self):
        return self._habitat

    @habitat.setter
    def habitat(self, habitat):
        self.is_valid_for_str(habitat)
        self._habitat = habitat

    def hunt(self, energy_loss: int, satiety_loss: int) -> str:
        """
        Дикое животное охотится.
        В результате оно тратит энергию и сытость на energy_loss и satiety_loss соответственно

        :param energy_loss: Значение, на которе дикое животное тратит энергию, в процентах
        :param satiety_loss: Значение, на которе дикое животное тратит сытость, в процентах
        :return: Сообщение о состоянии животного после игры
        """
        self._energy -= energy_loss
        self._satiety -= satiety_loss

        return f"{self.type_of_animal} охотится... Энергия животного {self.energy}%, сытость животного {self.satiety}%"


if __name__ == "__main__":

    owl = Animal('Сова', energy=70, satiety=50)
    # print(owl.eat(increased_energy=20, increased_satiety=25))

    cat = Pet(type_of_animal="Кошка", energy=80, satiety=90, name="Dilma", pet_breed="Siberian cat")
    cat.name = "Барсик"
    cat.pet_breed = "Бенгальская кошка"
    # print(cat.play(energy_loss=40, satiety_loss=30))
    print(cat.name, cat.pet_breed)

    tiger = WildAnimal(type_of_animal="Тигр", energy=60, satiety=40, habitat="Дальний Восток России")
    print(tiger.hunt(energy_loss=30, satiety_loss=20))

