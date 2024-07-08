import unittest
from unittest.mock import patch, MagicMock
from CW5.src.hh_api import HHAPI
import psycopg2

class TestHHAPI(unittest.TestCase):

    @patch('CW5.src.hh_api.requests.get')
    def test_get_vacancies_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'items': [{'name': 'Test Vacancy'}]}
        mock_get.return_value = mock_response

        api = HHAPI()
        vacancies = api.get_vacancies('test')
        self.assertEqual(len(vacancies), 1)
        self.assertEqual(vacancies[0]['name'], 'Test Vacancy')

    @patch('CW5.src.hh_api.requests.get')
    def test_get_vacancies_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.text = 'Not Found'
        mock_get.return_value = mock_response

        api = HHAPI()
        with self.assertRaises(Exception):
            api.get_vacancies('test')

if __name__ == '__main__':
    unittest.main()
