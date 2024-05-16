from enzoic import Enzoic

enzoic = Enzoic("d2e232e6b6fb42f684048fa33569d2ee", "j%Gn=NCKA?xNu!uH4=GATQ1RmffSu5YJ")

def passLeak(pwd):
    # Check compromission of a password
    if enzoic.check_password(pwd):
        print("Password is compromised")
        return True
    else:
        print("Password is not compromised")

def credentialsLeak(email, pwd):
    compromised_credential = 0
    compromised_credential_list = []
    if enzoic.check_credentials(email, pwd):
        print("Credentials are compromised")
        compromised_credential += 1
        compromised_credential_list.append(email, pwd)
        return compromised_credential, compromised_credential_list
    else:
        print("Credentials are not compromised")

def emailLeak(email):
    # Check compromission of an email
    exposures = enzoic.get_exposures_for_user(email)
    print(str(exposures["count"] + " exposures found for test@enzoic.com"))