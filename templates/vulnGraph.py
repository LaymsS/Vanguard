import os, json, base64
from datetime import date
from weasyprint import HTML, CSS
import matplotlib.pyplot as plt

def create_vuln_graph():
    session_file = "json/session.json" 
    session_name = get_session_name(session_file)
        
    with open(f"reports/{session_name}_session/{session_name}.json", 'r') as f:
        session_data = json.load(f)
        
    total_vulnerabilities = 0
    total_exploits = 0
    total_scores = 0
    total_open_ports = 0
    vulnerabilities_per_service = {}

    try:
        for scan_name, scan_results in session_data.items():
            if isinstance(scan_results, list):
                for host_scan in scan_results:
                    if isinstance(host_scan, dict) and 'ports' in host_scan:
                        for port_info in host_scan['ports']:
                            if isinstance(port_info, dict):
                                total_open_ports += 1
                                vulnerabilities = port_info.get('vulnerabilities', [])
                                total_vulnerabilities += len(vulnerabilities)
                                total_exploits += sum(1 for v in vulnerabilities if v.get('exploit', False))
                                total_scores += sum(v.get('score', 0) for v in vulnerabilities)
                                service = port_info.get('service')
                                if service:
                                    vulnerabilities_per_service[service] = vulnerabilities_per_service.get(service, 0) + len(vulnerabilities)

        print("Total des vulnérabilités trouvées :", total_vulnerabilities)
        print("Total d'exploits disponibles :", total_exploits)
        print("Moyenne total des scores de vulnérabilités :", total_scores)
        print("Nombre total des ports ouverts :", total_open_ports)
        print("Vulnérabilités par service :", vulnerabilities_per_service)

        plt.figure(figsize=(8, 8))  # Ajustez la largeur selon vos besoins
        plt.subplot()
        services = list(vulnerabilities_per_service.keys())
        vulnerabilities = list(vulnerabilities_per_service.values())

        max_vulnerabilities = max(vulnerabilities)
        colors = ['red' if v == max_vulnerabilities else 'green' for v in vulnerabilities]

        plt.bar(services, vulnerabilities, color=colors)
        plt.title('Vulnerabilities per Service')
        plt.xlabel('Service')
        plt.ylabel('Number of Vulnerabilities')
        plt.xticks(rotation=45, fontsize=8)  # Ajustez la taille de la police selon vos besoins
        plt.savefig(f'PDFreports/{session_name}_session/images/vuln_service.png')
        vul_file_path = (f'PDFreports/{session_name}_session/images/vuln_service.png')

        return vul_file_path
    except ValueError:
        print(ValueError)


def get_session_name(session_file):
    session_name = ""
    if os.path.exists(session_file):
        with open(session_file, 'r') as file:
            data = json.load(file)
            session_name = data['sessionName']
            if session_name != "":
                print(f"Session existante trouvée : {session_name}")
            else:
                print("session file doesn't exist")
    return session_name


# Fonction pour convertir une image en format base64
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return f"data:image/jpeg;base64,{encoded_string}"
