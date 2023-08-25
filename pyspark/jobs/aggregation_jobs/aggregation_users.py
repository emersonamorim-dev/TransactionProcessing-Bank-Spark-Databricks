from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, when

spark = SparkSession.builder.appName("AggregationUsersJob").getOrCreate()

def aggregate_users(source_path, destination_path_prefix):
    # Ler os dados do usuário
    users_df = spark.read.parquet(source_path)
    
    # Distribuição de usuários por gênero
    gender_distribution = users_df.groupBy("gender").agg(
        count("*").alias("number_of_users")
    )
    gender_distribution.write.parquet(destination_path_prefix + "/gender_distribution.parquet")
    
    # Distribuição de usuários por faixa etária
    age_bins = [
        (0, 18, "0-18"),
        (19, 30, "19-30"),
        (31, 50, "31-50"),
        (51, 100, "51-100")
    ]
    
    age_distribution = users_df.withColumn(
        "age_bin",
        next((when((col("age") >= start) & (col("age") <= end), label) for start, end, label in age_bins), "other")
    ).groupBy("age_bin").agg(
        count("*").alias("number_of_users")
    )
    age_distribution.write.parquet(destination_path_prefix + "/age_distribution.parquet")
    
    # Contagem de usuários por país
    country_distribution = users_df.groupBy("country").agg(
        count("*").alias("number_of_users")
    )
    country_distribution.write.parquet(destination_path_prefix + "/country_distribution.parquet")

# Agregação
aggregate_users("/mnt/databricks/processed_data/users.parquet", "/mnt/databricks/aggregated_data/users")
