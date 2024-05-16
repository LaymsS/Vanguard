from bs4 import BeautifulSoup
import re, json, requests, os

# Fonction pour extraire les adresses email d'une page web
def extract_emails_from_url(target, extension=None):
    print("emailScrapping launch")
    if extension is None:
        url = "http://" + target
    else: 
        url = "https://" + target + extension
    print('lurl est : ', url)
    try:
        # Faire une requête GET pour obtenir le contenu HTML de la page
        response = requests.get(url)
        # Vérifier si la requête a réussi
        response.raise_for_status()
        
        # Utiliser Beautiful Soup pour parser le contenu HTML
        print("page found")
        soup = BeautifulSoup(response.text, 'html.parser')
        # Utiliser une expression régulière pour rechercher les adresses email dans le contenu de la page
        email_pattern = r'[\w\.-]+@[\w\.-]+'
        second_email_pattern = r'[\w\.-]+\[at\][\w\.-]+'
        emails = re.findall(email_pattern, soup.get_text())
        second_emails = re.findall(second_email_pattern, soup.get_text())

        for email in emails:
            print(email)
        for email in second_emails:
            print(email)
        
        # Ajouter les adresses email au fichier JSON
        session_file = "json/session.json"  # Chemin vers le fichier de session
        session_name = get_session_name(session_file)
        filename = f"reports/{session_name}_session/{session_name}.json"
        print("filename = ", filename)
        add_emails_to_json(filename, emails + second_emails)

    except requests.exceptions.RequestException as e:
        print("Erreur lors de la récupération de la page :", e)
    
    finally:
        # Fermer la connexion si elle a été établie avec succès
        if 'response' in locals():
            response.close()

# Fonction pour ajouter les adresses email au fichier JSON
def add_emails_to_json(filename, emails):
    # Charger le fichier JSON existant
    if not os.path.exists(filename):
        data = {}
    else:
        with open(filename, 'r') as file:
            data = json.load(file)
    
    # Trouver un nom de clé unique pour stocker les adresses email
    email_key = unique_email_key(data)
    
    # Ajouter les adresses email à la structure de données JSON
    data[email_key] = emails
    
    # Enregistrer le fichier JSON mis à jour
    with open(filename, 'w') as file:
        json.dump(data, file)

# Fonction pour trouver un nom de clé unique pour stocker les adresses email
def unique_email_key(data):
    email_key_base = 'EmailScrapper'
    email_key = email_key_base
    index = 1
    while email_key in data:
        index += 1
        email_key = f'{email_key_base}{index}'
    return email_key

def get_session_name(session_file):
            if os.path.exists(session_file):
                with open(session_file, 'r') as file:
                    data = json.load(file)
                    session_name = data['sessionName']
            return session_name