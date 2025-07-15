CREATE DATABASE IF NOT EXISTS `api_seguranca`;
USE `api_seguranca`;
CREATE TABLE IF NOT EXISTS `usuarios` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `nome` VARCHAR(100) NOT NULL,
    `idade`  INT NOT NULL,
    `cpf` VARCHAR(11) NOT NULL UNIQUE,
    `telefone` VARCHAR(15) NOT NULL,
    `email` VARCHAR(100) NOT NULL UNIQUE,
    `senha` VARCHAR(255) NOT NULL
);