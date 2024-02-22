# Supprimer les valeurs manquantes
# def handle_missing_values(data):
#    filled_data = data.fillna(data.median())
#    return filled_data

import pandas as pd


# Fonction pour filtrer les données
def filter_data(data, condition):
    filtered_data = data.query(condition)
    return filtered_data


# Fonction pour traiter les valeurs manquantes
def handle_missing_values(data):
    filled_data = data.fillna(data.median())
    return filled_data


# Fonction pour traiter les valeurs aberrantes
def handle_outliers(data):
    clean_data = data[(data['value'] >= data['lower_bound']) & (data['value'] <= data['upper_bound'])]
    return clean_data


# Fonction pour effectuer un calcul
def perform_calculation(data, calculation):
    result = eval(calculation)
    return result


# Fonction pour normaliser les données
def normalize_data(data):
    normalized_data = (data - data.mean()) / data.std()
    return normalized_data


# Fonction pour ajouter un attribut aux données
def add_attribute(data, attribute_name, attribute_value):
    data[attribute_name] = attribute_value
    return data
