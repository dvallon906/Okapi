

# Variables pour compter les succès et les échecs
success_count=0
failure_count=0

# Fonction pour exécuter une commande et vérifier son succès
execute_command() {
    local description=$1
    local command=$2

    echo "\n--> $description"
    echo "Appuyez sur Enter pour exécuter la commande."
    read  # Attendre que l'utilisateur appuie sur Enter

    eval $command

    # Vérification du code de retour de la commande
    if [[ $? -ne 0 ]]; then
        echo "\n[ERREUR] La commande \"$command\" a échoué."
        ((failure_count++))  # Incrémenter le compteur d'échecs
    else
        echo "[OK] La commande \"$command\" a réussi."
        ((success_count++))  # Incrémenter le compteur de succès
    fi
}

# Étape pour supprimer le répertoire existant s'il est présent
remove_directory_if_exists() {
    local directory=$1

    if [[ -d $directory ]]; then
        echo "\nLe répertoire $directory existe déjà."
        echo "Appuyez sur Enter pour le supprimer."
        read  # Attendre que l'utilisateur appuie sur Enter
        execute_command "Suppression du répertoire $directory" "sudo rm -rf $directory"
    else
        echo "\n[INFO] Le répertoire $directory n'existe pas. Le clonage peut continuer."
    fi
}

# Vérifier et créer le répertoire /opt/okapi/daemons si nécessaire, puis se placer dedans
check_and_create_daemon_directory() {
    local daemon_dir="/opt/okapi/daemons"

    if [[ ! -d $daemon_dir ]]; then
        echo "\nLe répertoire $daemon_dir n'existe pas. Il va être créé."
        execute_command "Création du répertoire $daemon_dir" "sudo mkdir -p $daemon_dir"
    else
        echo "\n[INFO] Le répertoire $daemon_dir existe déjà."
    fi

    # Vérifier le propriétaire du répertoire
    local owner=$(stat -f "%Su" $daemon_dir)

    if [[ "$owner" != "root" ]]; then
        echo "\nLe répertoire $daemon_dir n'appartient pas à root. Propriétaire actuel : $owner"
        execute_command "Changer le propriétaire du répertoire en root" "sudo chown root:wheel $daemon_dir"
    else
        echo "\n[INFO] Le répertoire $daemon_dir est déjà possédé par root."
    fi

    # Se placer dans le répertoire /opt/okapi/daemons
    cd $daemon_dir
    echo "[INFO] Maintenant dans le répertoire $daemon_dir."
}

# Afficher une interface utilisateur dans le terminal
echo "=============================="
echo "   Gestion du démon Okapi"
echo "=============================="

# Chemin du répertoire à vérifier
repo_dir="/opt/okapi/daemons/ch.okapi.sync_manager"

# Étape avant de cloner : vérifier si le répertoire existe et proposer de le supprimer
remove_directory_if_exists $repo_dir

# Étape après suppression : vérifier et créer le répertoire /opt/okapi/daemons si nécessaire, puis se placer dedans
check_and_create_daemon_directory

# Étape 1 : Cloner le dépôt Git dans le répertoire actuel (qui est maintenant /opt/okapi/daemons)
execute_command "Cloner le dépôt Git ch.okapi.sync_manager" \
    "sudo git clone https://github.com/dvallon906/ch.okapi.sync_manager.git"

# Étape 2 : Décharger le service existant
execute_command "Décharger le service sync_manager_service (si existant)" \
    "sudo launchctl unload /Library/LaunchDaemons/sync_manager_service.plist"

# Étape 3 : Copier le fichier de service
execute_command "Copier le fichier sync_manager_service.plist vers /Library/LaunchDaemons/" \
    "sudo cp /opt/okapi/daemons/ch.okapi.sync_manager/services/sync_manager_service.plist /Library/LaunchDaemons/"

# Étape 4 : Rendre le script Python exécutable
execute_command "Rendre exécutable le script sync_manager.py" \
    "sudo chmod +x /opt/okapi/daemons/ch.okapi.sync_manager/sync_manager/sync_manager.py"

# Étape 5 : Charger le service
execute_command "Charger le service sync_manager_service" \
    "sudo launchctl load /Library/LaunchDaemons/sync_manager_service.plist"

# Étape 6 : Vérifier le statut du service
execute_command "Lister les services et rechercher le statut de sync_manager_service" \
    "sudo launchctl list | grep ch.okapi.sync_manager"

# Afficher un résumé des commandes exécutées
echo "\n=============================="
echo "Récapitulatif :"
echo "Commandes réussies : $success_count"
echo "Commandes échouées : $failure_count"
echo "=============================="