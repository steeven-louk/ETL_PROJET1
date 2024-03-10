import pandas as pd
import requests

######## EXTRACTION DE FICHIER ###########
def extract_csv(data):
    return pd.read_csv(data)


def extract_json(path):
    return pd.read_json(path, orient="records")


#def extract_from_api(api_url):
#    response = requests.get(api_url)
#    data = response.json()
#    data = pd.DataFrame(data)
#    print(data.head())
#    return data


def extract_from_xml(data):
    return pd.read_xml(data)


def extract_from_database(data):
    pass

######## EXTRACTION DE FICHIER ###########
#test_api = extract_from_api("https://dummyjson.com/users")
#print("fsjkdbnfjkshfj",test_api)
