import os
import json
import re
from StartPage.modes.Advance.AdvanceActions.emailScrapper import extract_emails_from_url
from Documents.topdf.pdf_setup import setup_rapport
from StartPage.modes.Advance.AdvanceActions.exploit import setup_ssh_exploit

def exploit_web_server(target, output_file):
    # Définir la commande Nikto avec la cible comme argument et spécifier le chemin du fichier de sortie
    command = f"/usr/bin/nikto -h {target} -o {output_file}"
        
    # Effacer le contenu du fichier texte
    open(output_file, 'w').close()

    # Exécuter la commande Nikto
    exit_code = os.system(command)

def get_next_nikto_scan_key(existing_keys):
    # Trie les clés existantes pour obtenir le numéro le plus élevé
    existing_keys.sort()

    # Parcourt les clés existantes pour déterminer la prochaine clé disponible
    for i in range(1, len(existing_keys) + 2):
        key = f"NiktoScan{i}"
        if key not in existing_keys:
            return key

def parse_nikto_output(filename):
    # Dictionnaire pour stocker les informations extraites
    nikto_data = {
        "Target Host": "",
        "Port Host": "",
        "outdatedApp": False,
        "Directory": [],
        "Sensitive": [],
        "lookUp": [],
        "Credentials": []
    }

    # Ouvrir le fichier en mode lecture
    with open(filename, 'r') as file:
        # Parcourir chaque ligne du fichier
        for line in file:
            line = line.strip()
            if "Target Host:" in line:
                nikto_data["Target Host"] = line.split(":")[1].strip()
            elif "Target Port:" in line:
                nikto_data["Port Host"] = line.split(":")[1].strip()
            elif "appears to be outdated" in line:
                nikto_data["outdatedApp"] = True
            elif "Directory indexing" in line or "directory found" in line:
                nikto_data["Directory"].append(line)
            elif line.startswith("+ GET /?="):
                nikto_data["Sensitive"].append(line)
            elif "interesting" in line:
                nikto_data["lookUp"].append(line)
            elif "credentials" in line.lower():
                nikto_data["Credentials"].append(line)
    
    target = nikto_data["Target Host"]
    extract_emails_from_url(target)
    setup_ssh_exploit(target)

    # Expression régulière pour extraire "/doc/", "/test/", "/icons/" ou "/phpMyAdmin/" à partir de la ligne Directory data
    directory_pattern = re.compile(r"\+ GET (\S+):")

    # Créer un ensemble pour stocker les valeurs déjà rencontrées
    unique_values = set()

    # Boucle pour parcourir les lignes de nikto_data["Directory"]
    for line in nikto_data["Directory"]:
        # Rechercher le motif dans la ligne
        match = directory_pattern.search(line)
        # Si le motif est trouvé
        if match:
            # Récupérer la valeur correspondante
            directory_value = match.group(1)
            # Vérifier si la valeur n'a pas encore été rencontrée
            if directory_value not in unique_values:
                # Imprimer la valeur
                extract_emails_from_url(target, directory_value)
                # Ajouter la valeur à l'ensemble des valeurs uniques
                unique_values.add(directory_value)

    return nikto_data

def update_json_with_nikto_data(filename, nikto_data):
    try:
        # Ouvrir le fichier JSON en mode lecture
        with open(filename, 'r') as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        # Si le fichier n'existe pas encore, créer un dictionnaire vide
        existing_data = {}

    # Récupérer les clés existantes
    existing_keys = list(existing_data.keys())

    # Obtenir la prochaine clé pour le scan Nikto
    next_key = get_next_nikto_scan_key(existing_keys)

    # Mettre à jour le dictionnaire JSON avec les données Nikto
    existing_data[next_key] = nikto_data

    # Écrire les données mises à jour dans le fichier JSON
    with open(filename, 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)
    
    setup_rapport()
