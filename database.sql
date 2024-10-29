CREATE DATABASE aula

USE aula

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    dni VARCHAR(20) NOT NULL,
    email VARCHAR(255) NOT NULL,
    nacimiento DATE NOT NULL,
    rol ENUM('maestro', 'alumno') NOT NULL
);
