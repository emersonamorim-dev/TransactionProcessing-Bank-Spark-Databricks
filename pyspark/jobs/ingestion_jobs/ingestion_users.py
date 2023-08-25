from pyspark.sql import SparkSession
from azure.storage.blob import BlobServiceClient

spark = SparkSession.builder.appName("IngestionUsersJob").getOrCreate()

# Configurações do Azure Blob Storage
ACCOUNT_NAME = 'YOUR_AZURE_STORAGE_ACCOUNT_NAME'
ACCOUNT_KEY = 'YOUR_AZURE_STORAGE_ACCOUNT_KEY'
CONTAINER_NAME = 'YOUR_CONTAINER_NAME'
BLOB_SERVICE_CLIENT = BlobServiceClient(account_url=f"https://{ACCOUNT_NAME}.blob.core.windows.net", credential=ACCOUNT_KEY)

def ingest_from_azure(blob_name, destination_path):
    # Criar um blob client usando o nome do blob e o nome do container
    blob_client = BLOB_SERVICE_CLIENT.get_blob_client(container=CONTAINER_NAME, blob=blob_name)
    
    # Baixar o blob para um stream
    blob_data = blob_client.download_blob()
    
    # Ler os dados do stream usando Spark e salvar no local desejado
    df = spark.read.option("header", "true").csv(blob_data.content_as_text())
    df.write.parquet(destination_path)

# Ingestão
ingest_from_azure("raw_data/users.csv", "/mnt/databricks/processed_data/users.parquet")
