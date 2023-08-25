from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ProcessingJob").getOrCreate()

def process_transactions(source_path, destination_path):
    df = spark.read.parquet(source_path)
    
    # Exemplo de processamento: remover transações com valores negativos
    df_processed = df.filter(df["transaction_value"] > 0)
    
    df_processed.write.parquet(destination_path)

# Exemplo de processamento
process_transactions("/mnt/databricks/processed_data/transactions.parquet", "/mnt/databricks/cleaned_data/transactions.parquet")
