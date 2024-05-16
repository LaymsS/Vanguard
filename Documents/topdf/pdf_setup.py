from  templates.spiderGraphMitre import create_spider_graph_mitre
from templates.vulnGraph import create_vuln_graph
from templates.generate_rapport import report_generation, report_generation_service
from StartPage.modes.Advance.AdvanceActions.nikto_get_info import get_nikto_result
from StartPage.modes.Advance.AdvanceActions.get_email_result import get_email_result
from StartPage.modes.Advance.AdvanceActions.ssh_get_result import get_ssh_result
from StartPage.modes.Advance.AdvanceActions.postexploit_get_result import get_postexploit_result
import json, os


def setup_rapport():

    def get_session_name(session_file):
        if os.path.exists(session_file):
            with open(session_file, 'r') as file:
                data = json.load(file)
                session_name = data['sessionName']
            return session_name
        
    session_file = "json/session.json"
    try:
        session_name = get_session_name(session_file)
        spider_file_path = create_spider_graph_mitre()
        vul_file_path = create_vuln_graph()
        email_data = get_email_result(session_name)
        sensitive_pem_files, other_sensitive_files, software_list, total_software_found, total_user_found, users_list = get_postexploit_result(session_name)
        result = get_ssh_result(session_name)
        if result is not None:
            ssh_result, username_ssh, password_ssh, leak_ssh, robustness_ssh = result
        else:
            ssh_result, username_ssh, password_ssh, leak_ssh, robustness_ssh = None, None, None, None, None
        target_host, port_host, outdated_app, directory, sensitive, look_up, credentials = get_nikto_result(session_name)
        report_generation(spider_file_path, vul_file_path, session_name, target_host, port_host, outdated_app, directory, sensitive, look_up, 
                        credentials, email_data, ssh_result, username_ssh, password_ssh, leak_ssh, robustness_ssh, sensitive_pem_files, 
                        other_sensitive_files, software_list, total_software_found, total_user_found, users_list)
    except ValueError:
        print(ValueError)
        print("Impossible de récupérer certaine informations via les scans. Impossible de générer le rapport")
        print("Relancer le scan avec des paramètres différents")


def setup_service_rapport():

    def get_session_name(session_file):
        if os.path.exists(session_file):
            with open(session_file, 'r') as file:
                data = json.load(file)
                session_name = data['sessionName']
            return session_name
        
    session_file = "json/session.json"
    session_name = get_session_name(session_file)
    report_generation_service(session_name)

