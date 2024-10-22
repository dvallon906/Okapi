import logging
import logging.handlers
import os

def setup_logging(log_file='/opt/okapi/logs/okapi.log'):
    logger = logging.getLogger('okapi')
    logger.debug(f"Le fichier de log est {log_file}")
    # Ne configure le logger que s'il n'est pas déjà configuré
    if not logger.hasHandlers():
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

        # Création du gestionnaire pour le fichier avec un niveau de log "INFO"
        file_handler = logging.handlers.RotatingFileHandler(
            log_file, maxBytes=10*1024*1024, backupCount=5  # Rotation de fichier de log
        )
        #file_handler.setLevel(logging.INFO)  # Niveau de log pour le fichier
        file_handler.setLevel(logging.DEBUG)  # Niveau de log pour le fichier
        file_formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        file_handler.setFormatter(file_formatter)

        # Création du gestionnaire pour la console avec un niveau de log "DEBUG"
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)  # Niveau de log pour la console
        console_formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        console_handler.setFormatter(console_formatter)

        # Configuration du logger principal
        logger = logging.getLogger('okapi')  # Nom du logger
        logger.setLevel(logging.DEBUG)  # Niveau minimum de log global

        # Ajout des gestionnaires au logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger