import mysql.connector
import pandas as pd


# Fonction pour filtrer les données
def filter_data(data, source_config):
    try:
        condition = source_config['condition']
        filtered_data = data.query(condition)
        print(filtered_data.head())
        return filtered_data
    except Exception as e:
        print("Error while filtering: ", e)


# Fonction pour traiter les valeurs manquantes
def handle_missing_values(data):
    try:
        filled_data = data.dropna()
        return filled_data
    except Exception as e:
        print("Handle_missing_values Error: ", e)


# Fonction pour effectuer un calcul
def perform_calculation(source_config, data):
    try:
        # for column in data.columns:
        #   if not pd.api.types.is_numeric_dtype(data[column]):
        #      data[column] = pd.to_numeric(data[column], errors='coerce')

        calculation = source_config['calculation']
        result = data.eval(calculation)
        return result
    except Exception as e:
        print("perform_calculation Error: ", e)


# Fonction pour normaliser les données
def normalize_data(data):
    try:
        if isinstance(data, pd.DataFrame):
            numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
            data[numeric_columns] = data[numeric_columns].apply(pd.to_numeric, errors='coerce')

            normalized_data = (data - data.mean()) / data.std()
            return normalized_data
        else:
            print("Error: Data is not a DataFrame.")
            return data
    except Exception as e:
        print("Normalize Error: ", e)
        return data


# Fusionner des sources de données
def merge_data(source_config, data):
    try:
        common_column = source_config['common_column']
        other_file_path = source_config['with']
        return pd.merge(data, pd.read_csv(other_file_path), on=common_column)
    except Exception as e:
        return print("Merge Error: ", e)


# Fonction pour ajouter un attribut aux données
def add_attribute(source_config, data):
    try:
        attribute_name = source_config['attribute_name']
        attribute_value = source_config['attribute_value']
        data[attribute_name] = attribute_value
        return data
    except Exception as e:
        print("add attribute Error: ", e)


# Fonction pour supprimer le dollar des montant
def clean_balance(data):
    try:
        data['balance'] = data['balance'].apply(lambda x: float(x.replace('$', '').replace(',', '')))
        return data
    except Exception as e:
        return print("Clean Balance Error: ", e)


def filter_data_from_database(connection_string, table_name, condition):
    try:
        # Connexion à la base de données
        connection = mysql.connector.connect(**connection_string)

        # Construction de la requête SQL
        query = f"SELECT * FROM {table_name} WHERE {condition};"

        # Exécution de la requête et récupération des résultats dans un DataFrame
        result = pd.read_sql_query(query, connection)
        print(result)
        return result

    except Exception as e:
        print(f"Error filtering data from database: {e}")
        return None

    finally:
        # Fermeture de la connexion à la base de données
        if connection:
            connection.close()