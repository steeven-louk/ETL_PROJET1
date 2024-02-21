import pandas as pd

def extract_data(data):
    return pd.read_csv(data)
client = pd.read_csv('./data/client1.csv')
client2 = pd.read_csv('data/client2.csv')

data = extract_data('./data/client1.csv')
print(data.head())

client.to_json('./extraction', orient="records")