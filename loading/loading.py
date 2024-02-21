from extraction.extraction import extract_csv
url = '../data/client1.csv'


def load_csv():
    data = extract_csv('https://raw.githubusercontent.com/OpenClassrooms-Student-Center/fr-4452741-decouvrez-les-librairies-python-pour-la-data-science/main/data/prets.csv')
    return data


def save_to_csv(data, path):
    data.to_csv(path, orient="records", lines=True, index=False, )


def save_to_json(data, path):
    data.to_json(path, orient="records", lines=True)


csv_load = load_csv()
print(csv_load)
#save_in_json = save_to_json(load_csv(url), './data')