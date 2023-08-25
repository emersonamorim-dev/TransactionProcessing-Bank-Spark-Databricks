#!/bin/bash

# Carregar configurações e credenciais
AZURE_CONFIG="./config/azure_config.json"
AZURE_CREDS="./config/azure_credentials.json"

RESOURCE_GROUP=$(jq -r '.resource_group' $AZURE_CONFIG)
LOCATION=$(jq -r '.location' $AZURE_CONFIG)
STORAGE_ACCOUNT=$(jq -r '.storage_account' $AZURE_CONFIG)
APP_SERVICE_PLAN=$(jq -r '.app_service_plan' $AZURE_CONFIG)
APP_NAME=$(jq -r '.app_name' $AZURE_CONFIG)

# Criar grupo de recursos
az group create --name $RESOURCE_GROUP --location $LOCATION

# Criar conta de armazenamento
az storage account create --name $STORAGE_ACCOUNT --resource-group $RESOURCE_GROUP --location $LOCATION --sku Standard_LRS

# Criar plano de serviço de aplicativo
az appservice plan create --name $APP_SERVICE_PLAN --resource-group $RESOURCE_GROUP --location $LOCATION --sku B1 --is-linux

# Criar serviço de aplicativo
az webapp create --resource-group $RESOURCE_GROUP --plan $APP_SERVICE_PLAN --name $APP_NAME --runtime "PYTHON|3.7" --deployment-local-git

# Se você estiver usando um banco de dados, como CosmosDB ou SQL Database, você também pode adicionar comandos para configurar esses recursos.

echo "Configuração concluída!"
