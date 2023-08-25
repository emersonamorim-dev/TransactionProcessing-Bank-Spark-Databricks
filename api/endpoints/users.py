from flask import Blueprint, request, jsonify
from pyspark.sql import SparkSession
from azure.storage.blob import BlobServiceClient
import hashlib 

# Inicializando SparkSession
spark = SparkSession.builder.appName("transacoesAPI").getOrCreate()

# Configurações do Azure Data Lake
account_name = 'YOUR_ACCOUNT_NAME'
account_key = 'YOUR_ACCOUNT_KEY'
container_name = 'YOUR_CONTAINER_NAME'
blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)

users = Blueprint('users', __name__)

@users.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        password = data.get('password')
        
        # Hashing da senha antes de armazenar
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        data['password'] = hashed_password
        
        df = spark.createDataFrame([data])
        output_path = "temp_user.parquet"
        df.write.parquet(output_path)
        
        with open(output_path, "rb") as data:
            blob_name = f"users/{df.first()['username']}.parquet"  
            blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
            blob_client.upload_blob(data)
        
        return jsonify({"message": "User registered successfully!"}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@users.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')
        
        # Construir o nome do blob
        blob_name = f"users/{username}.parquet"
        
        # Verificar se o blob existe
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        if not blob_client.exists():
            return jsonify({"error": "User not found"}), 404
        
        # Ler o blob para um DataFrame
        blob_data = blob_client.download_blob()
        df = spark.read.parquet(blob_data.readall())
        
        stored_password = df.collect()[0]['password']
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        if stored_password != hashed_password:
            return jsonify({"error": "Invalid password"}), 401
        
        return jsonify({"message": "Logged in successfully!"})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@users.route('/update/<username>', methods=['PUT'])
def update_user(username):
    # Similar ao endpoint de atualização de transações
    pass

@users.route('/delete/<username>', methods=['DELETE'])
def delete_user(username):
    # Similar ao endpoint de deletar transações
    pass

