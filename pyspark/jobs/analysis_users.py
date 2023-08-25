from pyspark.sql import SparkSession
from pyspark.sql.functions import count, when

spark = SparkSession.builder.appName("UserAnalysisJob").getOrCreate()

def analyze_users(source_path, destination_path):
    # Ler os dados do usuário
    users_df = spark.read.parquet(source_path)

    
    # Agregar por sexo e contar o número de usuários
    gender_distribution = users_df.groupBy("gender").agg(
        count("*").alias("number_of_users")
    )
    
    # Criar faixas etárias e contar o número de usuários em cada faixa
    age_bins = [
        (0, 18, "0-18"),
        (19, 30, "19-30"),
        (31, 50, "31-50"),
        (51, 100, "51-100")
    ]
    
    age_distribution = users_df.select("age").withColumn(
        "age_bin",
        next((when((col("age") >= start) & (col("age") <= end), label) for start, end, label in age_bins), "other")
    ).groupBy("age_bin").agg(
        count("*").alias("number_of_users")
    )
    
    # Juntar os resultados e salvar no destino
    result_df = gender_distribution.union(age_distribution)
    result_df.write.parquet(destination_path)

# Análise
analyze_users("/mnt/databricks/processed_data/users.parquet", "/mnt/databricks/analysis_data/user_categories.parquet")
