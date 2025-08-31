import requests

from src.parser import Parser


class ConnectHHError(Exception):
    pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies = []

    def load_vacancies(self, keyword):
        self.__params["text"] = keyword
        while self.__params.get("page") != 1:
            response = requests.get(
                self.__url, headers=self.__headers, params=self.__params
            )
            vacancies = response.json()["items"]
            self.__vacancies.extend(vacancies)
            self.__params["page"] += 1

    @property
    def get_vacancies(self) -> list[dict]:
        """Геттер для получения списка вакансий"""
        return self.__vacancies

    def connect(self) -> bool:
        """Проверка подключения к API HH.ru."""
        try:
            params: dict = {"text": "", "per_page": 1}
            response = requests.get(self.__url, headers=self.__headers, params=params)
            if response.status_code != 200:
                raise ConnectHHError("Ошибка сервера")
            return response.status_code == 200
        except requests.RequestException as e:
            print(f"Ошибка при подключении к API: {e}")
            raise ConnectHHError(str(e))
