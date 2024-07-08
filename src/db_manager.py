import psycopg2
from configparser import ConfigParser


def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')

    return db


class DBManager:
    def __init__(self):
        self.params = config()

    def connect(self):
        return psycopg2.connect(**self.params)

    def get_companies_and_vacancies_count(self):
        query = """
        SELECT o.name, COUNT(v.id)
        FROM organizations o
        LEFT JOIN vacancies v ON o.id = v.organization_id
        GROUP BY o.name;
        """
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                return cur.fetchall()

    def get_all_vacancies(self):
        query = """
        SELECT o.name, v.name, v.salary_from, v.salary_to, v.url
        FROM vacancies v
        JOIN organizations o ON v.organization_id = o.id;
        """
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                return cur.fetchall()

    def get_avg_salary(self):
        query = "SELECT AVG((salary_from + salary_to) / 2) FROM vacancies"
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                return cur.fetchone()[0]

    def get_vacancies_with_higher_salary(self):
        avg_salary = self.get_avg_salary()
        query = """
        SELECT o.name, v.name, v.salary_from, v.salary_to, v.url
        FROM vacancies v
        JOIN organizations o ON v.organization_id = o.id
        WHERE (v.salary_from + v.salary_to) / 2 > %s
        """
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (avg_salary,))
                return cur.fetchall()

    def get_vacancies_with_keyword(self, keyword):
        query = """
        SELECT o.name, v.name, v.salary_from, v.salary_to, v.url
        FROM vacancies v
        JOIN organizations o ON v.organization_id = o.id
        WHERE v.name ILIKE %s
        """
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (f'%{keyword}%',))
                return cur.fetchall()
