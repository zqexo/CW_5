import psycopg2

class DBManager:
    """
    Класс для управления базой данных PostgreSQL.

    Attributes:
        conn (psycopg2.extensions.connection): Соединение с базой данных.
        cur (psycopg2.extensions.cursor): Курсор для выполнения SQL-запросов.
    """

    def __init__(self, dbname, user, password, host="localhost", port=5432):
        """
        Инициализация объекта DBManager для работы с указанной базой данных.

        Args:
            dbname (str): Имя базы данных.
            user (str): Имя пользователя базы данных.
            password (str): Пароль пользователя базы данных.
            host (str, optional): Хост базы данных. По умолчанию "localhost".
            port (int, optional): Порт базы данных. По умолчанию 5432.
        """
        self.conn = psycopg2.connect(
            dbname=dbname, user=user, password=password, host=host, port=port
        )
        self.cur = self.conn.cursor()

    def insert_vacancy(self, vacancy_data):
        """
        Вставляет данные о вакансии в таблицу вакансий.

        Args:
            vacancy_data (dict): Словарь с данными о вакансии.
                Пример: {
                    'company_id': 1,
                    'name': 'Python Developer',
                    'url': 'https://example.com/vacancy/1',
                    'salary_from': 100000,
                    'salary_to': 150000,
                    'city': 'Moscow',
                    'experience': '3+ years'
                }
        """
        query = """
            INSERT INTO vacancies (company_id, name, url, salary_from, salary_to, city, experience)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            vacancy_data['company_id'],
            vacancy_data['name'],
            vacancy_data['url'],
            vacancy_data['salary_from'],
            vacancy_data['salary_to'],
            vacancy_data['city'],
            vacancy_data['experience']
        )
        self.cur.execute(query, values)
        self.conn.commit()

    def get_companies_and_vacancies_count(self):
        """
        Получает список всех компаний и количество вакансий у каждой компании.

        Returns:
            list: Список кортежей вида (название компании, количество вакансий).
        """
        query = """
            SELECT companies.name, COUNT(vacancies.id) as vacancy_count
            FROM companies
            LEFT JOIN vacancies ON companies.id = vacancies.company_id
            GROUP BY companies.name
        """
        self.cur.execute(query)
        return self.cur.fetchall()

    def get_all_vacancies(self):
        """
        Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.

        Returns:
            list: Список кортежей с данными о вакансиях.
        """
        query = """
            SELECT companies.name, vacancies.name, vacancies.salary_from, vacancies.url
            FROM vacancies
            JOIN companies ON vacancies.company_id = companies.id
        """
        self.cur.execute(query)
        return self.cur.fetchall()

    def get_avg_salary(self):
        """
        Получает среднюю зарплату по вакансиям.

        Returns:
            float: Средняя зарплата по вакансиям.
        """
        query = """
            SELECT AVG(salary_from)
            FROM vacancies
        """
        self.cur.execute(query)
        avg_salary = self.cur.fetchone()[0]
        return avg_salary

    # Добавьте документацию к остальным методам класса DBManager

    def close_connection(self):
        """
        Закрывает соединение с базой данных.
        """
        self.cur.close()
        self.conn.close()

