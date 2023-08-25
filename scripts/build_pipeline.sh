#!/bin/bash

# Definindo variáveis
JENKINS_URL="http://your-jenkins-url"
JOB_NAME="Your-Job-Name"
JENKINS_USER="your-jenkins-username"
JENKINS_TOKEN="your-jenkins-token" 

# Função para verificar se um comando foi bem-sucedido
check_exit_status() {
    if [ $? -ne 0 ]; then
        echo "Error: $1"
        exit 1
    fi
}

# Função para construir a pipeline no Jenkins
build_pipeline() {
    echo "Iniciando a construção da pipeline..."

    # Disparando a construção no Jenkins
    curl -X POST "$JENKINS_URL/job/$JOB_NAME/build" \
         --user $JENKINS_USER:$JENKINS_TOKEN

    check_exit_status "Falha ao construir a pipeline. Verifique o Jenkins para detalhes."

    echo "Pipeline iniciada com sucesso!"
}

main() {
    build_pipeline
}

main
