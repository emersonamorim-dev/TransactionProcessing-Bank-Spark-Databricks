#!/bin/bash

# Definindo variáveis
SPARK_MASTER_URL="spark://your-spark-master-url:7077"
LOG_DIR="/path/to/your/log/directory"

# Função para verificar se um comando foi bem-sucedido
check_exit_status() {
    if [ $? -ne 0 ]; then
        echo "Error: $1"
        exit 1
    fi
}

# Função para coletar informações do cluster Spark
collect_spark_info() {
    echo "Coletando informações do cluster Spark..."

    # Coletando informações do Spark Master
    curl -o $LOG_DIR/spark_master_info.log $SPARK_MASTER_URL

    check_exit_status "Falha ao coletar informações do Spark Master."

    # Coletando logs do Spark Master
    cp /path/to/spark/logs/spark-master.log $LOG_DIR/

    check_exit_status "Falha ao coletar logs do Spark Master."

    echo "Informações do Spark coletadas com sucesso!"
}

main() {
    collect_spark_info
}

main
