import json
import shutil

def clear_and_copy_json(src_file, dest_file):
    key = "sessionName"
    with open(dest_file, 'w') as dest_json:
        dest_json.write('')

    # Copier la clé et sa valeur du fichier source vers le fichier de destination
    with open(src_file, 'r') as src_json:
        src_data = json.load(src_json)
        if key in src_data:
            value = src_data[key]
            with open(dest_file, 'w') as dest_json:
                json.dump({key: value}, dest_json)

# Exemple d'utilisation :
src_file = 'source.json'
dest_file = 'destination.json'
key_to_copy = 'example_key'
