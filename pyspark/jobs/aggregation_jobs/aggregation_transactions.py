from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, date_format

spark = SparkSession.builder.appName("AggregationTransactionsJob").getOrCreate()

def aggregate_transactions(source_path, destination_path):
    # Ler os dados de transação
    transactions_df = spark.read.parquet(source_path)

    # Agregar por data e contar o número de transações
    aggregated_df = transactions_df.groupBy(date_format(col("transaction_date"), "yyyy-MM-dd").alias("date")).agg(
        count("*").alias("number_of_transactions")
    ).sort("date")
    
    # Salvar o DataFrame agregado no destino
    aggregated_df.write.parquet(destination_path)

# Agregação
aggregate_transactions("/mnt/databricks/cleaned_data/transactions.parquet", "/mnt/databricks/aggregated_data/daily_transactions.parquet")
