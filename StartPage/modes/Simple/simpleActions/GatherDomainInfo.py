import customtkinter as ctk
import subprocess
import re
from icon import set_icon

def gatherDomainInfo(osintMenu_window):
    print('window gather domain info open')

    def showGatherAction():
        # Masquer la fenetre précédente
        osintMenu_window.withdraw()

        # Créer une nouvelle fenêtre topleve
        gatherInfo_window = ctk.CTkToplevel(osintMenu_window)
        gatherInfo_window.title("Simple Information Gathering")
        set_icon(gatherInfo_window)
        gatherInfo_window.configure(bg='#053225')

        # Détermine les coordonnées pour centrer la fenêtre popup
        screen_width = osintMenu_window.winfo_screenwidth()
        screen_height = osintMenu_window.winfo_screenheight()
        popup_width = 650
        popup_height = 250
        x = (screen_width - popup_width) // 2
        y = (screen_height - popup_height) // 2

        # Positionne la fenêtre popup au centre de l'écran
        gatherInfo_window.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

        # Texte d'instruction
        label_instruction = ctk.CTkLabel(gatherInfo_window, text="Search subdomain from principal domain")
        label_instruction.grid(row=0, column=0, padx=10, pady=10)

        # Widget Text pour l'entrée de texte
        text_area = ctk.CTkEntry(gatherInfo_window, height=1, width=150)
        text_area.grid(row=0, column=1, padx=10, pady=10)

        # Fonction pour afficher le texte saisi
        def display_text():
            input_text = text_area.get("1.0", "end-1c").strip()
            if input_text:
                command = f"theHarvester -d {input_text} -l 200 -b duckduckgo,bing"
                try:
                    result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, text=True)
                    output = result.stdout

                    # Utilisation d'expressions régulières pour extraire les informations spécifiques
                    hosts_found_match = re.search(r"Hosts found : (\d+)", output)

                    if hosts_found_match:
                        hosts_found = hosts_found_match.group(1)
                        label_result.config(text=f"Hosts found: {hosts_found}")
                    else:
                        label_result.config(text="Informations non trouvées.")
                except subprocess.CalledProcessError as e:
                    label_result.config(text=f"Erreur lors de l'exécution de la commande : {e}")
            else:
                label_result.config(text="Veuillez entrer un domaine valide.")

        # Bouton pour afficher le texte saisi
        button_display = ctk.CTkButton(gatherInfo_window, text="Research", command=display_text)
        button_display.grid(row=0, column=2, padx=10, pady=10)

        # Label pour afficher le résultat
        label_result = ctk.CTkLabel(gatherInfo_window, text="Hosts found :")
        label_result.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        go_back_button = ctk.CTkButton(gatherInfo_window, text="GO BACK", command=lambda: goback_windows(gatherInfo_window))
        go_back_button.grid(row=2, column=0, padx=10, pady=75)
        quit_button = ctk.CTkButton(gatherInfo_window, text="QUIT", command=lambda: quit_windows(gatherInfo_window))
        quit_button.grid(row=2, column=2, pady=75)
        

        # Configurer la fonction à appeler lors de la fermeture de la fenêtre
        gatherInfo_window.protocol("WM_DELETE_WINDOW", lambda: close_window(gatherInfo_window))

    def goback_windows(window):
        window.destroy()
        osintMenu_window.deiconify()
    
    def quit_windows(window):
        # Détruire la fenêtre actuelle (la nouvelle fenêtre)
        window.quit()

    def close_window(window):
        window.destroy()
        osintMenu_window.deiconify()

    # Appeler la fonction pour montrer la nouvelle fenêtre
    showGatherAction()
