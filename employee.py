from typing import Union


class Employee:
    """Класс, который описывает сотрудника. """

    def __init__(self, name: str, surname: str, age: int, job: str, salary: Union[int, float]):
        """
        Инициализация объекта "Сотрудник"

        :param name: Имя сотрудника
        :param surname: Фамилия сотрудника
        :param age: Возраст сотрудника
        :param job: Должность сотрудника
        :param salary: Заработная плата сотрудника, в рублях
        """
        self.name = None
        self.surname = None
        self.age = None
        self.job = None
        self.salary = None

        self.is_valid_name(name)
        self.is_valid_surname(surname)
        self.is_valid_age(age)
        self.is_valid_job(job)
        self.is_valid_salary(salary)

    def is_valid_name(self, name: str) -> None:
        """
        Проверка корректности ввода имени сотрудника

        :param name: Имя сотрудника
        :return: None
        """

        if not isinstance(name, str):
            raise TypeError(f"Введен неверный тип данных для name: {name}")

        self.name = name

    def is_valid_surname(self, surname: str) -> None:
        """
        Проверка корректности ввода фамилии сотрудника

        :param surname: Фамилия сотрудника
        :return: None
        """

        if not isinstance(surname, str):
            raise TypeError(f"Введен неверный тип данных для surname: {surname}")

        self.surname = surname

    def is_valid_age(self, age: int) -> None:
        """
        Проверка корректности ввода возраста сотрудника

        :param age: Возраст сотрудника
        :return: None
        """

        if not isinstance(age, int):
            raise TypeError(f"Введен неверный тип данных для age: {age}")

        if age <= 0:
            raise ValueError(f"Введено неверное значение для age: {age}.")

        self.age = age

    def is_valid_job(self, job: str) -> None:
        """
        Проверка корректности ввода должности сотрудника

        :param job: Должность сотрудника
        :return: None
        """

        if not isinstance(job, str):
            raise TypeError(f"Введен неверный тип данных для job: {job}")

        self.job = job

    def is_valid_salary(self, salary: Union[int, float]) -> None:
        """
        Проверка корректности ввода заработной платы сотрудника

        :param salary: Заработная плата сотрудника
        :return: None
        """

        if not isinstance(salary, (int, float)):
            raise TypeError(f"Введен неверный тип данных для salary: {salary}")

        if salary <= 0:
            raise ValueError(f"Введено неверное значение для salary: {salary}.")

        self.salary = salary

    def get_promoted(self, delta: Union[int, float]) -> None:
        """
        Повышение заработной платы сотруднику на заданную сумму

        :param delta: Сумма, на которую будет повышение заработной платы
        :return: None

        Пример:
        employee = Employee('Harry', 'Potter', 12, 'Wizard', 20000)
        employee.get_promoted(10000)
        """
        ...

    def get_reduced(self, delta: Union[int, float]) -> None:
        """
        Понижение заработной платы сотруднику на заданную сумму

        :param delta: Сумма, на которую будет понижение заработной платы
        :return: None

        Пример:
        employee = Employee('Harry', 'Potter', 12, 'Wizard', 20000)
        employee.get_reduced(5000)
        """
        ...


if __name__ == "__main__":
    employee = Employee('Harry', 'Potter', 12, 'Wizard', 20000)

