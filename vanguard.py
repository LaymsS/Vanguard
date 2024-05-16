import customtkinter as ctk
import json
from PIL import Image
from time import sleep

# Fonction page call
from icon import set_icon
from StartPage.start_main import start_page
from Settings.settings_main import settings_page
from Documents.showDocuments import display_files
from Documents.newSession import rewrite_session

def open_page(page_name, root):
    if page_name == "Start":
        start_page(root)
    elif page_name == "Documents":
        display_files(root)
    elif page_name == "Profils":
        profils_page()
    elif page_name == "Settings":
        settings_page(root)

def profils_page():
    print("Page Profils")

def vanguard_start(session_name, create_session=None):
    print("lancé")
    print(session_name)
    update_theme()
    print(create_session)
    if create_session:
        create_session.destroy()
    root = ctk.CTk()
    root.title("Vanguard")
    root.configure(bg='#053225')
    set_icon(root)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    popup_width = 280
    popup_height = 500 
    x = (screen_width - popup_width) // 2
    y = (screen_height - popup_height) // 2
    root.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

    label_session = ctk.CTkLabel(root, text="Current Session : " +session_name)
    label_session.place(relx=0.5, rely=0.6, anchor='center')

    button_frame = ctk.CTkFrame(root)
    button_frame.place(relx=0.5, rely=0.3, anchor='center')

    menu_labels = ["Start", "Documents", "Profils", "Settings"]

    # Ajoutez une image pour chaque bouton
    image_start = ctk.CTkImage(light_image=Image.open("StartPage/images/start.gif"))
    image_documents = ctk.CTkImage(light_image=Image.open("StartPage/images/document.gif"))
    image_profils = ctk.CTkImage(light_image=Image.open("StartPage/images/profil.gif"))
    image_settings = ctk.CTkImage(light_image=Image.open("StartPage/images/settings.gif"))
    print(type(image_start._light_image))
    print(type(image_documents._light_image))
    print(type(image_profils._light_image))
    print(type(image_settings._light_image))


    button_images = [image_start, image_documents, image_profils, image_settings]

    for index, (label, image) in enumerate(zip(menu_labels, button_images)):
        menu_button = ctk.CTkButton(button_frame, text=label, image=image, compound="left", command=lambda l=label: open_page(l, root), width=250, height=35)
        menu_button.grid(row=index, column=0, columnspan=2, padx=10, pady=10)

    button_session = ctk.CTkButton(root, text="Start New Session", width=150, command=lambda: rewrite_session(root))
    button_session.place(relx=0.5, rely=0.7, anchor='center')

    button_exit = ctk.CTkButton(root, text="Exit", width=150, command=lambda: close_windows(root))
    button_exit.place(relx=0.5, rely=0.8, anchor='center')

    # Configurer la fonction à appeler lors de la fermeture de la fenêtre
    root.protocol("WM_DELETE_WINDOW", lambda: close_windows(root))
    root.mainloop()

def close_windows(window):
    # Détruire la fenêtre actuelle (la nouvelle fenêtre)
    window.destroy()

def update_theme():
    # Load the JSON file
    with open('json/session.json', 'r') as file:
        data = json.load(file)

    # Update the appearance mode based on the value of the "lightMode" key
    if data.get('lightMode') == 'dark':
        ctk.set_appearance_mode("dark")
    else:
        ctk.set_appearance_mode("light")
