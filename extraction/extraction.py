import pandas as pd
import requests
#import mysql.connector
import mysql.connector


######## EXTRACTION DE FICHIER ###########
def extract_csv(data):
    return pd.read_csv(data)


def extract_json(path):
    return pd.read_json(path, orient="records")


def extract_from_api(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        data = pd.DataFrame(data)
        return data
    else:
        print(f"Failed to fetch data from API. Status code: {response.status_code}")
        return None


def extract_from_xml(data):
    return pd.read_xml(data)


def extract_from_database(connection_params, query):
    try:
        conn = mysql.connector.connect(**connection_params)
        cursor = conn.cursor()
        cursor.execute(query)
        columns = cursor.column_names
        data = pd.DataFrame(cursor.fetchall(), columns=columns)
        print("database: ", data)
        conn.close()
        return data
    except mysql.connector.Error as err:
        print("Error while connecting to MySQL", err)
