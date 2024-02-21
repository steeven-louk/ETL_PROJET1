import pandas as pd
import requests
import json

url = '../data/client1.csv'  # url des données temporaire
json_url = '../data/ville.json'


######## EXTRACTION DE FICHIER ###########
def extract_csv(data) -> str:
    return pd.read_csv(data)


def extract__json(data):  # non fonctionnel
    return pd.read_json(data)


def extract_json(path):
    with open(path, 'r') as file:
        data = json.load(file)


def extract_from_api(api_url):
    response = requests.get(api_url)
    data = response.json()
    return data


def extract_from_xml(data):
    return pd.read_xml(data)

# def extract_from_database(data):
# return pd.read_sql(data)

######## EXTRACTION DE FICHIER ###########
# test_api = extract_from_api("https://randomuser.me/api/")
# print(test_api)
