import json
import re
from Documents.topdf.data_to_pdf import data_pdf_from_scan

def extract_data_nmapScan(session_name, target, output):
    # Utiliser une regex pour capturer toutes les sections pertinentes
    sections = re.findall(r'(\d+/tcp.*?)\n(?=\d+/tcp|\Z)', output, re.DOTALL)
    resultat_json = {"hosts": []}

    for section in sections:
        matches = re.match(r'(\d+/tcp)\s+(\w+)\s+(\w+)\s+(.+?)\n\| vulners:\s*(.+?)(?=\n\n|\Z)', section, re.DOTALL)
        if matches:
            host = {"host": "scanme.nmap.org", "ports": []}
            port = {"port": matches.group(1), "state": matches.group(2), "service": matches.group(3),
                    "version": matches.group(4), "vulnerabilities": []}

            vuln_lines = matches.group(5).strip().split('\n')
            for vuln_line in vuln_lines:
                vuln_data = vuln_line.strip().split()
                if len(vuln_data) >= 4:
                    try:
                        score = float(vuln_data[-2])  # Le score est avant-dernier
                    except ValueError:
                        score = 0.0  # ou une valeur par défaut appropriée

                    # Trouver l'index du début de l'ID de la vulnérabilité
                    id_start_index = vuln_line.find(":")  # Index du début de l'ID

                    # L'ID commence après le premier ":"
                    vulnerability_id = vuln_line[id_start_index + 1:].strip()

                    vulnerability = {"id": vulnerability_id, "score": score, "address": vuln_data[-1],
                                     "exploit": vuln_data[-3] == "true"}
                    port["vulnerabilities"].append(vulnerability)

            host["ports"].append(port)
            resultat_json["hosts"].append(host)

    # Obtenir les informations nécessaires pour le PDF
    # Calculer le nombre total de vulnérabilités
    total_vulnerabilities = sum(sum(len(port["vulnerabilities"]) for port in host["ports"]) for host in resultat_json["hosts"])

    # Calculer le nombre total d'exploits disponibles
    total_exploits = sum(sum(vuln["exploit"] for vuln in port["vulnerabilities"]) for host in resultat_json["hosts"] for port in host["ports"])

    # Calculer la moyenne des scores de vulnérabilité avec un chiffre après la virgule
    total_scores = sum(sum(vuln["score"] for vuln in port["vulnerabilities"]) for host in resultat_json["hosts"] for port in host["ports"])
    total_scores /= total_vulnerabilities if total_vulnerabilities > 0 else 1
    total_scores = round(total_scores, 1)  # Arrondir à une décimale

    # Calculer le nombre total de ports ouverts
    total_open_ports = sum(len(host["ports"]) for host in resultat_json["hosts"])

    ports_data = []
    # Parcourir les hôtes et les ports pour récupérer les données des ports ouverts
    for host in resultat_json["hosts"]:
        for port in host["ports"]:
            # Vérifier si le port est ouvert
            if port["state"] == "open":
                # Compter le nombre de vulnérabilités dans ce port
                num_vulnerabilities = len(port["vulnerabilities"])
                # Ajouter les données du port à la liste des ports ouverts
                ports_data.append([port["port"], num_vulnerabilities, port["service"]])
    
    # Appeler la fonction PDF_Format avec les données extraites
    data_pdf_from_scan(session_name, target, total_vulnerabilities, total_exploits, total_scores, total_open_ports, ports_data)
