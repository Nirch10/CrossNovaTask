import unittest

from Task1.WebApp.App import Server
from Task1.WebApp.PSqlQuery import PSqlQuery


class ServerTest(unittest.TestCase):
    def setUp(self):
        self.server = PSqlQuery("178.22.68.101", 5435, 'auto', 'candidato', 'crossnova20')

    def test_get_columns(self):
        res = self.server.get_table_columns(['numeric'])
        print(res)
        self.assertEqual(len(res) == 0)


if __name__ == '__main__':
    unittest.main()
