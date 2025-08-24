from src.interaction_user import (filter_vacancies, get_top_vacancies,
                                  get_vacancies_by_salary, print_vacancies,
                                  sort_vacancies)
from src.vacancy import Vacancy


def test_filter_vacancies(json_file_data):
    """Тест фильтрации вакансий по словам"""
    filter_words = ["Java", "Разработчик"]
    filtered = filter_vacancies(json_file_data, filter_words)

    assert len(filtered) == 3
    assert all("Java" in repr(vac) or "Разработчик" in repr(vac) for vac in filtered)


def test_get_vacancies_by_salary(json_file_data):
    """Тест получения вакансий по заработной плате"""
    salary_range = "0 - 15000000"
    data_vacancy = Vacancy.data_file_to_vacancy(json_file_data)
    filtered = get_vacancies_by_salary(data_vacancy, salary_range)
    assert len(filtered) == 3
    assert list(vac.salary_from >= 0 and vac.salary_to <= 15000000 for vac in filtered)


def test_sort_vacancies(json_file_data):
    """Тест сортировки вакансий по заработной плате"""
    data_vacancy = Vacancy.data_file_to_vacancy(json_file_data)
    sorted_vacancies = sort_vacancies(data_vacancy)

    assert sorted_vacancies[0].vacancy_id == "124262337"


def test_get_top_vacancies(json_file_data):
    """Тест получения ТОП вакансий"""
    data_vacancy = Vacancy.data_file_to_vacancy(json_file_data)
    top_count = 2
    top_vacancies = get_top_vacancies(data_vacancy, top_count)

    assert len(top_vacancies) == top_count
    assert top_vacancies == data_vacancy[:top_count]


def test_print_vacancies(json_file_data, capsys):
    """Тест вывода вакансий на печать"""

    print_vacancies(json_file_data)
    out = capsys.readouterr()
    assert "124262337" in out.out
