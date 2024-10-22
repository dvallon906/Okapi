# sync_task.py

import os
from time import sleep
from datetime_util import check_and_sync_time
from logging_config import setup_logging

# Obtenir le logger configuré
logger = setup_logging()

data_file = "/opt/okapi/datas/last_time_certified.txt"
os.makedirs(os.path.dirname(data_file), exist_ok=True)

def run_sync_task():
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