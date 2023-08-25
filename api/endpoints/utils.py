from pyspark.sql import SparkSession
from azure.storage.blob import BlobServiceClient

# Inicializando SparkSession
spark = SparkSession.builder.appName("transacoesAPI").getOrCreate()

# Configurações do Azure Data Lake
account_name = 'YOUR_ACCOUNT_NAME'
account_key = 'YOUR_ACCOUNT_KEY'
container_name = 'YOUR_CONTAINER_NAME'
blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)

def save_to_azure(dataframe, blob_name):
    
    ## Salva um DataFrame do PySpark no Azure Data Lake como um arquivo Parquet.
    output_path = "temp_output.parquet"
    dataframe.write.parquet(output_path)
    
    with open(output_path, "rb") as data:
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        blob_client.upload_blob(data, overwrite=True)

def read_from_azure(blob_name):

    ## Lê um arquivo Parquet do Azure Data Lake e retorna como um DataFrame do PySpark.
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    if not blob_client.exists():
        return None
    
    blob_data = blob_client.download_blob()
    df = spark.read.parquet(blob_data.readall())
    return df

def exists_in_azure(blob_name):
    
    ## Verifica se um blob específico existe no Azure Data Lake.
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    return blob_client.exists()

