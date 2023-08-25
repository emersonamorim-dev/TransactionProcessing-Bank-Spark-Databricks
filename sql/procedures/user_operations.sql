-- Procedure para adicionar um novo usuário
DELIMITER //
CREATE PROCEDURE AddUser(IN username VARCHAR(255), IN email VARCHAR(255))
BEGIN
    INSERT INTO users (username, email) VALUES (username, email);
END //
DELIMITER ;

-- Procedure para deletar um usuário
DELIMITER //
CREATE PROCEDURE DeleteUser(IN userId INT)
BEGIN
    DELETE FROM users WHERE id = userId;
END //
DELIMITER ;
