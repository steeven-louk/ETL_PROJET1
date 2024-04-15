import unittest

from extraction.extraction import extract_csv, extract_json, extract_from_xml, extract_from_api, extract_from_database


class TestExtraction(unittest.TestCase):
    def test_extract_csv(self):
        source_config = '../data/client1.csv'
        data = extract_csv(source_config)
        # Vérifier si les données extraites du fichier CSV sont correctes

    def test_extract_json(self):
        source_config = '../data/users.json'

        data = extract_json(source_config)
        # Vérifier si les données extraites du fichier JSON sont correctes

    def test_extract_xml(self):
        data = '../data/book.xml'
        data = extract_from_xml(data)
        # Vérifier si les données extraites du fichier XML sont correctes

    def test_extract_api(self):
        data = 'https://jsonplaceholder.typicode.com/todos'
        extract_from_api(data)
        # Vérifier si les données extraites de l'API sont correctes

 #   def test_extract_database(self):
#        source_config = {
#            'type': 'database',
#            'connection_params': {
#                'host': 'localhost',
#                'user': 'root',
#                'password': '',
#                'database': 'dm22'
#            },
#            'query': 'SELECT * FROM membres'
#        }
#        data = extract_from_database(source_config)
        # Vérifier si les données extraites de la base de données sont correctes


if __name__ == '__main__':
    unittest.main()
