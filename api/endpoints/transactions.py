from flask import Blueprint, request, jsonify
from pyspark.sql import SparkSession
from azure.storage.blob import BlobServiceClient

# Inicializando SparkSession
spark = SparkSession.builder.appName("transacoesAPI").getOrCreate()

# Configurações do Azure Data Lake
account_name = 'YOUR_ACCOUNT_NAME'
account_key = 'YOUR_ACCOUNT_KEY'
container_name = 'YOUR_CONTAINER_NAME'
blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)

transactions = Blueprint('transactions', __name__)

@transactions.route('/add', methods=['POST'])
def add_transaction():
    try:
        data = request.json
        df = spark.createDataFrame([data])
        output_path = "temp_transaction.parquet"
        df.write.parquet(output_path)
        
        with open(output_path, "rb") as data:
            blob_name = f"transactions/{df.first()['id']}.parquet"  
            blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
            blob_client.upload_blob(data)
        
        return jsonify({"message": "Transaction added successfully!"}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@transactions.route('/update/<transaction_id>', methods=['PUT'])
def update_transaction(transaction_id):
    try:
        # Recuperar os dados enviados na requisição
        data = request.json
        
        # Construir o nome do blob
        blob_name = f"transactions/{transaction_id}.parquet"
        
        # Verificar se o blob existe
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        if not blob_client.exists():
            return jsonify({"error": "Transaction not found"}), 404
        
        # Ler o blob existente para um DataFrame
        blob_data = blob_client.download_blob()
        df_existing = spark.read.parquet(blob_data.readall())
        
        # Atualizar o DataFrame com os novos dados
        for key, value in data.items():
            df_existing = df_existing.withColumn(key, lit(value))
        
        # Salvar o DataFrame atualizado de volta no Azure Data Lake
        output_path = "temp_update_transaction.parquet"
        df_existing.write.parquet(output_path)
        
        with open(output_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
        
        return jsonify({"message": "Transaction updated successfully!"})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@transactions.route('/delete/<transaction_id>', methods=['DELETE'])
def delete_transaction(transaction_id):
    try:
        # Construir o nome do blob
        blob_name = f"transactions/{transaction_id}.parquet"
        
        # Verificar se o blob existe
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        if not blob_client.exists():
            return jsonify({"error": "Transaction not found"}), 404
        
        # Deletar o blob
        blob_client.delete_blob()
        
        return jsonify({"message": "Transaction deleted successfully!"})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@transactions.route('/get/<transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    try:
        # Construir o nome do blob
        blob_name = f"transactions/{transaction_id}.parquet"
        
        # Verificar se o blob existe
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        if not blob_client.exists():
            return jsonify({"error": "Transaction not found"}), 404
        
        # Ler o blob para um DataFrame
        blob_data = blob_client.download_blob()
        df = spark.read.parquet(blob_data.readall())
        
        # Converter o DataFrame para um dicionário e retornar
        transaction_data = df.collect()[0].asDict()
        
        return jsonify(transaction_data)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


