from flask import Flask, request, jsonify
from pyspark.sql import SparkSession
from azure.storage.blob import BlobServiceClient

app = Flask(__name__)

# Inicializando SparkSession
spark = SparkSession.builder.appName("transacoesAPI").getOrCreate()

# Configurações do Azure Data Lake
account_name = 'YOUR_ACCOUNT_NAME'
account_key = 'YOUR_ACCOUNT_KEY'
container_name = 'YOUR_CONTAINER_NAME'
blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)

@app.route('/batch', methods=['POST'])
def process_batch():
    try:
        # Supondo que os dados são enviados como um arquivo CSV
        file = request.files['file']
        
        # Lendo o arquivo usando PySpark
        df = spark.read.csv(file.stream)
        
        # Processamento de dados: remover linhas com valores faltantes como exemplo
        processed_df = df.dropna()
        
        # Salvar no Azure Data Lake
        output_path = "temp_output.parquet"
        processed_df.write.parquet(output_path)
        
        with open(output_path, "rb") as data:
            blob_client = blob_service_client.get_blob_client(container=container_name, blob="batch_data.parquet")
            blob_client.upload_blob(data)
        
        return jsonify({"message": "Batch processado com sucesso!"})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/stream', methods=['POST'])
def process_stream():
    try:
        # Supondo que os dados são enviados como JSON
        data = request.json
        
        # Convertendo JSON para DataFrame do PySpark
        df = spark.createDataFrame([data])
        
        # Processamento de dados: remover linhas com valores faltantes como exemplo
        processed_df = df.dropna()
        
        # Salvar no Azure Data Lake
        output_path = "temp_stream_output.parquet"
        processed_df.write.parquet(output_path)
        
        with open(output_path, "rb") as data:
            blob_client = blob_service_client.get_blob_client(container=container_name, blob="stream_data.parquet")
            blob_client.upload_blob(data)
        
        return jsonify({"message": "Stream processado com sucesso!"})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
