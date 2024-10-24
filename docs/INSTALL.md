# Instructions d'installation

## 1. Deamon de supervision

### 1. Copier le fichier du script

Copiez le script Python dans `/usr/local/bin/` ou un autre dossier adapté :

```bash
sudo cp src/sync_manager.py /usr/local/bin/
sudo cp src/datetime_util.py /usr/local/bin/
sudo cp src/logging_config.py /usr/local/bin/
sudo cp src/sync_task.py /usr/local/bin/
sudo chmod +x /usr/local/bin/sync_manager.py
```

### 2. Pour Linux Copier le fichier de systemd

Copiez le fichier sync_manager_service.service dans `/etc/systemd/system/`
```bash
sudo cp services/sync_manager_service.service /etc/systemd/system/
```
Voir les dix derniers logs 
```bash
tail /opt/okapi/logs/okapi.log
```


### 2. Pour MacOS
Copiez le fichier sync_manager_service.plist dans `/Library/LaunchDaemons/`
```bash
sudo cp services/sync_manager_service.plist /Library/LaunchDaemons/
sudo chmod +x /usr/local/bin/sync_manager.py
```
2.1 Préparer le lancement du service
```bash
sudo launchctl load /Library/LaunchDaemons/sync_manager_service.plist
```

2.2 Démarer le service
```bash
sudo launchctl start ch.okapi.sync_manager_service 
```

option Stoper le service
```bash
sudo launchctl unload /Library/LaunchDaemons/sync_manager_service.plist
```

2.3 Vérifier que le servide est bien lancé
```bash
sudo launchctl list | grep ch.okapi.sync_manager_service
```
la réponce soit ressemblé à : <2670    0       ch.okapi.sync_manager_service>





