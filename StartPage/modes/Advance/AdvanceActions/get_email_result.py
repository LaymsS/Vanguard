import json

def get_email_result(session_name):
    # Lire les données depuis le fichier JSON
    with open(f'reports/{session_name}_session/{session_name}.json', 'r') as file:
        data = json.load(file)

    # Récupérer les informations sous la clé "EmailScrapper"
    email_scrapper_data = data.get('EmailScrapper', [])

    return email_scrapper_data