import customtkinter as ctk
from StartPage.modes.Simple.simpleMode import simpleMode_page
from StartPage.modes.Advance.automaticMode import automatic_mode
from icon import set_icon

def start_page(root):
    print("Start function called from startPage.py")

    def show_start_window():
        #masquer la fenetre précédente
        root.withdraw()
        # Créer une nouvelle fenêtre toplevel
        start_window = ctk.CTkToplevel(root)
        start_window.title("Choosing Mode")
        start_window.configure(bg='#053225')
        set_icon(start_window)

        #Détermine les coordonnées pour centrer la fenêtre popup
        # Largeur et la hauteur de l'écran
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        popup_width = 500
        popup_height = 200
        x = (screen_width - popup_width) // 2
        y = (screen_height - popup_height) // 2
        # Positionne la fenêtre popup au centre de l'écran
        start_window.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

        # Créer le cadre pour le premier bouton
        frame1 = ctk.CTkFrame(start_window)
        frame1.place(relx=0.5, rely=0.2, anchor='center')

        # Créer le bouton One at a time Mode (simple)
        button1 = ctk.CTkButton(frame1, text="One at a time (simple)", command=lambda: simpleMode_page(start_window))
        button1.pack(side=ctk.LEFT, padx=5, pady=5)

        # Créer le texte pour le premier bouton
        text1 = ctk.CTkLabel(frame1, text="Select a specific action to execute", wraplength=300)
        text1.pack(side=ctk.BOTTOM, padx=10, pady=10)

        # Créer le cadre pour le deuxième bouton
        frame2 = ctk.CTkFrame(start_window)
        frame2.place(relx=0.5, rely=0.5, anchor='center')

        # Créer le bouton Automatic Mode
        button2 = ctk.CTkButton(frame2, text="Automatic (Advanced)", command=lambda: automatic_mode(start_window))
        button2.pack(side=ctk.LEFT, padx=5, pady=5)

        # Créer le texte pour le deuxième bouton
        text2 = ctk.CTkLabel(frame2, text="Choose and personnalize some action", wraplength=300)
        text2.pack(side=ctk.BOTTOM, padx=10, pady=10)

        # Configurer la fonction à appeler lors de la fermeture de la fenêtre
        start_window.protocol("WM_DELETE_WINDOW", lambda: close_windows(start_window))

    def close_windows(window):
        # Détruire la fenêtre actuelle (la nouvelle fenêtre)
        window.destroy()
        # Rappeler la fenêtre principale
        root.deiconify()

    # Appeler la fonction pour montrer la nouvelle fenêtre
    show_start_window()
