from typing import Union


class Telephone:
    """Класс, который описывает телефон. """

    def __init__(self, model: str, device_memory: int, price: Union[int, float], phone_balance: Union[int, float]):
        """
        Инициализация объекта "Телефон"

        :param model: Модель телефона
        :param device_memory: Объем памяти телефона, в Гб
        :param price: Цена телефона
        :param phone_balance: Остаток денежных средств на телефоне, в рублях
        """

        self.model = model
        self.device_memory = device_memory
        self.price = price
        self.phone_balance = phone_balance

    def send_message(self, number_of_messages: int) -> None:
        """
        Посылает смс-сообщение, при этом баланс телефона уменьшается

        :param number_of_messages: Количество отправленныъ сообщений
        :return: None

        Пример:
        phone = Telephone("Realme", 64, 20000, 300)
        phone.send_message(2)
        """

    def upload_application(self, application_name: str, weight: Union[int, float]) -> None:
        """
        Загружает приложение в телфон, при этом объем свободной памяти уменьшается

        :param application_name: Название загружаемого приложения
        :param weight: Вес загружаемого приложения
        :return: None

        Пример:
        phone = Telephone("Realme", 64, 20000, 300)
        phone.upload_application("Telegram", 1)
        """
        ...


if __name__ == "__main__":
    phone = Telephone("Realme", 64, 20000, 300)
