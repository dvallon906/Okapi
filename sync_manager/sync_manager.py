import configparser
import multiprocessing
import os
import signal
import sys
from time import sleep
from datetime_util import check_and_sync_time
from logging_config import setup_logging
from sync_task import run_sync_task
from info import __version__ as v

# Obtenir le logger configuré
logger = setup_logging()

data_file = os.path.expanduser("~/datas/last_time_certified.txt")
os.makedirs(os.path.dirname(data_file), exist_ok=True)


def run():
    """
    Fonction principale pour exécuter la tâche de synchronisation.
    """
    logger.info(f"Opération de synchronisation démarrée version {v}")
    try:
        while True:
            ntp_time = check_and_sync_time()
            if ntp_time:
                # Stocker l'heure certifiée pour une future utilisation
                with open(data_file, "w") as f:
                    f.write(f"{ntp_time}\n")
            sleep(10)
    except Exception as e:
        logger.error(f"Erreur lors de la synchronisation: {e}")


def main():
    """
    Fonction principale pour démarrer le gestionnaire de synchronisation.
    Gère le processus de synchronisation dans un processus séparé.
    """
    try:
        logger.info(f"Démarrage du gestionnaire de synchronisation version {v}")

        # Démarrer le processus pour la tâche de synchronisation
        sync_process = multiprocessing.Process(target=run_sync_task)
        sync_process.start()

        # Le processus principal peut continuer à faire d'autres choses ici
        # Par exemple, surveiller les signaux ou d'autres tâches.

        sync_process.join()  # Attendre la fin du processus enfant si nécessaire
    except Exception as e:
        logger.error(f"Erreur dans le processus principal: {e}")
    finally:
        logger.info("Arrêt du gestionnaire de synchronisation")


def signal_handler(sig, frame):
    """
    Gère les signaux pour un arrêt propre.
    """
    logger.info(f"Le script s'est arrêté à cause du signal: {signal.Signals(sig).name}")
    sys.exit(0)


def on_exit():
    """
    Fonction appelée à la fin du script.
    """
    logger.info("Le script s'est arrêté normalement.")


if __name__ == "__main__":
    # Gérer les signaux pour un arrêt propre
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # Lire le fichier de configuration
    config = configparser.ConfigParser()
    config.read('config.ini')

    main()
