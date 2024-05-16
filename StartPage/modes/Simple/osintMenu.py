import customtkinter as ctk
from icon import set_icon
from StartPage.modes.Simple.simpleActions.GatherDomainInfo import gatherDomainInfo

def osintMenuInfo(simpleMode_window):
    print('fenetre simpleMode open')

    def showOsintMenu():
        #masquer la fenetre précédente
        simpleMode_window.withdraw()
        # Créer une nouvelle fenêtre toplevel
        osintMenu_window = ctk.CTkToplevel(simpleMode_window)
        osintMenu_window.title("OSINT Simple Mode")
        set_icon(osintMenu_window)
        osintMenu_window.configure(bg='#053225')

        #Détermine les coordonnées pour centrer la fenêtre popup
        # Largeur et la hauteur de l'écran
        screen_width = simpleMode_window.winfo_screenwidth()
        screen_height = simpleMode_window.winfo_screenheight()
        popup_width = 500
        popup_height = 200
        x = (screen_width - popup_width) // 2
        y = (screen_height - popup_height) // 2

        # Positionne la fenêtre popup au centre de l'écran
        osintMenu_window.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

        def domain_button_clicked():
            print(gatherDomainInfo(osintMenu_window))

        def email_button_clicked():
            print("EMAIL button clicked")

        def username_button_clicked():
            print("USERNAME button clicked")


        # Création des boutons dans la fenêtre simpleMode_window
        domain_button = ctk.CTkButton(osintMenu_window, text="DOMAIN", command=domain_button_clicked)
        email_button = ctk.CTkButton(osintMenu_window, text="EMAIL", command=email_button_clicked)
        username_button = ctk.CTkButton(osintMenu_window, text="USERNAME", command=username_button_clicked)
        go_back_button = ctk.CTkButton(osintMenu_window, text="GO BACK", command=lambda: goback_windows(osintMenu_window))
        go_back_button.grid(row=2, column=0, padx=10, pady=75)
        quit_button = ctk.CTkButton(osintMenu_window, text="QUIT", command=lambda: quit_windows(osintMenu_window))
        quit_button.grid(row=2, column=2, pady=75)

        # Placement des boutons dans la grille
        domain_button.grid(row=0, column=0, padx=10, pady=10)
        email_button.grid(row=0, column=1, padx=10, pady=10)
        username_button.grid(row=0, column=2, padx=10, pady=10)

        # Configurer la fonction à appeler lors de la fermeture de la fenêtre
        osintMenu_window.protocol("WM_DELETE_WINDOW", lambda: close_window(osintMenu_window))

    def goback_windows(window):
        window.destroy()
        simpleMode_window.deiconify()
    
    def quit_windows(window):
        # Détruire la fenêtre actuelle (la nouvelle fenêtre)
        window.quit()

    def close_window(window):
        # Détruire la fenêtre actuelle (la nouvelle fenêtre)
        window.destroy()

        # Rappeler la fenêtre principale
        simpleMode_window.deiconify()
        
    # Appeler la fonction pour montrer la nouvelle fenêtre
    showOsintMenu()
    