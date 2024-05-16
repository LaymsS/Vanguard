import subprocess
import json
import customtkinter as ctk
import re
import os

from Documents.data_json_extraction import extract_data_nmapScan

def scan_page(root):
    print("scan page lancé")

    def scan_window():
        root.withdraw()
        scan_window = ctk.CTkToplevel(root)
        scan_window.title("Simple Scan")
        scan_window.configure(bg='#053225')

        # Détermine les coordonnées pour centrer la fenêtre popup
        # Largeur et la hauteur de l'écran
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        popup_width = 650
        popup_height = 225
        x = (screen_width - popup_width) // 2
        y = (screen_height - popup_height) // 2

        # Positionne la fenêtre popup au centre de l'écran
        scan_window.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

        labelEmailCheck = ctk.CTkLabel(scan_window, text="IP scan host :")
        labelEmailCheck.grid(row=0, column=0, padx=10, pady=10)
        
        port_entry = ctk.CTkEntry(scan_window)
        port_entry.grid(row=0, column=1, padx=10, pady=10)

        buttonEmailCheck = ctk.CTkButton(scan_window, text="Verify", command=lambda: nmap_scanner(port_entry))
        buttonEmailCheck.grid(row=0, column=2, padx=10, pady=10)

        go_back_button = ctk.CTkButton(scan_window, text="GO BACK", command=lambda: goback_windows(scan_window))
        go_back_button.grid(row=2, column=0, padx=10, pady=75)
        quit_button = ctk.CTkButton(scan_window, text="QUIT", command=lambda: quit_windows(scan_window))
        quit_button.grid(row=2, column=2, pady=75)

        # Configurer la fonction à appeler lors de la fermeture de la fenêtre
        scan_window.protocol("WM_DELETE_WINDOW", lambda: close_window(scan_window))

    def goback_windows(window):
        window.destroy()
        root.deiconify()
    
    def quit_windows(window):
        # Détruire la fenêtre actuelle (la nouvelle fenêtre)
        window.quit()

    def close_window(window):
        # Détruire la fenêtre actuelle (la nouvelle fenêtre)
        window.destroy()
        # Rappeler la fenêtre principale
        root.deiconify()

    def nmap_scanner(target_entry):
        with open("json/session.json", "r") as json_file:
            data = json.load(json_file)
            session_name = data.get("sessionName")

        print("nom de la session : ",session_name)

        target = target_entry.get()  # Obtenir l'adresse IP à partir de l'entrée de l'utilisateur
        # Définir la commande Nmap avec les options spécifiées
        commande_nmap = ["nmap", "-sV", "--script", "vulners", "-v", target]

        # Exécuter la commande et capturer la sortie
        process = subprocess.Popen(commande_nmap, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

        # Attendre que la commande se termine et récupérer la sortie
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
                    host = {"host": "scanme.nmap.org", "ports": []}
                    port = {"port": matches.group(1), "state": matches.group(2), "service": matches.group(3), "version": matches.group(4), "vulnerabilities": []}

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

                            vulnerability = {"id": vulnerability_id, "score": score, "address": vuln_data[-1], "exploit": vuln_data[-3] == "true"}
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

            #extract_data_nmapScan(session_name, target, sortie)
        
        #nikto_scan(target)

        # Effacer le champ de texte après le scan
        target_entry.delete(0, ctk.END)

        # Afficher la popup pendant quelques secondes
        show_popup("Scan Done ! \n \n Find the result in your document.")

    def show_popup(message):
        popup_window = ctk.CTkToplevel()
        popup_window.title("Info")
        popup_window.geometry("500x100")
        popup_window.resizable(False, False)
        ctk.CTkLabel(popup_window, text=message).pack()
        popup_window.after(5000, popup_window.destroy)  # Fermer la fenêtre après 5 secondes

    scan_window()