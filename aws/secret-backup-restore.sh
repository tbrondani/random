#!/bin/bash

SECRETS_DIR="secrets"
mkdir -p "$SECRETS_DIR"

[[ $# -eq 0 ]] && { echo "Usage: $0 --all | secret_name | --list list.txt | --restore secret_name | --restore-all"; exit 1; }

case $1 in
    --all)
        get_all_secrets
        ;;
    --list)
        get_secrets_from_list "$2"
        ;;
    --restore)
        restore_secret_from_backup "$2"
        ;;
    --restore-all)
        restore_all_secrets
        ;;
    *)
        process_secrets "$1"
        ;;
esac

# retrieve all secrets from aws USE WITH CAUTION as there is no rate limit here
get_all_secrets() {
    secrets=$(aws secretsmanager list-secrets --query 'SecretList[*].Name' --output text)
    process_secrets "$secrets"
}

# retrieve secrets based on txt file list.txt
get_secrets_from_list() {
    [[ ! -f $1 ]] && { echo "File $1 not found."; exit 1; }
    secrets=$(<"$1")
    process_secrets "$secrets"
}

# secret retriever function
process_secrets() {
    for secret in $1; do
        secret_value=$(aws secretsmanager get-secret-value --secret-id "$secret" --query 'SecretString' --output text)
        echo "$secret_value" > "$SECRETS_DIR/$secret.txt"
        echo "Saved secret $secret to $SECRETS_DIR/$secret.txt"
    done
}

# restore specified secret
restore_secret_from_backup() {
    backup_file="$SECRETS_DIR/$1.txt"
    [[ ! -f $backup_file ]] && { echo "Backup file $backup_file not found."; exit 1; }
    secret_value=$(<"$backup_file")
    aws secretsmanager create-secret --name "$1" --secret-string "$secret_value"
    echo "Restored secret $1 from $backup_file"
}

# restore all secrets from secrets folder, tags will not be restored as there is no way rnow to retrieve current tags using aws cli.
restore_all_secrets() {
    for backup_file in "$SECRETS_DIR"/*.txt; do
        secret_name=$(basename "$backup_file" .txt)
        secret_value=$(<"$backup_file")
        aws secretsmanager create-secret --name "$secret_name" --secret-string "$secret_value"
        echo "Restored secret $secret_name from $backup_file"
    done
}



echo "done"
