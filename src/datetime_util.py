import os
from time import ctime, time

import ntplib


def get_ntp_time():
    try:
        client = ntplib.NTPClient()
        response = client.request('pool.ntp.org')  # Utiliser un serveur NTP
        return response.tx_time
    except Exception as e:
        print(f"Erreur lors de la synchronisation NTP: {e}")
        return None


def update_system_time(ntp_time):
    # Convertir le temps en format acceptable par 'date' sous Linux
    os.system(f'sudo date -s @{ntp_time}')
    print(f"Heure système mise à jour: {ctime(ntp_time)}")


def check_and_sync_time():
    ntp_time = get_ntp_time()
    if ntp_time:
        local_time = time()
        time_diff = abs(ntp_time - local_time)

        if time_diff > 1:  # Si la différence dépasse 1 seconde
            print(f"La différence de temps est de {time_diff} secondes, mise à jour nécessaire.")
            update_system_time(ntp_time)
            return ntp_time  # Retourner l'heure validée pour stockage
        else:
            print("L'heure système est correcte.")
            return ntp_time  # Retourner l'heure validée
    return None