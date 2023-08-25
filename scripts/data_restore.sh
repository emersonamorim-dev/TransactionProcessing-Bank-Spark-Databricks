#!/bin/bash

# Definindo variáveis
HDFS_PATH="/path/on/hdfs"
BACKUP_DIR="/path/to/local/backup/directory"
BACKUP_NAME="backup_to_restore.tar.gz"  

# Função para verificar se um comando foi bem-sucedido
check_exit_status() {
    if [ $? -ne 0 ]; then
        echo "Error: $1"
        exit 1
    fi
}

# Função para restaurar os dados
restore_data() {
    echo "Iniciando restauração dos dados..."

    # Descomprimindo o backup
    tar -xzf $BACKUP_DIR/$BACKUP_NAME -C $BACKUP_DIR

    check_exit_status "Falha ao descomprimir o backup."

    # Copiando dados restaurados para o HDFS
    hdfs dfs -copyFromLocal $BACKUP_DIR $HDFS_PATH

    check_exit_status "Falha ao copiar dados para o HDFS."

    echo "Restauração concluída com sucesso!"
}

main() {
    restore_data
}

main
