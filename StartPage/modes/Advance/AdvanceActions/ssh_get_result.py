import json

def get_ssh_result(session_name):
    # Lire les données depuis le fichier JSON
    with open(f'reports/{session_name}_session/{session_name}.json', 'r') as json_file:
        data = json.load(json_file)

    try:
        # Récupérer les informations sous la clé "exploitSSH1"
        exploit_ssh_data = data.get('ExploitSSH1', [])
        if exploit_ssh_data:  # Vérifie si exploit_ssh_data n'est pas vide
            exploit_ssh_item = exploit_ssh_data[0]  # Accéder au premier élément de la liste
            if exploit_ssh_item.get('username') != '':
                username_ssh = exploit_ssh_item.get('username')
            else:
                username_ssh = "None"
            if exploit_ssh_item.get('password', {}) != '':
                password_data = exploit_ssh_item.get('password', {})
            else:
                password_data = "None"
            if password_data.get('pwd') != '':
                password_ssh = password_data.get('pwd')
            else:
                password_ssh = "None"
            if password_data.get('leak') is not None:
                leak_ssh = password_data.get('leak')
            else:
                leak_ssh = None
            if password_data.get('robustness') is not None:
                robustness_ssh = password_data.get('robustness')
            else:
                robustness_ssh = None

            return exploit_ssh_data, username_ssh, password_ssh, leak_ssh, robustness_ssh
        
    except ValueError:
        print(ValueError)


    

