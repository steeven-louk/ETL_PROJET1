# Supprimer les valeurs manquantes
def handle_missing_values(data):
    filled_data = data.fillna(data.median())
    return filled_data
