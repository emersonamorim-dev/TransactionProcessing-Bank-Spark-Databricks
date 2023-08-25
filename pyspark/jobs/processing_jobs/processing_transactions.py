from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

spark = SparkSession.builder.appName("ProcessingTransactionsJob").getOrCreate()

def process_transactions(source_path, destination_path):
    # Ler os dados de transação
    transactions_df = spark.read.parquet(source_path)
    
    # Filtrar transações com status inválido
    valid_transactions_df = transactions_df.filter(col("status") == "valid")
    
    # Adicionar coluna categorizando a transação com base no valor
    categorized_df = valid_transactions_df.withColumn(
        "transaction_category",
        when(col("amount") < 100, "small")
        .when((col("amount") >= 100) & (col("amount") < 1000), "medium")
        .otherwise("large")
    )
    
    # Salvar o DataFrame processado no destino
    categorized_df.write.parquet(destination_path)

# Processamento
process_transactions("/mnt/databricks/processed_data/transactions.parquet", "/mnt/databricks/cleaned_data/transactions.parquet")
