from pyspark.sql import SparkSession
from azure.storage.blob import BlobServiceClient

# Inicializando SparkSession
spark = SparkSession.builder.appName("UserIngestionJob").getOrCreate()

# Configurações do Azure Data Lake
account_name = 'YOUR_ACCOUNT_NAME'
account_key = 'YOUR_ACCOUNT_KEY'
container_name = 'YOUR_CONTAINER_NAME'
blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)

def ingest_users_from_azure(blob_name, destination_path):
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    data = blob_client.download_blob().readall()
    df = spark.read.csv(data)
    df.write.parquet(destination_path)

# Exemplo de ingestão
ingest_users_from_azure("raw_data/users.csv", "/mnt/databricks/processed_data/users.parquet")
