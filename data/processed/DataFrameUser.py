import pandas as pd

# Dados de usuários bancários
data = {
    'user_id': [101, 102, 103, 104, 105],
    'name': ['AbeL', 'Bob', 'Charlie', 'Emerson', 'Eva'],
    'account_balance': [1500.00, 1200.00, 1800.00, 1100.00, 1350.00],
    'account_type': ['savings', 'checking', 'savings', 'checking', 'savings'],
    'last_transaction_date': ['2023-07-31', '2023-07-30', '2023-08-01', '2023-07-29', '2023-08-02']
}

# Criar DataFrame
df = pd.DataFrame(data)

# Salvar como arquivo .parquet
df.to_parquet("final_dataset2.parquet")
