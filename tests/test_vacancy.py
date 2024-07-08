import unittest
from ..src.vacancy import Vacancy
import psycopg2


class TestVacancy(unittest.TestCase):

    def test_init(self):
        name = "Software Engineer"

        url = "url1"
        salary_from = 50000
        salary_to = 70000
        city = "Moscow"
        experience = "3-6 years"

        vacancy = Vacancy(name, url, salary_from, salary_to, city, experience)

        self.assertEqual(vacancy.name, name)
        self.assertEqual(vacancy.url, url)
        self.assertEqual(vacancy.salary_from, salary_from)
        self.assertEqual(vacancy.salary_to, salary_to)
        self.assertEqual(vacancy.city, city)
        self.assertEqual(vacancy.experience, experience)

    def test_lt(self):
        vacancy1 = Vacancy("Software Engineer", "url1", 50000, 70000, "Moscow", "3-6 years")
        vacancy2 = Vacancy("Data Scientist", "url2", 60000, 80000, "Saint Petersburg", "1-3 years")

        self.assertTrue(vacancy1 < vacancy2)
        self.assertFalse(vacancy2 < vacancy1)

if __name__ == "__main__":
    unittest.main()