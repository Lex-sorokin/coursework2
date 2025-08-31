
import pytest

from src.hh import HH
from src.json_saver import JSONSaver
from src.vacancy import Vacancy


@pytest.fixture
def object_hh():
    return HH()


@pytest.fixture
def object_json_saver():
    return JSONSaver("test.json")


@pytest.fixture
def object_vacancy():
    return Vacancy(
        vacancy_id="124371241",
        vacancy_name="Java-разработчик",
        vacancy_url="https://hh.ru/vacancy/124371241",
        salary_from=0,
        salary_to=0,
        area_name="Москва",
        employer_id="247118",
        employer_name="ГЕТ ЭКСПЕРТС РЕКРУТМЕНТ",
        snippet="Опыт коммерческой разработки: от 2 лет. Spring Framework, Hibernate. Знание ООП, структур данных. ",
    )


@pytest.fixture
def crude_data():
    return {
        "items": [
            {
                "id": "93353083",
                "premium": False,
                "name": "Тестировщик комфорта квартир",
                "department": None,
                "has_test": False,
                "response_letter_required": False,
                "area": {
                    "id": "26",
                    "name": "Воронеж",
                    "url": "https://api.hh.ru/areas/26",
                },
                "salary": {
                    "from": 350000,
                    "to": 450000,
                    "currency": "RUR",
                    "gross": False,
                },
                "type": {"id": "open", "name": "Открытая"},
                "address": None,
                "response_url": None,
                "sort_point_distance": None,
                "published_at": "2024-02-16T14:58:28+0300",
                "created_at": "2024-02-16T14:58:28+0300",
                "archived": False,
                "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=93353083",
                "branding": {"type": "CONSTRUCTOR", "tariff": "BASIC"},
                "show_logo_in_search": True,
                "insider_interview": None,
                "url": "https://api.hh.ru/vacancies/93353083?host=hh.ru",
                "alternate_url": "https://hh.ru/vacancy/93353083",
                "relations": [],
                "employer": {
                    "id": "3499705",
                    "name": "Специализированный застройщик BM GROUP",
                    "url": "https://api.hh.ru/employers/3499705",
                    "alternate_url": "https://hh.ru/employer/3499705",
                    "logo_urls": {
                        "original": "https://hhcdn.ru/employer-logo-original/1214854.png",
                        "240": "https://hhcdn.ru/employer-logo/6479866.png",
                        "90": "https://hhcdn.ru/employer-logo/6479865.png",
                    },
                    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=3499705",
                    "accredited_it_employer": False,
                    "trusted": True,
                },
                "snippet": {
                    "requirement": "Занимать активную жизненную позицию. Обладать навыками коммуникации...",
                    "responsibility": "Оценивать вид из окна: встречать рассветы на кухне, провожать алые закаты ...",
                },
                "contacts": None,
                "schedule": {"id": "flexible", "name": "Гибкий график"},
                "working_days": [],
                "working_time_intervals": [],
                "working_time_modes": [],
                "accept_temporary": False,
                "professional_roles": [{"id": "107", "name": "Руководитель проектов"}],
                "accept_incomplete_resumes": False,
                "experience": {"id": "noExperience", "name": "Нет опыта"},
                "employment": {"id": "full", "name": "Полная занятость"},
                "adv_response_url": None,
                "is_adv_vacancy": False,
                "adv_context": None,
            },
            {
                "id": "92223756",
                "premium": False,
                "name": "Удаленный диспетчер чатов (в Яндекс)",
                "department": None,
                "has_test": False,
                "response_letter_required": False,
                "area": {
                    "id": "113",
                    "name": "Россия",
                    "url": "https://api.hh.ru/areas/113",
                },
                "salary": {
                    "from": 30000,
                    "to": 44000,
                    "currency": "RUR",
                    "gross": True,
                },
                "type": {"id": "open", "name": "Открытая"},
                "address": None,
                "response_url": None,
                "sort_point_distance": None,
                "published_at": "2024-01-25T17:37:04+0300",
                "created_at": "2024-01-25T17:37:04+0300",
                "archived": False,
                "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=92223756",
                "show_logo_in_search": None,
                "insider_interview": None,
                "url": "https://api.hh.ru/vacancies/92223756?host=hh.ru",
                "alternate_url": "https://hh.ru/vacancy/92223756",
                "relations": [],
                "employer": {
                    "id": "9498120",
                    "name": "Яндекс Команда для бизнеса",
                    "url": "https://api.hh.ru/employers/9498120",
                    "alternate_url": "https://hh.ru/employer/9498120",
                    "logo_urls": {
                        "original": "https://hhcdn.ru/employer-logo-original/1121425.jpg",
                        "90": "https://hhcdn.ru/employer-logo/6106293.jpeg",
                        "240": "https://hhcdn.ru/employer-logo/6106294.jpeg",
                    },
                    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=9498120",
                    "accredited_it_employer": False,
                    "trusted": True,
                },
                "snippet": {
                    "requirement": "Способен работать в команде. Способен принимать решения самостоятельно.",
                    "responsibility": "Работать с клиентами или партнерами для решения разнообразных ситуаций. ",
                },
                "contacts": None,
                "schedule": {"id": "remote", "name": "Удаленная работа"},
                "working_days": [],
                "working_time_intervals": [],
                "working_time_modes": [
                    {
                        "id": "start_after_sixteen",
                        "name": "Можно начинать работать после 16:00",
                    }
                ],
                "accept_temporary": False,
                "professional_roles": [{"id": "40", "name": "Другое"}],
                "accept_incomplete_resumes": True,
                "experience": {"id": "noExperience", "name": "Нет опыта"},
                "employment": {"id": "full", "name": "Полная занятость"},
                "adv_response_url": None,
                "is_adv_vacancy": False,
                "adv_context": None,
            },
        ]
    }


@pytest.fixture
def json_file_data():
    return [
        {
            "vacancy_id": "124262337",
            "vacancy_name": "Java-разработчик",
            "vacancy_url": "https://hh.ru/vacancy/124262337",
            "salary_from": 500,
            "salary_to": 1000,
            "area_name": "Ташкент",
            "employer_id": "11754610",
            "employer_name": "TECHNO FLAGMAN",
            "snippet": "Профессионализм. Знание <highlighttext>Java</highlighttext>, ООП, Hibernate, ORM, ",
        },
        {
            "vacancy_id": "124214735",
            "vacancy_name": "Начинающий тестировщик",
            "vacancy_url": "https://hh.ru/vacancy/124214735",
            "salary_from": 100000,
            "salary_to": 160000,
            "area_name": "Донецк",
            "employer_id": "10557415",
            "employer_name": "СМО Впомощь",
            "snippet": "...кейсов, баз UI/UX. Готовность работать полный день. Плюсом будет: Знание SQL. ",
        },
        {
            "vacancy_id": "124335156",
            "vacancy_name": "Разработчик (junior)",
            "vacancy_url": "https://hh.ru/vacancy/124335156",
            "salary_from": 60000,
            "salary_to": 100000,
            "area_name": "Москва",
            "employer_id": "4865",
            "employer_name": "ЕМЕ",
            "snippet": "Понимание методологии программирования на объектно-ориентированных языках.",
        },
    ]
