from src.vacancy import Vacancy


def filter_vacancies(
    vacancies_list: list[Vacancy], filter_words: list[str]
) -> list[Vacancy]:
    """Функция фильтрации вакансий по словам"""

    return [
        vac
        for word in filter_words
        for vac in vacancies_list
        if word.lower() in repr(vac).lower()
    ]


def get_vacancies_by_salary(
    vacancies_list: list[Vacancy], salary_range: str
) -> list[Vacancy]:
    """Функция получения вакансий по заработной плате"""
    salary_from, salary_to = list(map(lambda x: x.strip(), salary_range.split("-")))
    return list(
        filter(
            lambda x: x.salary_from >= int(salary_from)
            or x.salary_to <= int(salary_to),
            vacancies_list,
        )
    )


def sort_vacancies(vacancies_list: list[Vacancy]) -> list[Vacancy]:
    """Сортировка вакансий по заработной плате"""
    return sorted(vacancies_list, key=lambda x: x.salary_to)


def get_top_vacancies(vacancies_list: list[Vacancy], top_count: int) -> list[Vacancy]:
    """Выдаёт ТОП вакансий по запросу"""
    return vacancies_list[:top_count]


def print_vacancies(vacancies_list: list[Vacancy]) -> None:
    """Выводит на печать список вакансий"""
    for vacancy in vacancies_list:
        print(repr(vacancy))
