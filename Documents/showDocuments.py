import os
import json
import datetime
import webbrowser
import customtkinter as ctk

def get_session_name(session_file):
    if os.path.exists(session_file):
        with open(session_file, 'r') as file:
            data = json.load(file)
            session_name = data['sessionName']
        return session_name

def open_pdf(file_path):
    webbrowser.open(file_path)

def list_pdfs():
    session_file = "json/session.json"
    session_name = get_session_name(session_file)
    directorySimple = f"PDFreports/{session_name}_session/simpleReport"
    directoryAdvance = f"PDFreports/{session_name}_session/advanceReport"

    # Récupérer la liste des fichiers PDF dans le répertoire simpleReport
    pdf_files_simple = [f for f in os.listdir(directorySimple) if f.endswith('.pdf')]
    # Récupérer la liste des fichiers PDF dans le répertoire advanceReport
    pdf_files_advance = [f for f in os.listdir(directoryAdvance) if f.endswith('.pdf')]

    # Créer une liste pour stocker les informations sur les fichiers PDF
    files_info_simple = []
    files_info_advance = []

    # Parcourir la liste des fichiers PDF du répertoire simpleReport et récupérer les informations
    for pdf_file in pdf_files_simple:
        file_path = os.path.join(directorySimple, pdf_file)
        file_name = pdf_file
        file_date = datetime.datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
        files_info_simple.append((file_name, file_date, file_path))

    # Parcourir la liste des fichiers PDF du répertoire advanceReport et récupérer les informations
    for pdf_file in pdf_files_advance:
        file_path = os.path.join(directoryAdvance, pdf_file)
        file_name = pdf_file
        file_date = datetime.datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
        files_info_advance.append((file_name, file_date, file_path))

    return files_info_simple, files_info_advance

def display_files(root):
    # Masquer la fenêtre principale
    root.withdraw()
    print('files documents display')
    files_info_simple, files_info_advance = list_pdfs()

    # Créer une fenêtre customtkinter
    report_window = ctk.CTkToplevel(root)
    report_window.title("PDF Report")

    #Détermine les coordonnées pour centrer la fenêtre popup
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    popup_width = 750
    popup_height = 400
    x = (screen_width - popup_width) // 2
    y = (screen_height - popup_height) // 2

    # Positionne la fenêtre popup au centre de l'écran
    report_window.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

    # Créer un cadre pour afficher la liste des fichiers
    frame_simple = ctk.CTkFrame(report_window)
    frame_simple.pack(side="left", padx=10, pady=10)
    frame_advance = ctk.CTkFrame(report_window)
    frame_advance.pack(side="right", padx=10, pady=10)

    # Afficher les fichiers PDF du répertoire simpleReport
    if files_info_simple:
        for file_name, file_date, file_path in files_info_simple:
            label = ctk.CTkLabel(frame_simple, text=f"{file_name} ({file_date})")
            label.pack(anchor='w')
            button = ctk.CTkButton(frame_simple, text="Ouvrir", command=lambda path=file_path: open_pdf(path))
            button.pack(anchor='w')
    else:
        label_no_report = ctk.CTkLabel(frame_simple, text="Aucun rapport à afficher pour le moment")
        label_no_report.pack()

    # Afficher les fichiers PDF du répertoire advanceReport
    if files_info_advance:
        for file_name, file_date, file_path in files_info_advance:
            label = ctk.CTkLabel(frame_advance, text=f"{file_name} ({file_date})")
            label.pack(anchor='w')
            button = ctk.CTkButton(frame_advance, text="Ouvrir", command=lambda path=file_path: open_pdf(path))
            button.pack(anchor='w')
    else:
        label_no_report = ctk.CTkLabel(frame_advance, text="Aucun rapport à afficher pour le moment")
        label_no_report.pack()

    # Configurer la fonction à appeler lors de la fermeture de la fenêtre
    report_window.protocol("WM_DELETE_WINDOW", lambda: close_window(report_window))

    # Masquer la fenêtre actuelle
    root.iconify()

    def close_window(window):
        # Détruire la fenêtre actuelle (la nouvelle fenêtre)
        window.destroy()
        # Rappeler la fenêtre principale
        root.deiconify()
