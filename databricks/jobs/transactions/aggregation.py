from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg

spark = SparkSession.builder.appName("AggregationJob").getOrCreate()

def aggregate_transactions(source_path, destination_path):
    df = spark.read.parquet(source_path)
    
    # Exemplo de agregação: somar transações por dia
    df_aggregated = df.groupBy("transaction_date").agg(
        sum("transaction_value").alias("daily_sum"),
        avg("transaction_value").alias("daily_avg")
    )
    
    df_aggregated.write.parquet(destination_path)

# Exemplo de agregação
aggregate_transactions("/mnt/databricks/cleaned_data/transactions.parquet", "/mnt/databricks/aggregated_data/daily_transactions.parquet")
