#!/bin/bash

# Carregar configurações
AZURE_CONFIG="./config/azure_config.json"

RESOURCE_GROUP=$(jq -r '.resource_group' $AZURE_CONFIG)
APP_NAME=$(jq -r '.app_name' $AZURE_CONFIG)
STORAGE_ACCOUNT=$(jq -r '.storage_account' $AZURE_CONFIG)

# Implantar aplicação
az webapp up --name $APP_NAME --resource-group $RESOURCE_GROUP

# Configurar variáveis de ambiente (exemplo)
az webapp config appsettings set --resource-group $RESOURCE_GROUP --name $APP_NAME --settings APP_ENV="Production"

# Habilitar logs de aplicativo
az webapp log config --name $APP_NAME --resource-group $RESOURCE_GROUP --application-logging true --detailed-error-messages true --failed-request-tracing true --web-server-logging filesystem

# Se você estiver usando um banco de dados, você pode adicionar comandos para configurar a string de conexão:
az webapp config connection-string set --resource-group $RESOURCE_GROUP --name $APP_NAME --settings MyDbConnection="...your_connection_string_here..."

# Se você tiver um contêiner Docker para implantar:
az webapp config container set --name $APP_NAME --resource-group $RESOURCE_GROUP --docker-custom-image-name "your_docker_image_name" --docker-registry-server-url "your_docker_registry_url"

echo "Implantação concluída!"
