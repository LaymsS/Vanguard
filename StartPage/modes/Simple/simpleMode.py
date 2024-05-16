import customtkinter as ctk
from icon import set_icon
from StartPage.modes.Simple.osintMenu import *
from StartPage.modes.Simple.simpleActions.pwdAnalyser import pagePwdAnalyser
from StartPage.modes.Simple.simpleActions.authentificationWindow import  auth_window
from StartPage.modes.Simple.simpleActions.scanNmap import scan_page
from StartPage.modes.Simple.simpleActions.exploit import exploit_window


def simpleMode_page(root):
    print('fenetre simpleMode open')

    def show_simpleMode_window():
        #masquer la fenetre précédente
        root.withdraw()
        # Créer une nouvelle fenêtre toplevel
        simpleMode_window = ctk.CTkToplevel(root)
        simpleMode_window.title("Simple Mode")
        simpleMode_window.configure(bg='#053225')
        set_icon(simpleMode_window)

        #Détermine les coordonnées pour centrer la fenêtre popup
        # Largeur et la hauteur de l'écran
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        popup_width = 500
        popup_height = 270
        x = (screen_width - popup_width) // 2
        y = (screen_height - popup_height) // 2

        # Positionne la fenêtre popup au centre de l'écran
        simpleMode_window.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

        def osint_button_clicked():
            print(osintMenuInfo(simpleMode_window))

        def scan_button_clicked():
            print(scan_page(simpleMode_window))

        def detect_button_clicked():
            print("DETECT button clicked")

        def password_analyze_button_clicked():
            print(pagePwdAnalyser(simpleMode_window))

        def authentication_button_clicked():
            print(auth_window(simpleMode_window))

        def exploit_button_clicked():
            print(exploit_window(simpleMode_window))

        def post_exploit_button_clicked(): 
            print("POST-EXPLOIT button clicked")

        # Création des boutons dans la fenêtre simpleMode_window
        osint_button = ctk.CTkButton(simpleMode_window, text="OSINT", command=osint_button_clicked, )
        scan_button = ctk.CTkButton(simpleMode_window, text="SCAN", command=scan_button_clicked)
        detect_button = ctk.CTkButton(simpleMode_window, text="DETECT", command=detect_button_clicked)
        password_analyze_button = ctk.CTkButton(simpleMode_window, text="PASSWORD ANALYZE", command=password_analyze_button_clicked)
        authentication_button = ctk.CTkButton(simpleMode_window, text="AUTHENTICATION", command=authentication_button_clicked)
        exploit_button = ctk.CTkButton(simpleMode_window, text="EXPLOIT", command=exploit_button_clicked)
        post_exploit_button = ctk.CTkButton(simpleMode_window, text="POST-EXPLOIT", command=post_exploit_button_clicked)
        quit_button = ctk.CTkButton(simpleMode_window, text="QUIT", command=lambda: quit_windows(simpleMode_window))
        go_back_button = ctk.CTkButton(simpleMode_window, text="GO BACK", command=lambda: goback_windows(simpleMode_window))

        # Placement des boutons dans la grille
        osint_button.grid(row=0, column=0, padx=10, pady=10)
        scan_button.grid(row=0, column=1, padx=10, pady=10)
        detect_button.grid(row=0, column=2, padx=10, pady=10)
        password_analyze_button.grid(row=1, column=0, padx=10, pady=10)
        authentication_button.grid(row=1, column=1, padx=10, pady=10)
        exploit_button.grid(row=1, column=2, padx=10, pady=10)
        post_exploit_button.grid(row=2, column=1, pady=10)
        quit_button.grid(row=3, column=2, pady=75)
        go_back_button.grid(row=3, column=0, pady=75)

        # Configurer la fonction à appeler lors de la fermeture de la fenêtre
        simpleMode_window.protocol("WM_DELETE_WINDOW", lambda: close_window(simpleMode_window))

    def quit_windows(window):
        # Détruire la fenêtre actuelle (la nouvelle fenêtre)
        window.quit()

    def goback_windows(window):
        window.destroy()
        root.deiconify()

    def close_window(window):
        # Détruire la fenêtre actuelle (la nouvelle fenêtre)
        window.destroy()

        # Rappeler la fenêtre principale
        root.deiconify()
        
    # Appeler la fonction pour montrer la nouvelle fenêtre
    show_simpleMode_window()