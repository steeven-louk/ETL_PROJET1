from extraction.extraction import extract_csv, extract__json

url = '../data/client1.csv'


def load_csv():
    data = extract_csv(
        'https://raw.githubusercontent.com/OpenClassrooms-Student-Center/fr-4452741-decouvrez-les-librairies-python-pour-la-data-science/main/data/prets.csv')
    return data


# sauvegarder en fichier CSV
def save_to_csv(data, path):
    data.to_csv(path, index=False, )


# sauvegarder en fichier json
def save_to_json(data, path):
    try:
        data.to_json(path, orient="records", lines=True)
    except Exception as e:
        print("Unable to ", e)


# sauvegarder en fichier xml
def save_to_xml(data, path):
    data.to_xml(path, index=True, xml_declaration=True, pretty_print=True)


def load_to_database():
    pass