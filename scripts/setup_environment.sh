#!/bin/bash

# Definindo variáveis
PROJECT_DIR="/path/to/your/flask/project"
VENV_DIR="$PROJECT_DIR/venv"
REQUIREMENTS="$PROJECT_DIR/requirements.txt"

# Função para verificar se um comando foi bem-sucedido
check_exit_status() {
    if [ $? -ne 0 ]; then
        echo "Error: $1"
        exit 1
    fi
}

# Função para atualizar o sistema
update_system() {
    echo "Atualizando o sistema..."
    sudo apt-get update
    sudo apt-get upgrade -y
    check_exit_status "Falha ao atualizar o sistema."
}

# Função para instalar dependências do sistema
install_system_dependencies() {
    echo "Instalando dependências do sistema..."
    sudo apt-get install -y python3 python3-pip python3-venv git
    check_exit_status "Falha ao instalar dependências do sistema."
}

# Função para configurar o ambiente virtual Python
setup_virtualenv() {
    echo "Configurando ambiente virtual..."
    python3 -m venv $VENV_DIR
    source $VENV_DIR/bin/activate
    check_exit_status "Falha ao configurar o ambiente virtual."
}

# Função para instalar dependências do Python
install_python_dependencies() {
    echo "Instalando dependências do Python..."
    if [ -f $REQUIREMENTS ]; then
        pip3 install -r $REQUIREMENTS
        check_exit_status "Falha ao instalar dependências do Python."
    else
        echo "Arquivo requirements.txt não encontrado. Pulando instalação de dependências do Python."
    fi
}

# Função para instalar Flask (se não estiver no requirements.txt)
install_flask() {
    echo "Instalando Flask..."
    pip3 install Flask
    check_exit_status "Falha ao instalar Flask."
}

main() {
    update_system
    install_system_dependencies
    setup_virtualenv
    install_python_dependencies
    install_flask

    echo "Ambiente Flask configurado com sucesso!"
}

main
