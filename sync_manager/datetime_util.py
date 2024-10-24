import datetime
import os
from time import ctime, time
import ntplib
from logging_config import setup_logging

# Obtenir le logger configuré
logger = setup_logging()


def get_ntp_time():
    """
    Récupère l'heure depuis un serveur NTP.

    Returns:
        float: Le timestamp renvoyé par le serveur NTP ou None en cas d'erreur.
    """
    try:
        client = ntplib.NTPClient()
        response = client.request('ch.pool.ntp.org.')  # Utiliser un serveur NTP

        # Le timestamp renvoyé par le serveur NTP
        timestamp = response.tx_time

        return timestamp
    except Exception as e:
        # Si la commande échoue, écrire dans la sortie d'erreur (redirigée dans le fichier d'erreur)
        logger.error(f"Erreur lors de la synchronisation NTP: {e}\n")
        return None


def update_system_time(ntp_time):
    """
    Met à jour l'heure du système avec l'heure fournie par le serveur NTP.

    Args:
        ntp_time (float): Le timestamp du serveur NTP.
    """
    # Convertir le temps en format acceptable par 'date' sous Linux
    os.system(f'sudo date -s @{ntp_time}')
    logger.info(f"Heure système mise à jour: {ctime(ntp_time)}")


def check_and_sync_time():
    """
    Vérifie la différence entre l'heure locale et l'heure du serveur NTP
    et met à jour l'heure du système si nécessaire.

    Returns:
        float: Le timestamp validé ou None en cas d'erreur.
    """
    ntp_time = get_ntp_time()
    if ntp_time:
        local_time = time()
        time_diff = abs(ntp_time - local_time)

        if time_diff > 1:  # Si la différence dépasse 1 seconde
            logger.info(f"La différence de temps est de {time_diff} secondes, mise à jour nécessaire.")
            update_system_time(ntp_time)
            return ntp_time  # Retourner l'heure validée pour stockage
        else:
            logger.debug(f"L'heure système est correcte {datetime.datetime.fromtimestamp(ntp_time)}.")
            return ntp_time  # Retourner l'heure validée
    return None
