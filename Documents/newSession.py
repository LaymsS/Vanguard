import customtkinter as ctk
import json
import re
from icon import set_icon
from Documents.PDFrapportsDirectory import createPDFRapports

def rewrite_session(root):
    from vanguard import vanguard_start
    root.destroy()

    # Créer une fenêtre toplevel
    create_session = ctk.CTk()
    create_session.title("New Session")
    create_session.configure(bg='#053225')
    set_icon(create_session)

    #Détermine les coordonnées pour centrer la fenêtre popup
    # Largeur et la hauteur de l'écran
    screen_width = create_session.winfo_screenwidth()
    screen_height = create_session.winfo_screenheight()
    popup_width = 250
    popup_height = 250
    x = (screen_width - popup_width) // 2
    y = (screen_height - popup_height) // 2

    # Positionne la fenêtre popup au centre de l'écran
    create_session.geometry(f"{popup_width}x{popup_height}+{x}+{y}")
    
    #label
    labelEmailCheck = ctk.CTkLabel(create_session, text="Enter a name for your session :")
    labelEmailCheck.pack()

    #input
    entry_session_name = ctk.CTkEntry(create_session)
    entry_session_name.pack()
    
    #bouton
    check_and_write_session_name = ctk.CTkButton(create_session, text="Create", command=lambda: write_session_name(vanguard_start,create_session,entry_session_name))
    check_and_write_session_name.pack()

    create_session.protocol("WM_DELETE_WINDOW", lambda: close_windows(create_session))

def write_session_name(vanguard_start,create_session,entry_session_name):
    from Documents.writeSession import show_new_session
    from Documents.reportDirectory import createReport
    session_file = "json/session.json"
    print(entry_session_name)
    session_name = entry_session_name.get()
    if len(session_name) < 4 or re.search(r'\W', session_name):
        print("La valeur doit être supérieure à 4 caractères et ne doit pas contenir de caractères spéciaux.")
        return

    with open(session_file, 'w') as file:
        json.dump({'sessionName': session_name}, file)
        
    print(f"Nouvelle session créée : {session_name}")
    createReport(session_name)
    createPDFRapports(session_name)
    show_new_session(vanguard_start, session_name, create_session)

def close_windows(window):
    # Détruire la fenêtre actuelle (la nouvelle fenêtre)
    window.destroy()
