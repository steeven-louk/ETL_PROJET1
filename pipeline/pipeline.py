import yaml

from extraction.extraction import extract_json, extract_csv, extract_from_xml, extract_from_api, extract_from_database

from loading.loading import save_to_json, save_to_xml, save_to_csv, save_to_database

from transformation.transformation import filter_data, normalize_data, add_attribute, perform_calculation, \
    clean_balance, handle_missing_values, merge_data, filter_data_from_database, drop_missing_values_from_database


###Extraction de fichier en format DataFrame###
def extract_data(source_config):
    source_type = source_config['type']
    if source_type == 'file':
        if source_config['format'] == 'csv':
            return extract_csv(source_config['path'])
        elif source_config['format'] == 'json':
            return extract_json(source_config['path'])
        elif source_config['format'] == 'xml':
            return extract_from_xml(source_config['path'])
        else:
            raise ValueError("Unsupported file format")

    elif source_type == 'api':
        return extract_from_api(source_config['url'])
    elif source_type == 'database':
        return extract_from_database(source_config['connection_params'], source_config['query'])
    else:
        raise ValueError("Unsupported source type")


###Logique de transformation de fichier###
def apply_transformation(source_config, transformed_data):
    source_type = source_config['type']
    if source_type == 'handle_missing_values':
        return handle_missing_values(transformed_data)
    elif source_type == 'merge_data':
        return merge_data(source_config, transformed_data)
    elif source_type == 'filter':
        return filter_data(transformed_data, source_config)
    elif source_type == 'clean_balance':
        return clean_balance(transformed_data)

    elif source_type == 'drop_missing_values_from_database':
        column_names = source_config['column_names']
        return drop_missing_values_from_database(transformed_data, source_config['connection_params'], column_names)
    elif source_type == "filter_data_from_database":
        return filter_data_from_database(source_config['connection_params'], source_config["table_name"],
                                         source_config['condition'])
    elif source_type == 'add_attribute':
        return add_attribute(source_config, transformed_data)
    elif source_type == 'perform_calculation':
        return perform_calculation(source_config, transformed_data)
    elif source_type == 'normalize_data':
        return normalize_data(transformed_data)
    else:
        raise ValueError("Unsupported transformation type")


###Logique d'enregistrement de fichier###
def load_data(destination_config, data, destination):
    match destination:
        case 'json' if 'file_path' in destination_config:
            save_to_json(data, destination_config['file_path'])
        case 'csv' if 'file_path' in destination_config:
            save_to_csv(data, destination_config['file_path'])
        case 'xml' if 'file_path' in destination_config:
            save_to_xml(data, destination_config['file_path'])
        case 'mysql' if 'connection_params' in destination_config:
            save_to_database(data, destination_config["connection_params"], destination_config["table_name"])
        case _:
            raise ValueError("Unsupported destination type")


def execute_pipeline(pipeline_file):
    with open(pipeline_file, 'r') as file:
        pipeline = yaml.safe_load(file)

    data = {}
    for source in pipeline['sources']:
        data[source['name']] = extract_data(source)

    transformed_data = {}
    for transformation in pipeline['transformations']:
        for source_name, source_data in data.items():
            if transformation['source'] == source_name:
                transformed_data[source_name] = apply_transformation(transformation, source_data)

    for destination in pipeline['destinations']:
        load_data(destination, transformed_data[destination['source']], destination['destination'])
