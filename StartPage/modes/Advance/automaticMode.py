import customtkinter as ctk
from CTkListbox import *
from icon import set_icon
from StartPage.modes.Advance.AdvanceActions.automaticScan import scan_all, scan_all_without_port_service, scan_without_port_service, scan_without_service_with_port, scan_ip_with_port_service

def automatic_mode(root):
    print("Automatic mode launch")

    def show_automatic_window():
        root.withdraw()

        AutomaticMode_window = ctk.CTkToplevel(root)
        AutomaticMode_window.title("Automatic Mode")
        AutomaticMode_window.configure(bg='#053225', padx=20)
        set_icon(AutomaticMode_window)

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        popup_width = 650
        popup_height = 450
        x = (screen_width - popup_width) // 2
        y = (screen_height - popup_height) // 2
        AutomaticMode_window.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

        # Ajout des labels
        label = ctk.CTkLabel(AutomaticMode_window, text="Choose a specific IP or all IPs found :")
        label.grid(row=0, column=0, pady=10, sticky="w", padx=30)

        label3 = ctk.CTkLabel(AutomaticMode_window, text="Search for associates email :")
        label3.grid(row=2, column=0, pady=10, sticky="w", padx=30)

        label4 = ctk.CTkLabel(AutomaticMode_window, text="Choose a specific service or all Services :")
        label4.grid(row=3, column=0, pady=10, sticky="w", padx=30)

        label5 = ctk.CTkLabel(AutomaticMode_window, text="Do you want to try to exploit :")
        label5.grid(row=4, column=0, pady=10, sticky="w", padx=30)

        # Création des boutonso
        ip_selection = ctk.StringVar()
        specific_ip_radio = ctk.CTkRadioButton(AutomaticMode_window, text="Specific IP", variable=ip_selection, value="specific_ip")
        all_ips_radio = ctk.CTkRadioButton(AutomaticMode_window, text="All IPs", variable=ip_selection, value="all_ips")

        email_selection = ctk.StringVar()
        yes_email_compagny = ctk.CTkRadioButton(AutomaticMode_window, text="YES", variable=email_selection, value="email_yes")
        no_compagny_email = ctk.CTkRadioButton(AutomaticMode_window, text="NO", variable=email_selection, value="email_no")

        service_selection = ctk.StringVar()
        service_radio = ctk.CTkRadioButton(AutomaticMode_window, text="Specific Service", variable=service_selection, value="specific_service")
        services_radio = ctk.CTkRadioButton(AutomaticMode_window, text="All Services", variable=service_selection, value="all_services")

        exploit_selection = ctk.StringVar()
        exploit_yes = ctk.CTkRadioButton(AutomaticMode_window, text="YES", variable=exploit_selection, value="exploit_yes")
        exploit_no = ctk.CTkRadioButton(AutomaticMode_window, text="NO", variable=exploit_selection, value="exploit_no")

        # Placement des boutons radios
        specific_ip_radio.grid(row=0, column=1, pady=20, sticky="nsew", padx=25)
        all_ips_radio.grid(row=0, column=2, pady=20, sticky="nsew", padx=25)

        yes_email_compagny.grid(row=2, column=1, pady=20, sticky="nsew", padx=25)
        no_compagny_email.grid(row=2, column=2, pady=20, sticky="nsew", padx=25)

        service_radio.grid(row=3, column=1, pady=20, sticky="nsew", padx=25)
        services_radio.grid(row=3, column=2, pady=20, sticky="nsew", padx=25)

        exploit_yes.grid(row=4, column=1, pady=20, sticky="nsew", padx=25)
        exploit_no.grid(row=4, column=2, pady=20, sticky="nsew", padx=25)

        # les radio par défault
        all_ips_radio.invoke()
        yes_email_compagny.invoke()
        services_radio.invoke()
        exploit_yes.invoke()

        
        launch_button = ctk.CTkButton(AutomaticMode_window, text="LAUNCH", command=lambda: get_radio_value())
        quit_button = ctk.CTkButton(AutomaticMode_window, text="QUIT", command=lambda: quit_windows(AutomaticMode_window))
        go_back_button = ctk.CTkButton(AutomaticMode_window, text="GO BACK", command=lambda: goback_windows(AutomaticMode_window))
        quit_button.grid(row=5, column=2, pady=50)
        go_back_button.grid(row=5, column=0, pady=50)
        launch_button.grid(row=5, column=1, pady=50)

        def quit_windows(window):
            window.quit()

        def goback_windows(window):
            window.destroy()
            root.deiconify()

        def get_radio_value():
            print("get radio value press")
            ip_value = ip_selection.get()
            email_value = email_selection.get()
            service_value = service_selection.get()
            exploit_value = exploit_selection.get()

            print("IP selection:", ip_value)
            print("Email selection:", email_value)
            print("Service selection:", service_value)
            print("Exploit selection:", exploit_value)

            automatic_scan_personalize(ip_value, email_value, service_value, exploit_value, AutomaticMode_window)
    show_automatic_window()

def automatic_scan_personalize(ip_value, email_value, service_value, exploit_value, AutomaticMode_window):
    if ip_value == "specific_ip":
        all_ip = False
    else:
        all_ip = True

    if email_value == "email_yes":
        all_email = True
    else:
        all_email = False

    if service_value == "specific_service":
        all_service = False
    else:
        all_service = True

    if exploit_value == "exploit_yes":
        all_exploit = True
    else:
        all_exploit = False
    
    launch_all(all_ip, all_email, all_service, all_exploit, AutomaticMode_window)

def launch_all(all_ip, all_email, all_service, all_exploit, AutomaticMode_window):
    if all_ip and all_service:
        scan_all(all_email, all_exploit)
    elif not all_ip and not all_service:
        popup_ip_service(AutomaticMode_window, all_email, all_exploit)
    elif not all_ip and all_service:
        popup_ip(AutomaticMode_window, all_email, all_exploit)

def popup_ip(root, all_email, all_exploit):
    popup_window = ctk.CTkToplevel(root)
    popup_window.title("Personalize your options")
    popup_window.geometry("250x200")

    label = ctk.CTkLabel(popup_window, text="Enter the IP:")
    label.pack(pady=10)
    entry = ctk.CTkEntry(popup_window)
    entry.pack(pady=5)

    # Label pour afficher le message d'erreur
    error_label = ctk.CTkLabel(popup_window, text="Veuillez d'abord remplir le champ")
    error_label.pack(pady=5)
    error_label.pack_forget()  # Masquer le label par défaut

    # Bouton
    def submit_service():
        ip_name = entry.get()
        if not ip_name:  # Vérifier si le champ est vide
            error_label.pack()  # Afficher le message d'erreur
        else:
            error_label.pack_forget()  # Cacher le message d'erreur s'il était affiché précédemment
            popup_window.destroy()
            scan_ip_with_port_service(all_email, all_exploit, ip_name)
        
    button = ctk.CTkButton(popup_window, text="Select and launch", command=submit_service)
    button.pack(pady=10)

def popup_service(root):
    popup_window = ctk.CTkToplevel(root)
    popup_window.title("Personalize your options")
    popup_window.geometry("250x200")

    
    # Label
    label = ctk.CTkLabel(popup_window, text="Enter the service:")
    label.pack(pady=10)
    
    # Champ d'entrée (Entry)
    entry = ctk.CTkEntry(popup_window)
    entry.pack(pady=5)
    
    # Bouton
    def submit_service():
        service_name = entry.get()
        print("Name submitted:", service_name)
        popup_window.destroy()
        return service_name

    button = ctk.CTkButton(popup_window, text="Select and launch", command=submit_service)
    button.pack(pady=10)

def popup_ip_service(root, all_email, all_exploit):
    popup_window = ctk.CTkToplevel(root)
    popup_window.title("Personalize your options")
    popup_window.geometry("250x450")

    label = ctk.CTkLabel(popup_window, text="Enter the IP:")
    label.pack(pady=10)
    entry = ctk.CTkEntry(popup_window)
    entry.pack(pady=5)

    label2 = ctk.CTkLabel(popup_window, text="Select the Service from the list:")
    label2.pack(pady=10)
    
    selected_service = ctk.StringVar(popup_window)

    listbox = CTkListbox(popup_window)
    listbox.pack(fill="both", expand=True, padx=10, pady=10)

    listbox.insert(0, "Default")
    listbox.insert(1, "AFP")
    listbox.insert(2, "DHCP")
    listbox.insert(3, "DHCPv6")
    listbox.insert(4, "DNS")
    listbox.insert(5, "FTP")
    listbox.insert(6, "HTTPS")
    listbox.insert(7, "HTTP")
    listbox.insert(8, "Kerberos")
    listbox.insert(9, "LDAP")
    listbox.insert(10, "MySQL")
    listbox.insert(11, "RDP")
    listbox.insert(12, "SFTP")
    listbox.insert(13, "SSH")
    listbox.insert(14, "SMB")
    listbox.insert(15, "Syslog")
    listbox.insert(16, "Telnet")
    listbox.insert(17, "TFTP")

    # Bouton
    def submit_service():
        ip_name = entry.get()
        selected_service_value = listbox.get(listbox.curselection())  # Récupère la valeur sélectionnée dans la liste
        service_ports = {
            "Default": 0, "AFP": 548, "DHCP": 67, "DHCPv6": 546, "DNS": 53, "FTP": 21, "HTTPS": 443,
            "HTTP": 80, "Kerberos": 88, "LDAP": 389, "MySQL": 3306, "RDP": 3389, "SFTP": 22, "SSH": 22,
            "SMB": 445, "Syslog": 514, "Telnet": 23, "TFTP": 69
        }
        selected_port = service_ports.get(selected_service_value, "Port inconnu")
        print(selected_port)
        popup_window.destroy()
        scan_without_service_with_port(all_email, all_exploit, ip_name, selected_port)
        
    button = ctk.CTkButton(popup_window, text="Select and launch", command=submit_service)
    button.pack(pady=10)


def popup_ip_port_service(root):
    popup_window = ctk.CTkToplevel(root)
    popup_window.title("Personalize your options")
    popup_window.geometry("250x300")

    label = ctk.CTkLabel(popup_window, text="Enter the IP:")
    label.pack(pady=10)
    entry = ctk.CTkEntry(popup_window)
    entry.pack(pady=5)

    label2 = ctk.CTkLabel(popup_window, text="Enter the Port:")
    label2.pack(pady=10)
    entry2 = ctk.CTkEntry(popup_window)
    entry2.pack(pady=5)

    label3 = ctk.CTkLabel(popup_window, text="Enter the Service:")
    label3.pack(pady=10)
    entry3 = ctk.CTkEntry(popup_window)
    entry3.pack(pady=5)
    
    # Bouton
    def submit_service():
        ip_name = entry.get()
        port_name = entry2.get()
        service_name = entry3.get()
        popup_window.destroy()
        return ip_name, port_name, service_name

    button = ctk.CTkButton(popup_window, text="Select and launch", command=submit_service)
    button.pack(pady=10)