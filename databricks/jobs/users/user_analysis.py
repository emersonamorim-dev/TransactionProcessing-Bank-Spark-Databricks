from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, avg

spark = SparkSession.builder.appName("UserAnalysisJob").getOrCreate()

def analyze_users(source_path, destination_path):
    df = spark.read.parquet(source_path)
    
    # Exemplo de análise: contar usuários por categoria
    df_analysis = df.groupBy("user_category").agg(
        count("user_id").alias("number_of_users"),
        avg("user_purchase_value").alias("avg_purchase_value")
    )
    
    df_analysis.write.parquet(destination_path)

# Exemplo de análise
analyze_users("/mnt/databricks/processed_data/users.parquet", "/mnt/databricks/analysis_data/user_categories.parquet")
