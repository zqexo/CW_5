import requests

class HHAPI:
    def __init__(self):
        self.base_url = 'https://api.hh.ru'

    def get_vacancies(self, search_query):
        url = f'{self.base_url}/vacancies'
        params = {'text': search_query}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()['items']
        else:
            raise Exception(f"Ошибка при получении данных вакансий: {response.status_code} - {response.text}")
