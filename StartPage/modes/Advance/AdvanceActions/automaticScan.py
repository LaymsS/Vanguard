import os
import subprocess
import ipaddress
import socket
import re
import json
from StartPage.modes.Advance.AdvanceActions.niktoScan import exploit_web_server, parse_nikto_output, update_json_with_nikto_data
from StartPage.modes.Advance.AdvanceActions.preExploit import search_exploit_available
from Documents.topdf.pdf_setup import setup_service_rapport
from Documents.clear_json_report import clear_and_copy_json
from StartPage.modes.Advance.AdvanceActions.exploit import setup_ssh_exploit

def scan_all(all_email, all_exploit):
    print("scan launched")
    ip_adress = get_ip_address()
    print("ip adress = ", ip_adress)
    subnet_mask_length = 24
    network_adress = get_network_from_ip(ip_adress, subnet_mask_length)
    print("network adress = ", network_adress)
    #network_adress = str(network_adress)  # Convertir en chaîne de caractères si nécessaire
    commande_nmap = ["nmap", network_adress +"/" + str(subnet_mask_length)]
    print(commande_nmap)
    process = subprocess.Popen(commande_nmap, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    sortie, erreur = process.communicate()
    print(sortie)
    ip_found = []
    lines = sortie.split('\n')
    for line in lines:
        if 'Nmap scan report for' in line:
            ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', line)
            if ip_match:
                ip_found.append(ip_match.group())
    print("ip found = ", ip_found)

    for ip_adress_found in ip_found:
        scan_all_in_details(ip_adress_found)


def scan_all_in_details(ip_adress):
    print("scan in detail launch")
    with open("json/session.json", "r") as json_file:
        data = json.load(json_file)
        session_name = data.get("sessionName")

    commande_nmap = ["nmap", "-sV", "--script", "vulners", "-v", ip_adress]
    process = subprocess.Popen(commande_nmap, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    sortie, erreur = process.communicate()

    # Vérifier s'il y a eu une erreur
    if process.returncode != 0:
        print("Erreur lors de l'exécution de la commande Nmap:")
        print(erreur)
    else:
        # Utiliser une regex pour capturer toutes les sections pertinentes
        sections = re.findall(r'(\d+/tcp.*?)\n(?=\d+/tcp|\Z)', sortie, re.DOTALL)
        resultat_json = {"hosts": []}

        for section in sections:
            matches = re.match(r'(\d+/tcp)\s+(\w+)\s+(\w+)\s+(.+?)\n\| vulners:\s*(.+?)(?=\n\n|\Z)', section, re.DOTALL)
            if matches:
                host = {"host": ip_adress, "ports": []}
                port = {"port": matches.group(1), "state": matches.group(2), "service": matches.group(3), "version": matches.group(4), "vulnerabilities": []}

                vuln_lines = matches.group(5).strip().split('\n')
                for vuln_line in vuln_lines:
                    vuln_data = vuln_line.strip().split()
                    if len(vuln_data) >= 4:
                        # Vérifier si un exploit est disponible
                        exploit = "*EXPLOIT*" in vuln_data

                        if not exploit:
                            # Si pas d'exploit, l'adresse est l'avant-dernier élément et le score est le dernier
                            address = vuln_data[-1]
                            vulnerability_id = vuln_data[-3]
                            if vuln_data[-2].replace('.', '', 1).isdigit():
                                score = float(vuln_data[-2])
                            else:
                                # Gérer le cas où vuln_data[-2] n'est pas un nombre
                                score = 0.0
                        else:
                            # Si un exploit est disponible, l'adresse est l'avant-dernier élément et le score est 0.0
                            address = vuln_data[-2]
                            score = float(vuln_data[-3])
                            vulnerability_id = vuln_data[-4]

                        vulnerability = {"id": vulnerability_id, "score": score, "address": address, "exploit": exploit}
                        port["vulnerabilities"].append(vulnerability)

                host["ports"].append(port)
                resultat_json["hosts"].append(host)

        # Charger les données existantes du fichier JSON
        with open("reports/{}_session/{}.json".format(session_name, session_name), "r") as json_file:
            existing_data = json.load(json_file)

        # Incrémente le numéro de la clé "NmapScanX" s'il existe, sinon initialise à 1
        nmap_scan_num = existing_data.get("NmapScanNum", 0) + 1

        # Ajoute les nouveaux résultats au dictionnaire existant s'il existe
        existing_hosts = existing_data.get("hosts", [])  # Récupère la liste des hôtes existants ou une liste vide si la clé 'hosts' n'existe pas
        existing_hosts.extend(resultat_json["hosts"])  # Étend la liste des hôtes existants avec les nouveaux résultats
            
        # Met à jour le dictionnaire existing_data avec la nouvelle liste d'hôtes
        existing_data["hosts"] = existing_hosts

        # Ajoute la nouvelle clé "NmapScanX" avec les résultats actuels
        existing_data[f"NmapScan{nmap_scan_num}"] = existing_data.pop("hosts")

        # Met à jour le numéro de la clé "NmapScanNum" dans le dictionnaire existing_data
        existing_data["NmapScanNum"] = nmap_scan_num

        # Écrire les données mises à jour dans le fichier JSON
        with open("reports/{}_session/{}.json".format(session_name, session_name), "w") as json_file:
            json.dump(existing_data, json_file, indent=4)

def scan_ip_with_port_service(all_email, all_exploit, ip_name):
    output_file = "/home/kali/Downloads/niktoScan.txt"
    print("scan launched")
    with open("json/session.json", "r") as session_json_file:
        session_data = json.load(session_json_file)
        session_name = session_data.get("sessionName")
    
    src_file = "json/session.json"
    dest_file = f'reports/{session_name}_session/{session_name}.json'
    clear_and_copy_json(src_file, dest_file)

    commande_nmap = ["nmap", "-sV", "--script", "vulners", "-v", ip_name]
    process = subprocess.Popen(commande_nmap, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    sortie, erreur = process.communicate()

    # Vérifier s'il y a eu une erreur
    if process.returncode != 0:
        print("Erreur lors de l'exécution de la commande Nmap:")
        print(erreur)
    else:
        # Utiliser une regex pour capturer toutes les sections pertinentes
        sections = re.findall(r'(\d+/tcp.*?)\n(?=\d+/tcp|\Z)', sortie, re.DOTALL)
        resultat_json = {"hosts": []}

        for section in sections:
            matches = re.match(r'(\d+/tcp)\s+(\w+)\s+(\w+)\s+(.+?)\n\| vulners:\s*(.+?)(?=\n\n|\Z)', section, re.DOTALL)
            if matches:
                host = {"host": ip_name, "ports": []}
                port = {"port": matches.group(1), "state": matches.group(2), "service": matches.group(3), "version": matches.group(4), "vulnerabilities": []}

                vuln_lines = matches.group(5).strip().split('\n')
                for vuln_line in vuln_lines:
                    vuln_data = vuln_line.strip().split()
                    if len(vuln_data) >= 4:
                        # Vérifier si un exploit est disponible
                        exploit = "*EXPLOIT*" in vuln_data

                        if not exploit:
                            # Si pas d'exploit, l'adresse est l'avant-dernier élément et le score est le dernier
                            address = vuln_data[-1]
                            vulnerability_id = vuln_data[-3]
                            if vuln_data[-2].replace('.', '', 1).isdigit():
                                score = float(vuln_data[-2])
                            else:
                                # Gérer le cas où vuln_data[-2] n'est pas un nombre
                                score = 0.0
                        else:
                            # Si un exploit est disponible, l'adresse est l'avant-dernier élément et le score est 0.0
                            address = vuln_data[-2]
                            score = float(vuln_data[-3])
                            vulnerability_id = vuln_data[-4]

                        vulnerability = {"id": vulnerability_id, "score": score, "address": address, "exploit": exploit}
                        port["vulnerabilities"].append(vulnerability)

                host["ports"].append(port)
                resultat_json["hosts"].append(host)

        # Charger les données existantes du fichier JSON
        with open("reports/{}_session/{}.json".format(session_name, session_name), "r") as existing_json_file:
            existing_data = json.load(existing_json_file)

        # Incrémente le numéro de la clé "NmapScanX" s'il existe, sinon initialise à 1
        nmap_scan_num = existing_data.get("NmapScanNum", 0) + 1

        # Ajoute les nouveaux résultats au dictionnaire existant s'il existe
        existing_hosts = existing_data.get("hosts", [])  # Récupère la liste des hôtes existants ou une liste vide si la clé 'hosts' n'existe pas
        existing_hosts.extend(resultat_json["hosts"])  # Étend la liste des hôtes existants avec les nouveaux résultats
            
        # Met à jour le dictionnaire existing_data avec la nouvelle liste d'hôtes
        existing_data["hosts"] = existing_hosts

        # Ajoute la nouvelle clé "NmapScanX" avec les résultats actuels
        existing_data[f"NmapScan{nmap_scan_num}"] = existing_data.pop("hosts")

        # Met à jour le numéro de la clé "NmapScanNum" dans le dictionnaire existing_data
        existing_data["NmapScanNum"] = nmap_scan_num

        # Écrire les données mises à jour dans le fichier JSON
        with open("reports/{}_session/{}.json".format(session_name, session_name), "w") as updated_json_file:
            json.dump(existing_data, updated_json_file, indent=4)
        
        filename = "reports/{}_session/{}.json".format(session_name, session_name)
        search_exploit_available()
        
        with open(f"reports/{session_name}_session/{session_name}.json", 'r') as f:
            data = json.load(f)

        for host_scan in data.get("NmapScan1", []):
            for port_info in host_scan.get("ports", []):
                port_number = port_info.get('port')
                if "80" in port_number or "443" in port_number:
                    print("port trouvé pour l'execution nikto")
                    exploit_web_server(ip_name, output_file)
                if "22" in port_number:
                    print("ssh port found, launch bruteforce")
                    setup_ssh_exploit(ip_name)
                    break
        
        nikto_data = parse_nikto_output(output_file)
        update_json_with_nikto_data("reports/{}_session/{}.json".format(session_name, session_name), nikto_data)


def scan_all_without_port_service(all_email, all_exploit, service_name, port_name):
    print("scan launched")

def scan_without_port_service(all_email, all_exploit, ip_name, service_name):
    print("scan launched")

def scan_without_service_with_port(all_email, all_exploit, ip_name, selected_port):
    print("scan launched")
    with open("json/session.json", "r") as json_file:
        data = json.load(json_file)
        session_name = data.get("sessionName")

    commande_nmap = ["nmap", "-sV", "--script", "vulners", "-p{}".format(selected_port), "-v", ip_name]
    print("scan launched")
    process = subprocess.Popen(commande_nmap, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    sortie, erreur = process.communicate()

    # Vérifier s'il y a eu une erreur
    if process.returncode != 0:
        print("Erreur lors de l'exécution de la commande Nmap:")
        print(erreur)
    else:
        # Utiliser une regex pour capturer toutes les sections pertinentes
        sections = re.findall(r'(\d+/tcp.*?)\n(?=\d+/tcp|\Z)', sortie, re.DOTALL)
        resultat_json = {"hosts": []}

        for section in sections:
            matches = re.match(r'(\d+/tcp)\s+(\w+)\s+(\w+)\s+(.+?)\n\| vulners:\s*(.+?)(?=\n\n|\Z)', section, re.DOTALL)
            if matches:
                host = {"host": ip_name, "ports": []}
                port = {"port": matches.group(1), "state": matches.group(2), "service": matches.group(3), "version": matches.group(4), "vulnerabilities": []}

                vuln_lines = matches.group(5).strip().split('\n')
                for vuln_line in vuln_lines:
                    vuln_data = vuln_line.strip().split()
                    if len(vuln_data) >= 4:
                        # Vérifier si un exploit est disponible
                        exploit = "*EXPLOIT*" in vuln_data

                        if not exploit:
                            # Si pas d'exploit, l'adresse est l'avant-dernier élément et le score est le dernier
                            address = vuln_data[-1]
                            vulnerability_id = vuln_data[-3]
                            if vuln_data[-2].replace('.', '', 1).isdigit():
                                score = float(vuln_data[-2])
                            else:
                                # Gérer le cas où vuln_data[-2] n'est pas un nombre
                                score = 0.0
                        else:
                            # Si un exploit est disponible, l'adresse est l'avant-dernier élément et le score est 0.0
                            address = vuln_data[-2]
                            score = float(vuln_data[-3])
                            vulnerability_id = vuln_data[-4]

                        vulnerability = {"id": vulnerability_id, "score": score, "address": address, "exploit": exploit}
                        port["vulnerabilities"].append(vulnerability)

                host["ports"].append(port)
                resultat_json["hosts"].append(host)

        # Charger les données existantes du fichier JSON
        with open("reports/{}_session/{}.json".format(session_name, session_name), "r") as json_file:
            existing_data = json.load(json_file)

        # Incrémente le numéro de la clé "NmapScanX" s'il existe, sinon initialise à 1
        nmap_scan_num = existing_data.get("NmapScanNum", 0) + 1

        # Ajoute les nouveaux résultats au dictionnaire existant s'il existe
        existing_hosts = existing_data.get("hosts", [])  # Récupère la liste des hôtes existants ou une liste vide si la clé 'hosts' n'existe pas
        existing_hosts.extend(resultat_json["hosts"])  # Étend la liste des hôtes existants avec les nouveaux résultats
            
        # Met à jour le dictionnaire existing_data avec la nouvelle liste d'hôtes
        existing_data["hosts"] = existing_hosts

        # Ajoute la nouvelle clé "NmapScanX" avec les résultats actuels
        existing_data[f"NmapScan{nmap_scan_num}"] = existing_data.pop("hosts")

        # Met à jour le numéro de la clé "NmapScanNum" dans le dictionnaire existing_data
        existing_data["NmapScanNum"] = nmap_scan_num

        # Écrire les données mises à jour dans le fichier JSON
        with open("reports/{}_session/{}.json".format(session_name, session_name), "w") as json_file:
            json.dump(existing_data, json_file, indent=4)
        search_exploit_available()
        setup_service_rapport()

def get_ip_address():
    # Créer un socket UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Se connecter à un serveur quelconque (Google) avec un port quelconque
        s.connect(("8.8.8.8", 80))
        # Récupérer l'adresse IP de l'interface utilisée pour la connexion
        ip_address = s.getsockname()[0]
    finally:
        s.close()
    return ip_address

def get_network_from_ip(ip_address, subnet_mask_length):
    # Obtenir l'adresse du réseau à partir de l'adresse IP fournie
    network = ipaddress.ip_network(ip_address + '/' + str(subnet_mask_length), strict=False)
    # Récupérer l'adresse du réseau
    network_address = network.network_address
    return str(network_address)