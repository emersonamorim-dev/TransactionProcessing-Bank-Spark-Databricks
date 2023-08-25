#!/bin/bash

# Definindo variáveis
FLASK_APP_PATH="/path/to/your/flask/project/app.py"
FLASK_APP="your_flask_app_name"  

# Função para verificar se um comando foi bem-sucedido
check_exit_status() {
    if [ $? -ne 0 ]; then
        echo "Error: $1"
        exit 1
    fi
}

# Função para reverter a última migração
rollback_last_migration() {
    echo "Revertendo a última migração..."

    # Definindo a variável de ambiente FLASK_APP
    export FLASK_APP=$FLASK_APP_PATH

    # Usando o flask db downgrade para reverter a última migração
    flask db downgrade

    check_exit_status "Falha ao reverter a migração."
}

main() {
    rollback_last_migration

    echo "Migração revertida com sucesso!"
}

main
