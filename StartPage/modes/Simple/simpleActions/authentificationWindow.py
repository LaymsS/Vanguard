import customtkinter as ctk
from icon import set_icon

def auth_window(root):
    print('fenetre authentification open')

    def show_auth_window():
        # Masquer la fenetre précédente
        root.withdraw()
        
        def validate_credentials():
            username = username_entry.get()
            password = password_entry.get()
            address = address_entry.get()
            print(f"Username: {username}, Password: {password}, Address: {address}")
            # Ici, on ajoutera la logique de validation des identifiants


        # Créer une nouvelle fenêtre toplevel
        auth_page = ctk.CTkToplevel(root)
        auth_page.title("Authentification")
        auth_page.configure(bg='#053225')
        set_icon(auth_page)

        # Détermine les coordonnées pour centrer la fenêtre popup ainsi que Largeur et la hauteur de l'écran
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        popup_width = 750
        popup_height = 400
        x = (screen_width - popup_width) // 2
        y = (screen_height - popup_height) // 2

        # Positionne la fenêtre popup au centre de l'écran
        auth_page.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

        auth_page.protocol("WM_DELETE_WINDOW", lambda: close_window(auth_page))

        # Rendre la fenêtre modale
        auth_page.grab_set()

        # Widgets
        ctk.CTkLabel(auth_page, text="Identifiant:", background='#053225', foreground='white').grid(row=0, column=0, padx=10, pady=20)
        username_entry = ctk.CTkEntry(auth_page)
        username_entry.grid(row=0, column=1, padx=10, pady=20)

        ctk.CTkLabel(auth_page, text="Mot de passe:", background='#053225', foreground='white').grid(row=1, column=0, padx=10, pady=20)
        password_entry = ctk.CTkEntry(auth_page, show="*")
        password_entry.grid(row=1, column=1, padx=10, pady=20)

        ctk.CTkLabel(auth_page, text="Adresse :", background='#053225', foreground='white').grid(row=2, column=0, padx=10, pady=20)
        address_entry = ctk.CTkEntry(auth_page)
        address_entry.grid(row=2, column=1, padx=10, pady=20)

        validate_button = ctk.CTkButton(auth_page, text="Check Credential", command=validate_credentials)
        validate_button.grid(row=3, column=0, columnspan=2, pady=20, padx=10)

    def close_window(window):
        # Détruire la fenêtre actuelle (la nouvelle fenêtre)
        window.destroy()

        # Rappeler la fenêtre principale
        root.deiconify()

    show_auth_window()
