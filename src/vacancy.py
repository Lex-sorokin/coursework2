class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = (
        "vacancy_id",
        "vacancy_name",
        "vacancy_url",
        "salary_from",
        "salary_to",
        "area_name",
        "employer_id",
        "employer_name",
        "snippet",
    )

    def __init__(
        self,
        vacancy_id: str,
        vacancy_name: str,
        vacancy_url: str,
        salary_from: int | None,
        salary_to: int | None,
        area_name: str,
        employer_id: str,
        employer_name: str,
        snippet: str,
    ):
        self.vacancy_id = self.__validate_str(vacancy_id)
        self.vacancy_name = self.__validate_str(vacancy_name)
        self.vacancy_url = self.__validate_str(vacancy_url)
        self.salary_from = self.__validate_int(salary_from)
        self.salary_to = self.__validate_int(salary_to)
        self.area_name = self.__validate_str(area_name)
        self.employer_id = self.__validate_str(employer_id)
        self.employer_name = self.__validate_str(employer_name)
        self.snippet = (
            self.__validate_str(snippet)
            if snippet is not None
            else "Описание не указано"
        )

    @classmethod
    def cast_to_object_vacancies(cls, vacancies_list: list[dict]) -> list["Vacancy"]:
        v_list = []
        for v in vacancies_list:
            if isinstance(v, dict):
                salary = v.get("salary")
                v_list.append(
                    cls(
                        vacancy_id=v.get("id", ""),
                        vacancy_name=v.get("name", ""),
                        vacancy_url=v.get("alternate_url", ""),
                        salary_from=salary.get("from") if salary else None,
                        salary_to=salary.get("to") if salary else None,
                        area_name=v.get("area", {}).get("name"),
                        employer_id=v.get("employer", {}).get("id"),
                        employer_name=v.get("employer", {}).get("name"),
                        snippet=v.get("snippet", {}).get("requirement"),
                    )
                )
            else:
                print(
                    f"Внимание, передаваемые файлы не соответствуют ожидаемому {type(v)}: {v}"
                )
        return v_list

    @classmethod
    def data_file_to_vacancy(cls, data_file: list[dict]) -> list["Vacancy"]:
        """Преобразование данных из файла в объекты класса Vacancy"""
        return [cls(**data) for data in data_file]

    @staticmethod
    def __validate_str(value: str) -> str:
        """Метод валидации входящих строковых аргументов"""
        return value if isinstance(value, str) else ""

    @staticmethod
    def __validate_int(value: int | None) -> int:
        """Метод валидации входящих числовых аргументов"""
        return value if isinstance(value, int) else 0

    def __lt__(self, other):
        """Сравнение вакансий по зарплате (меньше)."""
        if not isinstance(other, Vacancy):
            raise ValueError("Неверный тип данных")
        return self.salary_to < other.salary_to

    def __repr__(self) -> str:
        """Метод корректного вывода данных по вакансии"""
        return (
            f"Vacancy(vacancy_id={self.vacancy_id},\n "
            f"vacancy_name={self.vacancy_name},\n "
            f"vacancy_url={self.vacancy_url},\n "
            f"salary_from={self.salary_from},\n "
            f"salary_to={self.salary_to},\n "
            f"area_name={self.area_name},\n "
            f"employer_id={self.employer_id},\n "
            f"employer_name={self.employer_name},\n "
            f"snippet={self.snippet})\n\n"
        )

    def to_dict(self) -> dict:
        """Метод подготавливающий данные к записи"""
        return {
            "vacancy_id": self.vacancy_id,
            "vacancy_name": self.vacancy_name,
            "vacancy_url": self.vacancy_url,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "area_name": self.area_name,
            "employer_id": self.employer_id,
            "employer_name": self.employer_name,
            "snippet": self.snippet,
        }
