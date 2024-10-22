import datetime
import os
from time import ctime, time
import ntplib
from src.logging_config import setup_logging

# Obtenir le logger configuré
logger = setup_logging()


def get_ntp_time():
    try:
        client = ntplib.NTPClient()
        response = client.request('ch.pool.ntp.org.')  # Utiliser un serveur NTP

        # Le timestamp renvoyé par le serveur NTP
        timestamp = response.tx_time

        # Convertir le timestamp en objet datetime
        dt_object = datetime.datetime.fromtimestamp(timestamp)

        # Formater la date et l'heure au format français : jour/mois/année heure:minute:seconde avec jours, mois et années sur 2 chiffres
        formatted_time = dt_object.strftime("%d/%m/%y %H:%M:%S")

        # Si la commande réussit, écrire dans la sortie standard (redirigée dans le fichier log)

        logger.debug(f"{formatted_time} ok")


        return timestamp
    except Exception as e:

        # Si la commande échoue, écrire dans la sortie d'erreur (redirigée dans le fichier d'erreur)
        logger.error(f"Erreur lors de la synchronisation NTP: {e}\n")

        return None


def update_system_time(ntp_time):
    # Convertir le temps en format acceptable par 'date' sous Linux
    os.system(f'sudo date -s @{ntp_time}')
    logger.info(f"Heure système mise à jour: {ctime(ntp_time)}")


def check_and_sync_time():
    ntp_time = get_ntp_time()
    if ntp_time:
        local_time = time()
        time_diff = abs(ntp_time - local_time)

        if time_diff > 1:  # Si la différence dépasse 1 seconde
            logger.info(f"La différence de temps est de {time_diff} secondes, mise à jour nécessaire.")
            update_system_time(ntp_time)
            return ntp_time  # Retourner l'heure validée pour stockage
        else:
            logger.debug("L'heure système est correcte.")
            return ntp_time  # Retourner l'heure validée
    return None