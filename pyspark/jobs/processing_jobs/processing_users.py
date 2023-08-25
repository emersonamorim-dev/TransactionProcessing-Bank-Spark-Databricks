from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, upper, length

spark = SparkSession.builder.appName("ProcessingUsersJob").getOrCreate()

def process_users(source_path, destination_path):
    # Ler os dados do usuário
    users_df = spark.read.parquet(source_path)
    
    # Filtrar usuários com idade inválida
    valid_age_df = users_df.filter((col("age") >= 0) & (col("age") <= 120))
    
    # Padronizar os nomes dos usuários
    standardized_names_df = valid_age_df.withColumn("name", upper(col("name")))
    
    # Verificar e remover e-mails inválidos
    valid_email_df = standardized_names_df.filter(col("email").contains("@") & (length(col("email")) > 5))
    
    # Adicionar uma coluna categorizando o usuário com base na idade
    categorized_df = valid_email_df.withColumn(
        "age_category",
        when(col("age") < 18, "minor")
        .when((col("age") >= 18) & (col("age") < 60), "adult")
        .otherwise("senior")
    )
    
    # Salvar o DataFrame processado no destino
    categorized_df.write.parquet(destination_path)

# Processamento
process_users("/mnt/databricks/raw_data/users.parquet", "/mnt/databricks/processed_data/users.parquet")
