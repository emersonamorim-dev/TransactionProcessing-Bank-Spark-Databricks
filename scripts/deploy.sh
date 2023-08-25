#!/bin/bash

# Definindo variáveis
DOCKER_COMPOSE_FILE="docker-compose.yml"
APP_NAME="my_app"
IMAGE_NAME="my_app_image"
IMAGE_VERSION="latest"

# Função para verificar se um comando foi bem-sucedido
check_exit_status() {
    if [ $? -ne 0 ]; then
        echo "Error: $1"
        exit 1
    fi
}

# Função para construir a imagem Docker
build_docker_image() {
    echo "Construindo imagem Docker..."

    docker build -t $IMAGE_NAME:$IMAGE_VERSION .

    check_exit_status "Falha ao construir a imagem Docker."
}

# Função para implantar a aplicação
deploy_app() {
    echo "Implantando aplicação..."

    docker-compose -f $DOCKER_COMPOSE_FILE up -d

    check_exit_status "Falha ao implantar a aplicação."
}

# Função principal
main() {
    build_docker_image
    deploy_app

    echo "Aplicação $APP_NAME implantada com sucesso!"
}

main
