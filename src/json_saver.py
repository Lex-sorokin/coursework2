import json
import os
from abc import ABC, abstractmethod

from config import ROOT_DIR
from src.vacancy import Vacancy


class BaseJSONSaver(ABC):

    @abstractmethod
    def read_file(self, path: str) -> None: ...

    @abstractmethod
    def add_vacancies(self, list_vacancy: list[Vacancy]) -> None: ...

    @abstractmethod
    def write_file(self) -> None: ...

    @abstractmethod
    def delete_vacancy_by_index(self, vacancy: Vacancy) -> None: ...


class JSONSaver(BaseJSONSaver):
    """Класс для чтения и записи вакансий в файл"""

    def __init__(self, filename: str = "hh.data.json") -> None:
        self.__path: str = self.__validate_file(filename)
        self.__data: list[Vacancy] = []

    def __validate_file(self, filename: str) -> str:
        """Проверка наличия файла"""
        path = os.path.join(ROOT_DIR, "data", filename)
        file_exist = os.path.exists(path)
        if not file_exist:
            with open(path, "w", encoding="utf-8"):
                pass
        else:
            self.read_file(path)
        return str(path)

    def read_file(self, path: str) -> None:
        """Метод чтения файла"""
        with open(path, "r", encoding="utf-8") as f:
            self.__data = Vacancy.data_file_to_vacancy(json.load(f))

    def add_vacancies(self, list_vacancy: list[Vacancy]) -> None:
        """Добавление вакансии в список с проверкой на дубликаты"""
        id_vacancies = [i.vacancy_id for i in self.__data]
        for vacancy in list_vacancy:
            if vacancy.vacancy_id not in id_vacancies:
                self.__data.append(vacancy)
        self.write_file()

    def write_file(self) -> None:
        """Метод записи файла"""
        convert_json = [i.to_dict() for i in self.__data]
        with open(self.__path, "w", encoding="utf-8") as f:
            json.dump(convert_json, f, ensure_ascii=False, indent=4)

    def delete_vacancy_by_index(self, vacancy: Vacancy) -> None:
        """Удаляет вакансию по индексу в списке."""
        for index, vac in enumerate(self.__data):
            if vac.vacancy_id == vacancy.vacancy_id:
                del self.__data[index]
                self.write_file()
                break
