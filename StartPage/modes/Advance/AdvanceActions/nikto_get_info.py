import json

def get_nikto_result(filename):
    
    with open(f'reports/{filename}_session/{filename}.json', 'r') as file:
        data = json.load(file)

    if "NiktoScan1" in data:
        nikto_scan_data = data["NiktoScan1"]
        
        target_host = nikto_scan_data["Target Host"]
        port_host = nikto_scan_data["Port Host"]
        outdated_app = nikto_scan_data["outdatedApp"]
        directory = nikto_scan_data["Directory"]
        sensitive = nikto_scan_data["Sensitive"]
        look_up = nikto_scan_data["lookUp"]
        credentials = nikto_scan_data["Credentials"]

        print("Informations du scan Nikto :")
        print(f"Target Host : {target_host}")
        print(f"Port Host : {port_host}")
        print(f"Outdated App : {outdated_app}")
        print("Directory :")
        for entry in directory:
            print(entry)
        print("Sensitive :")
        for entry in sensitive:
            print(entry)
        print("Look Up :")
        for entry in look_up:
            print(entry)
        print("Credentials :")
        for entry in credentials:
            print(entry)
    else:
        print("La clé 'NiktoScan1' n'a pas été trouvée dans le fichier JSON.")
    
    return target_host, port_host, outdated_app, directory, sensitive, look_up, credentials