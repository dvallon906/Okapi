import configparser
import os
import sys
from time import sleep
from datetime_util import check_and_sync_time

def daemonize(print_debug):
    # Fork pour dissocier du parent
    if os.fork() > 0:
        sys.exit()

    os.setsid()  # Crée une nouvelle session et devient le leader
    os.umask(0)  # Change le masque de fichier pour le démon

    # Fork une seconde fois pour s'assurer de ne pas réacquérir un terminal de contrôle
    if os.fork() > 0:
        sys.exit()

    # Gestion des sorties selon print_debug
    sys.stdout.flush()


    user_home = os.path.expanduser('~')  # Récupère le répertoire personnel de l'utilisateur

    if print_debug:
        # Rediriger vers des fichiers si print-debug est true
        log_out = open(os.path.join(user_home, 'my_daemon_output.log'), 'a+')
        log_err = open(os.path.join(user_home, 'my_daemon_error.log'), 'a+')
        os.dup2(log_out.fileno(), sys.stdout.fileno())
        os.dup2(log_err.fileno(), sys.stderr.fileno())
    else:
        # Rediriger vers /dev/null si print-debug est false
        with open('/dev/null', 'r') as f:
            os.dup2(f.fileno(), sys.stdin.fileno())
        with open('/dev/null', 'a+') as f:
            os.dup2(f.fileno(), sys.stdout.fileno())
        with open('/dev/null', 'a+') as f:
            os.dup2(f.fileno(), sys.stderr.fileno())

def run():
    while True:
        while True:
            ntp_time = check_and_sync_time()
            if ntp_time:
                # Stocker l'heure certifiée pour une future utilisation
                user_home = os.path.expanduser('~')
                log_file_path = os.path.join(user_home, "last_time_certified.txt")
                with open(log_file_path, "w") as f:
                    f.write(f"{ntp_time}\n")
            sleep(10)

if __name__ == "__main__":

    # Lire le fichier de configuration
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Récupérer la valeur de l'option print-debug
    print_debug = config.getboolean('Settings', 'print-debug')

    daemonize(print_debug)
    run()



