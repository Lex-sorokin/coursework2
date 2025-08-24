from abc import ABC, abstractmethod


class Parser(ABC):
    """Родительский класс для работы с API сервиса с вакансиями"""

    @abstractmethod
    def load_vacancies(self, keyword): ...

    @abstractmethod
    def connect(self): ...
