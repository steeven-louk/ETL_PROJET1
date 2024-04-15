import os
import unittest

from loading.loading import save_to_json, save_to_csv, save_to_xml


class TestLoading(unittest.TestCase):
    def test_load_data_json(self):
        data = {'A': [1, 2, 3], 'B': ['a', 'b', 'c']}
        file_path = '../destination/test_destination'
        save_to_json(data, file_path)
        self.assertTrue(os.path.exists(file_path))

    def test_load_data_csv(self):
        data = {'A': [1, 2, 3], 'B': ['a', 'b', 'c']}
        file_path = '../destination/test_destination'
        save_to_csv(data, file_path)
        self.assertTrue(os.path.exists(file_path))

    def test_load_data_xml(self):
        data = {'A': [1, 2, 3], 'B': ['a', 'b', 'c']}
        file_path = '../destination/test_destination'
        save_to_xml(data, file_path)
        self.assertTrue(os.path.exists(file_path))


# def test_load_data_mysql(self):
#    data = {'A': [1, 2, 3], 'B': ['a', 'b', 'c']}
#   connection_params = {'host': 'localhost', 'user': 'root', 'password': '', 'database': 'test'}
#  table_name = 'test_table'
# load_data(data, 'mysql', connection_params, table_name)
# Vérifier si les données ont été correctement chargées dans la base de données

if __name__ == '__main__':
    unittest.main()
