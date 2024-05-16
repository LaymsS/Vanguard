from datetime import date
import base64
from weasyprint import HTML, CSS
import os
import json
import matplotlib.pyplot as plt

def data_pdf_from_scan(session_name, target, total_vulnerabilities, total_exploits, total_scores, total_open_ports, port_data):
    print("Nom de session : ", session_name)
    print("Target : ", target)
    print("Total des vulnérabilités : ", total_vulnerabilities)
    print("Total d'exploits disponibles : ", total_exploits)
    print("Moyennes des scores : ", total_scores)
    print("Nombre de ports ouverts : ", total_open_ports)
    ports_data_json = json.dumps(port_data)

    total_vulnerabilities = sum(vulnerabilities for _, vulnerabilities, _ in port_data)
    vulnerabilities_per_service = {service: num_vulnerabilities for _, num_vulnerabilities, service in port_data}

    plt.figure(figsize=(6, 6))  # Ajustez la largeur selon vos besoins
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
        # Convertir l'image en base64
    vul_base64 = image_to_base64(vul_file_path)
    print(vul_file_path)
    # Convertir l'image en base64
    with open(vul_file_path, "rb") as image_file:
        vul_base64 = base64.b64encode(image_file.read()).decode('utf-8')

    # Générer le code HTML avec le logo au milieu et la date en haut à gauche
    html_content = f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Rapport</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #ffffff; /* Couleur de fond */
            }}
            .container {{
                position: relative;
                width: 100%;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
            }}
            .date {{
                position: absolute;
                top: 10px;
                left: 30px;
            }}
            .container {{
                position: relative;
                width: 100%;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background-color: rgba(255, 255, 255, 0.5); /* Opacité de 50% */
            }}
            .logo {{
                position: relative;
                display: block;
                margin: auto;
                opacity: 0.2; /* Opacité de l'image */
            }}
            table {{
                border-collapse: collapse;
                width: 70%; /* Largeur de votre table */
                margin: auto; /* Centrer la table */
            }}
            th, td {{
                border: 1px solid black; /* Bordure noire */
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #f2f2f2; /* Couleur de fond des cellules d'en-tête */
            }}
            h1, h2 {{
                text-align: center;
            }}
            .session {{
                text-align: right;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <img class="logo" src="{image_to_base64('/home/kali/Downloads/V6/templates/images/logo.jpg')}" alt="Logo">
        </div>
        <div class="date">
            <p>Rapport du : {date.today().strftime("%d/%m/%Y")}</p>
            <div class="session">
                <p class="session_name">Nom de Session : {session_name}</p>
            </div>
        </div>
        <div class="imgVuln">
            <img class="vulnGraph" src="{image_to_base64(vul_file_path)}" alt="vulGraph">
        </div>
         <h1>Host Vulnerability Report</h1>
         <h2>Scan réalisé sur la target : {target}</h2>
    <table>
        <tr>
            <th>Name</th>
            <th>Information</th>
        </tr>
        <tr>
            <td>Total de vulnérabiliés trouvées</td>
            <td>{total_vulnerabilities}</td>
        </tr>
        <tr>
            <td>Total d'exploit disponible</td>
            <td>{total_exploits}</td>
        </tr>
        <tr>
            <td>Nombre total de ports ouverts</td>
            <td>{total_open_ports}</td>
        </tr>
    </table>
    <h2>Détails des vulnérabilités par port :</h2>
    <table>
        <tr>
            <th>Port Number</th>
            <th>Number of Vulnerability</th>
            <th>Service</th>
        </tr>
    """

    for port_info in port_data:
        port_name = port_info[0]
        num_vulnerabilities = port_info[1]
        service = port_info[2]  # Service correspondant au port
        html_content += f"""
        <tr>
            <td>{port_name}</td>
            <td>{num_vulnerabilities}</td>
            <td>{service}</td>
        </tr>
        """

    html_content += """
    </table>
    </body>
    </html>
    """

    # Chemin vers le répertoire du rapport PDF
    pdf_report_dir = f"PDFreports/{session_name}_session"
    if not os.path.exists(pdf_report_dir):
        os.makedirs(pdf_report_dir)

    # Vérifier l'existence du fichier PDF
    filename = f"scan1_rapport.pdf"
    scan = 1
    while os.path.exists(os.path.join(pdf_report_dir, filename)):
        scan += 1
        filename = f"scan{scan}_rapport.pdf"

    # Chemin complet vers le fichier PDF de sortie
    pdf_path = os.path.join(pdf_report_dir, filename)

    # Générer le PDF à partir du code HTML
    HTML(string=html_content).write_pdf(pdf_path, stylesheets=[CSS(string='@page { size: A4; margin: 0; }')])

    print("rapport créé")


# Fonction pour convertir une image en format base64
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return f"data:image/jpeg;base64,{encoded_string}"
