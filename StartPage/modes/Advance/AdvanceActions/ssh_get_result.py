import json

def get_ssh_result(session_name):
    # Lire les données depuis le fichier JSON
    with open(f'reports/{session_name}_session/{session_name}.json', 'r') as json_file:
        data = json.load(json_file)

    # Récupérer les informations sous la clé "exploitSSH1"
    exploit_ssh_data = data.get('ExploitSSH1', [])
    username_ssh = exploit_ssh_data.get('username')
    password_data = exploit_ssh_data.get('password', {})
    password_ssh = password_data.get('pwd')
    leak_ssh = password_data.get('leak')
    robustness_ssh = password_data.get('robustness')

    return exploit_ssh_data, username_ssh, password_ssh, leak_ssh, robustness_ssh

