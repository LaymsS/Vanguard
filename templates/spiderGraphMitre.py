import plotly.graph_objects as go
import os
import json

def create_spider_graph_mitre():
    def get_mitre_attack_values():
        mitre_attack_matrix = {}

        session_file = "json/session.json"  # Chemin vers le fichier de session
        session_name = get_session_name(session_file)
        filename = f"reports/{session_name}_session/{session_name}.json"
        with open(filename, 'r') as file:
            data = json.load(file)

        try:
            # Parcourir les données pour récupérer les valeurs MITRE ATT&CK
            for url_data in data["NmapScan1"]:
                for port_data in url_data["ports"]:
                    for vulnerability in port_data["vulnerabilities"]:
                        if "MITRE&ATTACK" in vulnerability:
                            for key in vulnerability["MITRE&ATTACK"]:
                                if key not in mitre_attack_matrix:
                                    mitre_attack_matrix[key] = 1
                                else:
                                    mitre_attack_matrix[key] += 1

            # Créer les listes categories et values à partir de la matrice
            categories = list(mitre_attack_matrix.keys())
            values = list(mitre_attack_matrix.values())

            # Appel de la fonction create_radar_chart et retour du résultat
            return create_radar_chart(categories, values, session_name)
        
        except ValueError:
            print(ValueError)
    


    def get_session_name(session_file):
        if os.path.exists(session_file):
            with open(session_file, 'r') as file:
                data = json.load(file)
                session_name = data['sessionName']
            return session_name

    def create_radar_chart(categories, values, session_name):
        # Création du graphique en toile d'araignée
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            hoverinfo='text',  # Active l'affichage des valeurs au survol du curseur
            text=values,  # Définit le texte à afficher pour chaque point
            fill='toself',
        ))
        # Mise en forme du titre
        fig.update_layout(
            title='MITRE&ATTACK',
        )
        # Définir manuellement les échelles de l'axe y
        fig.update_yaxes(range=[0, max(values) + 10])  # ajustez 5 selon vos besoins pour un espace supplémentaire
        fig.write_image(f'PDFreports/{session_name}_session/images/spiderGraphMitre.png')
        spider_file_path = f'PDFreports/{session_name}_session/images/spiderGraphMitre.png'
        return spider_file_path

    # Appel de la fonction pour obtenir le chemin du fichier du graphique
    spider_file_path = get_mitre_attack_values()
    return spider_file_path
