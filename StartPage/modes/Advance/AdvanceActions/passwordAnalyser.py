from password_strength import PasswordPolicy, PasswordStats
from enzoic import Enzoic
import json, os

enzoic = Enzoic("d2e232e6b6fb42f684048fa33569d2ee", "j%Gn=NCKA?xNu!uH4=GATQ1RmffSu5YJ")

policy = PasswordPolicy.from_names(
    length=12,  # min length: 8
    uppercase=1,  # need min. 2 uppercase letters
    numbers=1,  # need min. 2 digits
    special=1,  # need min. 2 special characters
    nonletters=1,  # need min. 2 non-letter characters (digits, specials, anything)
)

def PassAnalyzer(password):
    stats = PasswordStats(password)
    if stats.strength() < 0.66666:
        return False
    elif stats.strength() < 0.66666:
        return True

        

def passLeak(password):
    # Check compromission of a password
    if enzoic.check_password(password):
        print("Password is compromised")
        return True
    else:
        print("Password is not compromised")
        return False

def get_session_name(session_file):
            if os.path.exists(session_file):
                with open(session_file, 'r') as file:
                    data = json.load(file)
                    session_name = data['sessionName']
            return session_name