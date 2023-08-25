import pandas as pd

# Dados de transações bancárias
data = {
    'transaction_id': [2001, 2002, 2003, 2004, 2005],
    'account_id': [501, 502, 503, 504, 505],
    'transaction_type': ['deposit', 'withdrawal', 'deposit', 'withdrawal', 'deposit'],
    'amount': [500.00, 200.00, 1000.00, 50.00, 750.00],
    'transaction_date': ['2023-08-01', '2023-08-01', '2023-08-02', '2023-08-02', '2023-08-03'],
    'transaction_status': ['completed', 'completed', 'completed', 'pending', 'completed']
}

# Criar DataFrame
df = pd.DataFrame(data)

# Salvar como arquivo .parquet
df.to_parquet("final_dataset1.parquet")
