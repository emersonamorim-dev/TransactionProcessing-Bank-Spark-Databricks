#!/bin/bash

# Carregar configurações
AZURE_CONFIG="./config/azure_config.json"

RESOURCE_GROUP=$(jq -r '.resource_group' $AZURE_CONFIG)
STORAGE_ACCOUNT=$(jq -r '.storage_account' $AZURE_CONFIG)
APP_NAME=$(jq -r '.app_name' $AZURE_CONFIG)

# Desassociar e excluir IPs públicos (se você tiver usado algum)
IP_NAMES=$(az network public-ip list --resource-group $RESOURCE_GROUP --query "[].name" --output tsv)
for IP_NAME in $IP_NAMES; do
    az network public-ip delete --resource-group $RESOURCE_GROUP --name $IP_NAME
done

# Excluir discos não associados
DISK_IDS=$(az disk list --resource-group $RESOURCE_GROUP --query "[?diskState=='Unattached'].id" --output tsv)
for DISK_ID in $DISK_IDS; do
    az disk delete --ids $DISK_ID --yes --no-wait
done

# Excluir grupo de recursos
az group delete --name $RESOURCE_GROUP --yes --no-wait

echo "Limpeza concluída!"
