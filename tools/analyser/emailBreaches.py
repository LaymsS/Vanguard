import requests

def check_email_breaches(email):
    url = f"https://haveibeenpwned.com/api/v2/breachedaccount/{email}"
    headers = {"User-Agent": "Chrome/98.0.4758.109"}  # Remplacez Your_User_Agent par une description de votre application ou un identifiant unique
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # L'adresse e-mail a été compromise dans une ou plusieurs violations de données
        print(f"L'adresse e-mail {email} a été compromise dans les violations de données suivantes :")
        breaches = response.json()
        for breach in breaches:
            print(f"- {breach['Name']} ({breach['BreachDate']})")
    elif response.status_code == 404:
        # L'adresse e-mail n'a pas été compromise dans une violation de données
        print(f"L'adresse e-mail {email} n'a pas été compromise dans les violations de données.")
    else:
        # Une erreur s'est produite lors de la requête
        print("Une erreur s'est produite lors de la requête à l'API Have I Been Pwned.")
        print(f"Code d'état de la réponse : {response.status_code}")
        print(f"Message d'erreur : {response.text}")

