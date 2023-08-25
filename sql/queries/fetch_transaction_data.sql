-- Query para buscar todas as transações de um usuário específico
SELECT * FROM transactions WHERE user_id = ?;

-- Query para buscar uma transação específica por ID
SELECT * FROM transactions WHERE id = ?;
