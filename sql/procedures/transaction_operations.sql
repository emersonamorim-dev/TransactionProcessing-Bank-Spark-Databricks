-- Procedure para adicionar uma nova transação
DELIMITER //
CREATE PROCEDURE AddTransaction(IN userId INT, IN amount DECIMAL(10,2))
BEGIN
    INSERT INTO transactions (user_id, amount) VALUES (userId, amount);
END //
DELIMITER ;

-- Procedure para atualizar uma transação
DELIMITER //
CREATE PROCEDURE UpdateTransaction(IN transactionId INT, IN amount DECIMAL(10,2))
BEGIN
    UPDATE transactions SET amount = amount WHERE id = transactionId;
END //
DELIMITER ;
