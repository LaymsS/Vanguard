import customtkinter as ctk
from tkinter import filedialog
from icon import set_icon
from tools.analyser.passAnalyzer2 import passAnalyzer2
from tools.analyser.passLeak import passLeak, credentialsLeak, emailLeak
from password_strength import PasswordPolicy, PasswordStats

policy = PasswordPolicy.from_names(
    length=12,  # min length: 8
    uppercase=1,  # need min. 2 uppercase letters
    numbers=1,  # need min. 2 digits
    special=1,  # need min. 2 special characters
    nonletters=1,  # need min. 2 non-letter characters (digits, specials, anything)
)

def pagePwdAnalyser(root):
    print('fenetre password analyser open')

    def checkPwd(entryField):
        if len(entryField) >= 4:
            if '@' in entryField:
                print("Mot de passe vérifié :", entryField)
                emailLeak(entryField)
                #a finir
                #a finir
                #a finir
            else:
                print("Il s'agit d'un username")
        else:
            print("Email ou Username invalid")

    def PassAnalyzer1(entryField, entryPassAnalyz1):
        print(entryField)
        stats = PasswordStats(entryField)
        print(stats.strength())
        pass_as_leak = passLeak(entryField)
        if pass_as_leak == True:
            print("The password ", entryField, " is compromised")
        else:
            print("The password ", entryField, " isn't compromised")
        if stats.strength() < 0.66666:
            print("Your password is weak")
        else:
            print("Your password is robust")
        print()
        entryPassAnalyz1.delete(0, ctk.END)

    def PassAnalyzerCSV():
        # Ouvrir une fenêtre de dialogue pour sélectionner un fichier
        file_path = filedialog.askopenfilename(title="Sélectionner un fichier", filetypes=[("CSV files", "*.csv")])
        # Vérifier si un fichier a été sélectionné
        if file_path:
            print(f"Fichier sélectionné : {file_path}")
            # Traitez ici le fichier sélectionné, par exemple, lisez le fichier CSV ou XLS
            passAnalyzer2(file_path)
        else:
            print("Aucun fichier sélectionné")

    def show_pwdAnalyser_window():
        #masquer la fenetre précédente
        root.withdraw()
        # Créer une nouvelle fenêtre toplevel
        show_pwdAnalyser_window = ctk.CTkToplevel(root)
        show_pwdAnalyser_window.title("Password and Email Analyser tool")
        set_icon(show_pwdAnalyser_window)
        show_pwdAnalyser_window.configure(bg='#053225')

        #Détermine les coordonnées pour centrer la fenêtre popup ainsi que Largeur et la hauteur de l'écran
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        popup_width = 900
        popup_height = 400
        x = (screen_width - popup_width) // 2
        y = (screen_height - popup_height) // 2

        # Positionne la fenêtre popup au centre de l'écran
        show_pwdAnalyser_window.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

        # Création des éléments de la fenêtre popup
        ctk.CTkLabel(show_pwdAnalyser_window, text="Enter your email adress and check for potentioal breaches :").grid(row=0, column=0, padx=10, pady=20)
        entryEmailCheck = ctk.CTkEntry(show_pwdAnalyser_window)
        entryEmailCheck.grid(row=0, column=1, padx=10, pady=20)
        ctk.CTkButton(show_pwdAnalyser_window, text="Verify", command=lambda: checkPwd(entryEmailCheck.get())).grid(row=0, column=2, padx=10, pady=20)

        ctk.CTkLabel(show_pwdAnalyser_window, text="Enter your password to check its robustness :").grid(row=1, column=0, padx=10, pady=20)
        entryPassAnalyz1 = ctk.CTkEntry(show_pwdAnalyser_window)
        entryPassAnalyz1.grid(row=1, column=1, padx=10, pady=20)
        ctk.CTkButton(show_pwdAnalyser_window, text="Verify", command=lambda: PassAnalyzer1(entryPassAnalyz1.get(), entryPassAnalyz1)).grid(row=1, column=2, padx=10, pady=20)

        ctk.CTkLabel(show_pwdAnalyser_window, text="Upload your local CSV password files :").grid(row=2, column=0, padx=10, pady=20)
        ctk.CTkButton(show_pwdAnalyser_window, text="Upload File", command=lambda: PassAnalyzerCSV()).grid(row=2, column=1, padx=10, pady=20)

        go_back_button = ctk.CTkButton(show_pwdAnalyser_window, text="GO BACK", command=lambda: goback_windows(show_pwdAnalyser_window))
        go_back_button.grid(row=3, column=0, padx=10, pady=75)
        quit_button = ctk.CTkButton(show_pwdAnalyser_window, text="QUIT", command=lambda: quit_windows(show_pwdAnalyser_window))
        quit_button.grid(row=3, column=2, pady=75)
        

        # Configurer la fonction à appeler lors de la fermeture de la fenêtre
        show_pwdAnalyser_window.protocol("WM_DELETE_WINDOW", lambda: close_window(show_pwdAnalyser_window))

        # Rendre la fenêtre simpleMode modale
        show_pwdAnalyser_window.grab_set()

    def goback_windows(window):
        window.destroy()
        root.deiconify()
    
    def quit_windows(window):
        window.quit()

    def close_window(window):
        window.destroy()

    # Appeler la fonction pour montrer la nouvelle fenêtre
    show_pwdAnalyser_window()
