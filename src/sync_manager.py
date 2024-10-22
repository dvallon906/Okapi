import configparser
import multiprocessing
import os
import signal
import sys
from time import sleep

from datetime_util import check_and_sync_time
from logging_config import setup_logging
from sync_task import run_sync_task

# Obtenir le logger configuré
logger = setup_logging()

data_file = "/opt/okapi/datas/last_time_certified.txt"
os.makedirs(os.path.dirname(data_file), exist_ok=True)

def run():
        logger.info("Opération de synchronisation démarrée")
        try:
            while True:
                ntp_time = check_and_sync_time()
                if ntp_time:
                    # Stocker l'heure certifiée pour une future utilisation
                    with open(data_file, "w") as f:
                        f.write(f"{ntp_time}\n")
                sleep(10)
        except Exception as e:
            logger.error("Erreur lors de la synchronisation: %s", e)


def main():
    try:
        logger.info("Démarrage du gestionnaire de synchronisation")

        # Démarrer le processus pour la tâche de synchronisation
        sync_process = multiprocessing.Process(target=run_sync_task)
        sync_process.start()

        # Le processus principal peut continuer à faire d'autres choses ici
        # Par exemple, surveiller les signaux ou d'autres tâches.

        sync_process.join()  # Attendre la fin du processus enfant si nécessaire
    except Exception as e:
        logger.error("Erreur dans le processus principal: %s", e)
    finally:
        logger.info("Arrêt du gestionnaire de synchronisation")

def signal_handler(sig, frame):
    logger.info(f"Le script s'est arrêté à cause du signal: {signal.Signals(sig).name}")
    sys.exit(0)

def on_exit():
    logger.info("Le script s'est arrêté normalement.")

if __name__ == "__main__":


    # Lire le fichier de configuration
    config = configparser.ConfigParser()
    config.read('config.ini')

    main()



