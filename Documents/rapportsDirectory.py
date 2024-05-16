import os

def createPDFRapports(session_name):
    print("check directory rapport")
    # Création du répertoire avec le nom de la session
    directory_path = f"PDFrapports/{session_name}_session"
    print(f"chemin du rappport {directory_path}")
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Rapport {session_name} créé avec succès.")
    else:
        print(f"Rapport {session_name} existe déjà.")
