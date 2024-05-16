import os
import json

def createReport(session_name):
    print("check directory")
    # Création du répertoire avec le nom de la session
    directory_path = f"reports/{session_name}_session"
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Répertoire {session_name} créé avec succès.")
    else:
        print(f"Répertoire {session_name} existe déjà.")

    # Création du fichier JSON à l'intérieur du répertoire
    json_file_path = f"{directory_path}/{session_name}.json"
    if not os.path.exists(json_file_path):
        with open(json_file_path, 'w') as file:
            data = {'session_name': session_name}
            json.dump(data, file)
            print(f"Fichier {session_name}.json créé avec succès.")
    else:
        print(f"Fichier {session_name}.json existe déjà.")
