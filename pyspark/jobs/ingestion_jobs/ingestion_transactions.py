from pyspark.sql import SparkSession
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

spark = SparkSession.builder.appName("IngestionTransactionsJob").getOrCreate()

# Configurações do Azure Blob Storage
account_name = 'YOUR_AZURE_STORAGE_ACCOUNT_NAME'
account_key = 'YOUR_AZURE_STORAGE_ACCOUNT_KEY'
container_name = 'YOUR_CONTAINER_NAME'
blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)

def ingest_from_azure(blob_name, destination_path):
    # Criar um blob client usando o nome do blob e o nome do container
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    
    # Baixar o blob para um stream
    blob_data = blob_client.download_blob()
    
    # Ler os dados do stream usando Spark e salvar no local desejado
    df = spark.read.option("header", "true").csv(blob_data.content_as_text())
    df.write.parquet(destination_path)

# Ingestão
ingest_from_azure("raw_data/transactions.csv", "/mnt/databricks/processed_data/transactions.parquet")


