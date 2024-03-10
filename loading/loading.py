from extraction.extraction import extract_csv

import pandas as pd


# sauvegarder en fichier CSV
def save_to_csv(data, path):
    try:
        #print('data',data)
        #print('chemin',path)
        #return data.to_csv(path, index=False)
        if data is not None and isinstance(data, pd.DataFrame):
            data.to_csv(path, index=False)
            print(f"Les données ont été sauvegardées avec succès dans {path}")
        else:
            print("Erreur: Impossible de sauvegarder les données au format CSV. Les données sont invalides.")

    except Exception as e:
        print("Save To CSV Error :", e)


# sauvegarder en fichier json
# def save_to_json(data, path):
#    try:
#        #print("json print output :", data.to_json(path))
#        return data.to_json(path, orient="records", lines=True)
#    except Exception as e:
#        print("Save to Json Error: ", e)
def save_to_json(data, path):
    print("Save To JSON Error :", data)
    if data is not None and isinstance(data, pd.DataFrame):
        data.to_json(path, orient='records', lines=True)
        print(f"Les données ont été sauvegardées avec succès dans {path}")
    else:
        print("Erreur: Impossible de sauvegarder les données au format JSON. Les données sont invalides.")


# sauvegarder en fichier xml
def save_to_xml(data, path):
    try:
        # print('xml print data: ', data.to_xml(index=True))
        return data.to_xml(path, index=True, xml_declaration=True, root_name='data', pretty_print=True)
    except Exception as e:
        print("Save to XML Error :", e)


def load_to_database():
    pass
