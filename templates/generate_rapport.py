from datetime import date
import base64
from weasyprint import HTML, CSS
import os
import json


def report_generation(spider_file_path, vul_file_path, session_name, target_nikto, port_nikto, outdated_app, directory_files, sensitive_files, 
                      look_up_files, credentials_files, email_data, ssh_result, username_ssh, password_ssh, leak_ssh, robustness_ssh, 
                      sensitive_pem_files, other_sensitive_files, software_list, total_software_found, total_user_found, users_list):
     
    with open(f"reports/{session_name}_session/{session_name}.json", 'r') as f:
        session_data = json.load(f)
        
    total_vulnerabilities = 0
    total_exploits = 0
    total_open_ports = 0
    vulnerabilities_per_service = {}

    target = session_data.get("NmapScan1", [])[0].get("host", "")

    for host_scan in session_data.get("NmapScan1", []):
        for port_info in host_scan.get("ports", []):
            port_name = port_info.get('port')
            num_vulnerabilities = len(port_info.get('vulnerabilities', []))
            service = port_info.get('service')
            total_open_ports += 1
            total_vulnerabilities += num_vulnerabilities
            total_exploits += sum(1 for v in port_info.get('vulnerabilities', []) if v.get('exploit', False))
            if service:
                vulnerabilities_per_service[service] = vulnerabilities_per_service.get(service, 0) + num_vulnerabilities

    # Convertir l'image en base64
    with open(vul_file_path, "rb") as image_file:
        vul_base64 = base64.b64encode(image_file.read()).decode('utf-8')

    html_content1 = f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{
            background-color: #1E212D;
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            color: #FFFFFF;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); /* Ombre pour le texte */
        }}
        .container {{
            position: relative;
            text-align: center;
            padding: 50px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.5); /* Ombre pour le fond */
        }}
        h1 {{
            font-size: 48px;
            color: #FFFFFF;
            margin-bottom: 20px;
            text-transform: uppercase;
            letter-spacing: 2px;
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); /* Ombre pour le texte */
        }}
        p {{
            font-size: 24px;
            color: #CCCCCC;
            margin-bottom: 40px;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5); /* Ombre pour le texte */
        }}
        .logo {{
            width: 300px;
            margin-top: 20px;
            opacity: 0.5; /* Opacité réduite */
            box-shadow: 4px 4px 8px rgba(0, 0, 0, 0.5); /* Ombre pour le logo */
        }}
        .corner-triangle {{
            position: absolute;
            bottom: 0;
            left: 0;
            border-left: 100px solid transparent;
            border-top: 100px solid #FFFFFF;
            box-shadow: -2px 2px 4px rgba(0, 0, 0, 0.5); /* Ombre pour le triangle */
        }}
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #ffffff;
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
        <h1>Report Vanguard Toolbox</h1>
        <p>Une analyse complète de la sécurité informatique</p>
    </div>
    <div class="corner-triangle"></div>

    """
    html_content2 = f"""

        <div class="container">
            <img class="logo" src="{image_to_base64('/home/kali/Downloads/V6/templates/images/logo.jpg')}" alt="Logo">
        </div>
        <!-- Date et session -->
        <div class="date">
            <p>Rapport du : {date.today().strftime("%d/%m/%Y")}</p>
            <div class="session">
                <p class="session_name">Nom de Session : {session_name}</p>
            </div>
        </div>
        <!-- Images vulnGraph et spiderGraph -->
        <div class="imgContainer">
            <div class="imgVuln">
                <img class="vulnGraph" src="{image_to_base64(vul_file_path)}" alt="vulGraph">
            </div>
            <div class="imgSpider">
                <img class="spiderGraph" src="{image_to_base64(spider_file_path)}" alt="spiderGraph">
            </div>
        </div>
        <!-- Informations vulnérabilités -->
        <h1>Host Vulnerability Report</h1>
        <h2>Scan de vulnérabilité réalisé sur la target : {target}</h2>
        <table>
            <tr>
                <th>Name</th>
                <th>Information</th>
            </tr>
            <tr>
                <td>Total de vulnérabilités trouvées</td>
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

    for host_scan in session_data.get("NmapScan1", []):
        for port_info in host_scan.get("ports", []):
            port_name = port_info.get('port')
            num_vulnerabilities = len(port_info.get('vulnerabilities', []))
            service = port_info.get('service')
            html_content2 += f"""
                <tr>
                    <td>{port_name}</td>
                    <td>{num_vulnerabilities}</td>
                    <td>{service}</td>
                </tr>
            """

    html_content2 += f"""
        </table>
        <table>
        <h2>Scan Nikto Effectué : </h2>
            <tr>
                <th>Target ip</th>
                <th>Target Port</th>
                <th>App Outdated</th>
            </tr>
            <tr>
                <td>{target_nikto}</td>
                <td>{port_nikto}</td>
                <td>{outdated_app}</td>
            </tr>
        </table>
        <table>
        <h2>Rapport Nikto : </h2>
            <tr>
                <th>Nombre de Directory </th>
                <th>Nombre de dossier sensibles </th>
                <th>Nombre de fichier intéressant</th>
                <th>Nombre de fichier de credential</th>
            </tr>
            """

    directory_files_count = len(directory_files)
    sensitive_files_count = len(sensitive_files)
    look_up_files_count = len(look_up_files)
    credentials_files_count = len(credentials_files)
    nbr_email_found = len(email_data)
    html_content2 += f"""
                <tr>
                    <td>{directory_files_count}</td>
                    <td>{sensitive_files_count}</td>
                    <td>{look_up_files_count}</td>
                    <td>{credentials_files_count}</td>
                </tr>
            </table>
            <p>Une recherche d'email à été lancé sur la cible avec {nbr_email_found} résultat(s)</p>
            <table>
                <h2> Email Scrapper </table>
                <tr>
                    <th>Email</th>
            """
    for items in email_data:
        items_email = items
    html_content2 += f"""
                <tr>
                    <td>{items_email}</td>
                    </table>
                    """

    html_content2 += """
    <table>
        <h2> Exploit SSH lancé</h2>
        <tr>
                <th>Target </th>
                <th>Port </th>
                <th>Technique </th>
                <th>Resultat</th>
            </tr>
            """

    if len(ssh_result) == 0:
        result_exploit_ssh = False
    else: 
        result_exploit_ssh = True
        if leak_ssh == True:
            leak_text = "Le password existe dans des bases de données leaked"
        else:
            leak_text = "Le password ne semble pas avoir été leaked"
        if robustness_ssh == True:
            robustness_text = "Le password est considéré comme robuste"
        else:
            robustness_text = "Le password est considéré comme faible"
    html_content2 += f"""
                <tr>
                    <td>{target}</td>
                    <td>22</td>
                    <td>BruteForce</td>
                    <td>{result_exploit_ssh}</td>
                </tr>
            </table>
            """

    html_content2 += f"""
    </table>
    <div>
        <p>Les identifiants trouvé par bruteforce sont : username = <b>{username_ssh}</b> et password = <b>{password_ssh}</b></p>
        <p><b>{leak_text}</b></p>
        <p><b>{robustness_text}</b></p>
    </div>
    <h2>Résultat de la Post-Exploitation</h2>
    <h3>Fichiers sensibles sur le système cible</h3>
    <table>
           <tr>
                <th>Total de fichiers sensibles  </th>
                <th>Total de fichiers de clés </th>
                <th>Autres fichier sensibles</th>
            </tr>
            """
    total_exploit_sensitives_files = len(sensitive_pem_files) + len(other_sensitive_files)
    html_content2 += f"""
            <tr>
                <th>{total_exploit_sensitives_files}</th>
                <th>{len(sensitive_pem_files)}</th>
                <th>{len(other_sensitive_files)}</th>
            </tr>
    </table>
    <p>Il y a un total de <b>{total_software_found}</b> applications découvert sur le systeme cible</>
    <p>Il y a un total de <b>{total_user_found}</b> utilisateurs découvert sur le systeme cible</>
    </body>
    </html>
    """

    # Chemin vers le répertoire du rapport PDF
    pdf_report_dir = f"PDFreports/{session_name}_session/advanceReport"
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
    html_final_content = html_content1 + html_content2
    # Générer le PDF à partir du code HTML
    HTML(string=html_final_content).write_pdf(pdf_path, stylesheets=[CSS(string='@page { size: A4; margin: 0; }')])

    print("rapport créé")


# Fonction pour convertir une image en format base64
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return f"data:image/jpeg;base64,{encoded_string}"



def report_generation_service(session_name):
     
    with open(f"reports/{session_name}_session/{session_name}.json", 'r') as f:
        session_data = json.load(f)
        
    total_vulnerabilities = 0
    total_exploits = 0
    total_open_ports = 0
    vulnerabilities_per_service = {}

    target = session_data.get("NmapScan1", [])[0].get("host", "")

    for host_scan in session_data.get("NmapScan1", []):
        for port_info in host_scan.get("ports", []):
            port_name = port_info.get('port')
            num_vulnerabilities = len(port_info.get('vulnerabilities', []))
            service = port_info.get('service')
            total_open_ports += 1
            total_vulnerabilities += num_vulnerabilities
            total_exploits += sum(1 for v in port_info.get('vulnerabilities', []) if v.get('exploit', False))
            if service:
                vulnerabilities_per_service[service] = vulnerabilities_per_service.get(service, 0) + num_vulnerabilities

    for host_scan in session_data.get("NmapScan1", []):
        for port_info in host_scan.get("ports", []):
            port_name = port_info.get('port')
            num_vulnerabilities = len(port_info.get('vulnerabilities', []))
            service = port_info.get('service')
    
    if total_exploits <= 0:
        text_exploit = "There is no exploit found on the system"
    else:
        text_exploit = "There is a total of ", total_exploits, " exploit(s) found in the system."

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
                margin: 10;
                padding: 10;
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
        <!-- Logo -->
        <div class="container">
            <img class="logo" src="{image_to_base64('/home/kali/Downloads/V6/templates/images/logo.jpg')}" alt="Logo">
        </div>
        <!-- Date et session -->
        <div class="date">
            <p>Rapport du : {date.today().strftime("%d/%m/%Y")}</p>
            <div class="session">
                <p class="session_name">Nom de Session : {session_name}</p>
            </div>
        </div>
        <!-- Images vulnGraph et spiderGraph -->
        <div class="imgContainer">
        </div>
        <!-- Informations vulnérabilités -->
        <h1>Host Vulnerability Report</h1>
        <p>This report presents a detailed analysis of the target's <b>{target}</b> IT security, 
        with particular emphasis on the assessment of potential vulnerabilities and risks on the service <b>{service}</b>. 
        The main objective of this assessment is to ensure the resilience and integrity of [target]'s IT systems, by identifying 
        and correcting security flaws that could compromise data confidentiality, service availability and system integrity.</p>
        <h2>Scan réalisé sur la target : {target}</h2>
        <table>
            <tr>
                <th>Name</th>
                <th>Information</th>
            </tr>
            <tr>
                <td>Total de vulnérabilités trouvées</td>
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
        <h2>Nombre totals des vulnérabilités pour le service <b>{service}</b> :</h2>
        <table>
            <tr>
                <th>Port Number</th>
                <th>Number of Vulnerability</th>
                <th>Service</th>
            </tr>
            <tr>
                <td>{port_name}</td>
                <td>{num_vulnerabilities}</td>
                <td>{service}</td>
            </tr>
        </table>
        <p>A total of {num_vulnerabilities} has been found on the target system ({target}). 
            {text_exploit}</p>
    </body>
    </html>
    """

    # Chemin vers le répertoire du rapport PDF
    pdf_report_dir = f"PDFreports/{session_name}_session/advanceReport"
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