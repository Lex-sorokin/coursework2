import pytest

from src.hh import HH
from src.vacancy import Vacancy


def test_cast_to_object_vacancies(crude_data) -> None:
    assert (
        Vacancy.cast_to_object_vacancies(crude_data["items"])[0].vacancy_id
        == "93353083"
    )
    assert Vacancy.cast_to_object_vacancies([""]) == []


def test_data_file_to_vacancy(json_file_data) -> None:
    assert Vacancy.data_file_to_vacancy(json_file_data)[0].vacancy_id == "124262337"


def test_to_dict(object_vacancy) -> None:
    assert object_vacancy.to_dict() == {
        "area_name": "Москва",
        "employer_id": "247118",
        "employer_name": "ГЕТ ЭКСПЕРТС РЕКРУТМЕНТ",
        "salary_from": 0,
        "salary_to": 0,
        "snippet": 'Опыт коммерческой разработки: от 2 лет. Spring Framework, Hibernate. Знание ООП, структур данных. ',
        "vacancy_id": "124371241",
        "vacancy_name": "Java-разработчик",
        "vacancy_url": "https://hh.ru/vacancy/124371241",
    }
    assert repr(object_vacancy) == (
        "Vacancy(vacancy_id=124371241,\n"
        " vacancy_name=Java-разработчик,\n"
        " vacancy_url=https://hh.ru/vacancy/124371241,\n"
        " salary_from=0,\n"
        " salary_to=0,\n"
        " area_name=Москва,\n"
        " employer_id=247118,\n"
        " employer_name=ГЕТ ЭКСПЕРТС РЕКРУТМЕНТ,\n"
        " snippet=Опыт коммерческой разработки: от 2 лет. Spring Framework, Hibernate. Знание ООП, структур данных. )\n"
        "\n"
    )
    assert not (object_vacancy < object_vacancy)
    with pytest.raises(ValueError):
        object_vacancy < HH()
