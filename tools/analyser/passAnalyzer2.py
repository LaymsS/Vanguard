import csv
from password_strength import PasswordPolicy, PasswordStats

policy = PasswordPolicy.from_names(
    length=12,  # min length: 8
    uppercase=1,  # need min. 2 uppercase letters
    numbers=1,  # need min. 2 digits
    special=1,  # need min. 2 special characters
    nonletters=1,  # need min. 2 non-letter characters (digits, specials, anything)
)

def passAnalyzer2(file_path):
    count_weak_password = 0
    nbr_cells = 0
    weak_pass = []

    cells = read_cells(file_path)
    
    # Afficher les valeurs stockées
    for cell in cells:
        nbr_cells += 1
        print(cell)
        stats = PasswordStats(cell)
        print(stats.strength())
        if stats.strength() < 0.66666:
            count_weak_password += 1
            weak_pass.append(cell)

    print("Nombre mot de passe faible = ", count_weak_password)
    print(weak_pass)

def read_cells(file_path):
    cells_list = []
    
    try:
        # Ouvrir le fichier avec l'encodage Windows-1252
        with open(file_path, 'r', encoding='ISO-8859-15') as file:
            reader = csv.reader(file)
            
            # Lire la première cellule de chaque ligne jusqu'à ce qu'elle soit vide
            for row in reader:
                if row and row[0]:  # Vérifier si la liste n'est pas vide et si la première cellule n'est pas vide
                    cells_list.append(row[0])
                else:
                    break  # Sortir de la boucle si la première cellule est vide
                    
        return cells_list
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return None
