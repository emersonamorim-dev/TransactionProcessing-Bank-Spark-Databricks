#!/bin/bash

# Atualizar a lista de pacotes
sudo apt-get update

# Instalar pip para Python3
sudo apt-get install -y python3-pip

# Instalar git 
sudo apt-get install -y git

# Instalar outras dependências do sistema, se necessário
# sudo apt-get install -y 

# Navegar para o diretório do projeto 
cd /path/to/your/project

# Instalar dependências do Python a partir de um arquivo requirements.txt
if [ -f requirements.txt ]; then
    pip3 install -r requirements.txt
fi

echo "Todas as dependências foram instaladas com sucesso!"
