import unittest
from CW5.src.db_manager import DBManager


class TestDBManager(unittest.TestCase):
    def setUp(self):
        self.manager = DBManager()

    def test_get_companies_and_vacancies_count(self):
        result = self.manager.get_companies_and_vacancies_count()
        self.assertIsInstance(result, list)

    def test_get_all_vacancies(self):
        result = self.manager.get_all_vacancies()
        self.assertIsInstance(result, list)

    def test_get_avg_salary(self):
        result = self.manager.get_avg_salary()
        self.assertIsInstance(result, (int, float, type(None)))

    def test_get_vacancies_with_higher_salary(self):
        result = self.manager.get_vacancies_with_higher_salary()
        self.assertIsInstance(result, list)

    def test_get_vacancies_with_keyword(self):
        result = self.manager.get_vacancies_with_keyword('Python')
        self.assertIsInstance(result, list)


if __name__ == '__main__':
    unittest.main()
