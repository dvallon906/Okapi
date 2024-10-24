#!/bin/zsh

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

# Menu principal
main_menu() {
    while true; do
        echo "\n=============================="
        echo "   Menu - Gestion du démon Okapi"
        echo "=============================="
        echo "1) Décharger le service sync_manager_service (si existant)"
        echo "2) Charger le service sync_manager_service"
        echo "3) Lister les services et rechercher le statut de sync_manager_service"
        echo "Q) Quitter"
        echo "=============================="
        echo -n "Choisissez une option : "
        read choice

        case $choice in
            1)
                # Option 1 : Décharger le service existant
                execute_command "Décharger le service sync_manager_service (si existant)" \
                    "sudo launchctl unload /Library/LaunchDaemons/sync_manager_service.plist"
                ;;
            2)
                # Option 2 : Charger le service
                execute_command "Charger le service sync_manager_service" \
                    "sudo launchctl load /Library/LaunchDaemons/sync_manager_service.plist"
                ;;
            3)
                # Option 3 : Lister et rechercher le statut du service
                execute_command "Lister les services et rechercher le statut de sync_manager_service" \
                    "sudo launchctl list | grep ch.okapi.sync_manager"
                ;;
            Q|q)
                echo "Quitter..."
                break
                ;;
            *)
                echo "Option non valide. Veuillez choisir une option valide."
                ;;
        esac
    done

    # Afficher un résumé des commandes exécutées
    echo "\n=============================="
    echo "Récapitulatif :"
    echo "Commandes réussies : $success_count"
    echo "Commandes échouées : $failure_count"
    echo "=============================="
}

# Lancer le menu principal
main_menu