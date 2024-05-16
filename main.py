import os
import json
import customtkinter as ctk
from icon import set_icon
import re
from vanguard import vanguard_start
from Documents.reportDirectory import createReport
from Documents.PDFrapportsDirectory import createPDFRapports

def get_session_name(session_file):
    print("session test")
    session_name = None  # Initialiser session_name à None
    if os.path.exists(session_file):
        with open(session_file, 'r') as file:
            data = json.load(file)
            session_name = data.get('sessionName')  # Utilisez get pour obtenir la valeur avec une valeur par défaut None
            if session_name:
                print(f"Session existante trouvée : {session_name}")
                vanguard_start(session_name)
            else:
                # appelle de la fonction pour la création de la premiere session
                print("session file exists but session name is empty")
                create_first_session(session_file)

    return session_name

def create_first_session(session_file):
    # Créer une fenêtre toplevel
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue") 
    create_session = ctk.CTk()
    create_session.title("Create Session")
    create_session.configure(bg='#053225')
    set_icon(create_session)

    #Détermine les coordonnées pour centrer la fenêtre popup
    # Largeur et la hauteur de l'écran
    screen_width = create_session.winfo_screenwidth()
    screen_height = create_session.winfo_screenheight()
    popup_width = 400
    popup_height = 250
    x = (screen_width - popup_width) // 2
    y = (screen_height - popup_height) // 2

    # Positionne la fenêtre popup au centre de l'écran
    create_session.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

    labelEmailCheck = ctk.CTkLabel(create_session, text="Enter a name for your session :")
    labelEmailCheck.pack()

    entry_session_name = ctk.CTkEntry(create_session)
    entry_session_name.pack()

    check_and_write_session_name = ctk.CTkButton(create_session, text="Create", command=lambda: write_session_name(entry_session_name ,session_file), width=10)
    check_and_write_session_name.pack()
    
    print("window create")

    def write_session_name(entry_session_name, session_file):
        session_name = entry_session_name.get()
        if len(session_name) <= 4 or re.search(r'\W', session_name):
            print("La valeur doit être supérieure à 4 caractères et ne doit pas contenir de caractères spéciaux.")
        else:
            with open(session_file, 'w') as file:
                json.dump({'sessionName': session_name, "lightMode" : "light"}, file)
            print(f"Nouvelle session créée : {session_name}")
            createReport(session_name)
            createPDFRapports(session_name)
            vanguard_start(session_name, create_session)
                
    create_session.mainloop()
                
# appelle de la fonction
session_file = "json/session.json"  # Chemin vers le fichier de session
session_name = get_session_name(session_file)