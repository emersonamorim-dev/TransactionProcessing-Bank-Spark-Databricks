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

# Função para aplicar migrações
apply_migrations() {
    echo "Aplicando migrações..."

    # Definindo a variável de ambiente FLASK_APP
    export FLASK_APP=$FLASK_APP_PATH

    # Usando o flask db upgrade para aplicar migrações
    flask db upgrade

    check_exit_status "Falha ao aplicar migrações."
}

main() {
    apply_migrations

    echo "Migrações aplicadas com sucesso!"
}

main

