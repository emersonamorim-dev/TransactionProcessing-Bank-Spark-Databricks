#!/bin/bash

# Definindo variáveis
HDFS_PATH="/path/on/hdfs"
BACKUP_DIR="/path/to/local/backup/directory"
CURRENT_DATE=$(date +"%Y%m%d")
BACKUP_NAME="backup_$CURRENT_DATE.tar.gz"
AZURE_CONTAINER_NAME="your-azure-container-name"
AZURE_BLOB_NAME="your-azure-blob-name"
AZURE_CONNECTION_STRING="your-azure-connection-string"

# Função para verificar se um comando foi bem-sucedido
check_exit_status() {
    if [ $? -ne 0 ]; then
        echo "Error: $1"
        exit 1
    fi
}

# Função para verificar se um comando foi bem-sucedido
check_exit_status() {
    if [ $? -ne 0 ]; then
        echo "Error: $1"
        exit 1
    fi
}

# Função para criar backup dos dados
backup_data() {
    echo "Iniciando backup dos dados..."

    # Copiando dados do HDFS para o sistema local
    hdfs dfs -copyToLocal $HDFS_PATH $BACKUP_DIR

    check_exit_status "Falha ao copiar dados do HDFS."

    # Comprimindo os dados copiados
    tar -czf $BACKUP_DIR/$BACKUP_NAME -C $BACKUP_DIR .

    check_exit_status "Falha ao comprimir os dados."

    # Enviando o backup para o Azure Blob Storage
    az storage blob upload --account-name $AZURE_BLOB_NAME --container-name $AZURE_CONTAINER_NAME --type page_blob --name $BACKUP_NAME --type text/plain --file $BACKUP_DIR/$BACKUP_NAME --connection-string $AZURE_CONNECTION_STRING

    check_exit_status "Falha ao enviar o backup para o Azure Blob Storage."

    echo "Backup concluído com sucesso!"
}

main() {
    backup_data
}
