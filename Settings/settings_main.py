import customtkinter as ctk
import json
from icon import set_icon

def settings_page(root):
    print("Start function called from startPage.py")

    def show_settings_window():
        #masquer la fenetre précédente
        root.withdraw()
        # Créer une nouvelle fenêtre toplevel
        settings_window = ctk.CTkToplevel(root)
        settings_window.title("Settings")
        settings_window.configure(bg='#053225')
        set_icon(settings_window)

        #Détermine les coordonnées pour centrer la fenêtre popup
        # Largeur et la hauteur de l'écran
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        popup_width = 500
        popup_height = 200
        x = (screen_width - popup_width) // 2
        y = (screen_height - popup_height) // 2
        # Positionne la fenêtre popup au centre de l'écran
        settings_window.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

        # Créer le cadre pour le premier bouton
        frame1 = ctk.CTkFrame(settings_window)
        frame1.place(relx=0.5, rely=0.2, anchor='center')

        # Initialize the switch_text variable
        switch_text = ctk.StringVar()

        # Initialize the switch_var variable
        switch_var = ctk.BooleanVar()

        # Load the JSON file
        with open('json/session.json', 'r') as file:
            data = json.load(file)

        # Initialize the switch based on the value of the "lightMode" key
        if data.get('lightMode') == 'dark':
            switch_var.set(True)
            switch_text.set("Dark")
        else:
            switch_var.set(False)
            switch_text.set("Light")

        # Update the switch_text variable whenever the switch_var variable changes
        switch_var.trace('w', lambda name, index, mode, switch_var=switch_var: update_switch_text(switch_var))

        switch = ctk.CTkSwitch(frame1, variable=switch_var, onvalue=True, offvalue=False, textvariable=switch_text)
        switch.pack(side=ctk.LEFT, padx=5, pady=5)

        # Configurer la fonction à appeler lors de la fermeture de la fenêtre
        settings_window.protocol("WM_DELETE_WINDOW", lambda: close_windows(settings_window))

        def update_switch_text(switch_var):
            # Load the JSON file
            with open('json/session.json', 'r') as file:
                data = json.load(file)

            if switch_var.get():
                switch_text.set("Dark")
                data['lightMode'] = 'dark'
                ctk.set_appearance_mode("dark")
            else:
                switch_text.set("Light")
                data['lightMode'] = 'light'
                ctk.set_appearance_mode("light")

            # Write the updated data back to the file
            with open('json/session.json', 'w') as file:
                json.dump(data, file)

    def close_windows(window):
        # Détruire la fenêtre actuelle (la nouvelle fenêtre)
        window.destroy()
        # Rappeler la fenêtre principale
        root.deiconify()

    # Appeler la fonction pour montrer la nouvelle fenêtre
    show_settings_window()