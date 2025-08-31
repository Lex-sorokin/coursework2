from src.hh import HH
from src.interaction_user import (filter_vacancies, get_top_vacancies,
                                  get_vacancies_by_salary, print_vacancies,
                                  sort_vacancies)
from src.json_saver import JSONSaver
from src.vacancy import Vacancy

hh = HH()  # создаём объект
json_saver = JSONSaver()

if hh.connect():
    print("Проверка подключения к API HH.ru выполнена успешно.")
else:
    print("Проверка подключения к API HH.ru не удалась, повторите попытку позже.")
    exit()  # Здесь нужно остановить выполнение программы


# Функция для взаимодействия с пользователем
def user_interaction():

    search_query = input("Введите поисковый запрос: ")
    hh.load_vacancies(search_query)
    vac = hh.get_vacancies
    vacancies_list = Vacancy.cast_to_object_vacancies(vac)
    json_saver.add_vacancies(vacancies_list)
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
