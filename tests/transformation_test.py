import unittest

from transformation.transformation import merge_data, handle_missing_values, filter_data


class TestTransformation(unittest.TestCase):
    def test_merge_data(self):
        source_data = {'identifiant': [1, 2, 3], 'nom': ['Alice', 'Bob', 'Charlie']}
        with_data = {'identifiant': [1, 2, 3], 'email': ['alice@example.com', 'bob@example.com', 'charlie@example.com']}
        common_column = 'identifiant'
        merged_data = merge_data('merge_data', source_data)
        # Vérifier si les données fusionnées sont correctes

    def test_handle_missing_values(self):
        source_data = {'identifiant': [1, 2, None], 'nom': ['Alice', None, 'Charlie']}
        cleaned_data = handle_missing_values(source_data)
        return cleaned_data
        # Vérifier si les valeurs manquantes ont été correctement traitées

    def test_filter(self):
        source_data = {'identifiant': [1, 2, 3], 'genre': ['M', 'F', 'M']}
        condition = 'genre == "M"'
        filtered_data = filter_data(source_data, condition)
        # Vérifier si les données ont été correctement filtrées selon la condition

    # Ajoutez d'autres méthodes de test pour les autres transformations...


if __name__ == '__main__':
    unittest.main()
