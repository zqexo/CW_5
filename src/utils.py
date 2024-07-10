def filter_vacancies(vacancies, keywords):
    return [vac for vac in vacancies if any(word in vac.name for word in keywords)]


def get_vacancies_by_salary(vacancies, salary_range):
    salary_min, salary_max = map(int, salary_range.split('-'))
    return [vac for vac in vacancies if vac.salary_from >= salary_min and vac.salary_to <= salary_max]


def sort_vacancies(vacancies):
    return sorted(vacancies, key=lambda x: x.salary_from, reverse=True)


def get_top_vacancies(vacancies, top_n):
    return vacancies[:top_n]


def print_vacancies(vacancies):
    for vac in vacancies:
        print(vac)
