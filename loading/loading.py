import mysql.connector

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
        data.to_json(path, orient="split", index=False)
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


def save_to_database(data, connection_params, table_name):
    try:
        conn = mysql.connector.connect(**connection_params)
        cursor = conn.cursor()

        # Création de la table si elle n'existe pas déjà
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
        for column in data.columns:
            create_table_query += f"{column} VARCHAR(255), "
        create_table_query = create_table_query[:-2] + ")"
        cursor.execute(create_table_query)

        # Insertion des données dans la table
        for row in data.itertuples(index=False):
            insert_query = f"INSERT INTO {table_name} VALUES ("
            for value in row:
                insert_query += f"'{value}', "
            insert_query = insert_query[:-2] + ")"
            cursor.execute(insert_query)

        conn.commit()
        conn.close()
        print("Data saved to MySQL successfully.")
    except mysql.connector.Error as err:
        print("Error while connecting to MySQL", err)
