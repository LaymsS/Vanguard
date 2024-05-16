import os

def createPDFRapports(session_name):
    print("check directory rapport")
    # Création du répertoire avec le nom de la session
    directory_path = f"PDFreports/{session_name}_session"
    print(f"chemin du rappport {directory_path}")
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Rapport {session_name} créé avec succès.")
    else:
        print(f"Rapport {session_name} existe déjà.")

     # Chemin du sous-répertoire "images"
    images_directory_path = os.path.join(directory_path, "images")
    advance_directory_path = os.path.join(directory_path, "advanceReport")
    simple_directory_path = os.path.join(directory_path, "simpleReport")
    
    # Vérifier s'il existe et le créer au besoin
    if not os.path.exists(images_directory_path):
        os.makedirs(images_directory_path)
        os.makedirs(advance_directory_path)
        os.makedirs(simple_directory_path)
        print(f"Répertoire 'images' créé avec succès à l'intérieur de {session_name}_session.")
    else:
        print(f"Le répertoire 'images' existe déjà à l'intérieur de {session_name}_session.")