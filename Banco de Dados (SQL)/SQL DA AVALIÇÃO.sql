-- Exercicio 3
CREATE TABLE CONSUMIDORES (
    CPF CHAR(11) PRIMARY KEY,
    nome VARCHAR(80) NOT NULL,
    Cidade VARCHAR(15),
    Estado CHAR(2)
);

CREATE TABLE REVENDEDORAS (
    CNPJ CHAR(14) PRIMARY KEY,
    nome VARCHAR(80),
    Cidade VARCHAR(15),
    Estado CHAR(2)
);

CREATE TABLE NEGOCIOS (
    CPF CHAR(11),
    CNPJ CHAR(14),
    Automovel VARCHAR(15),
    DataCompra DATE,
    Preco NUMERIC,
    PRIMARY KEY (CPF, CNPJ),
    FOREIGN KEY (CPF) REFERENCES CONSUMIDORES(CPF),
    FOREIGN KEY (CNPJ) REFERENCES REVENDEDORAS(CNPJ)
);

-- Exercicio 4
ALTER TABLE CONSUMIDORES
ADD idade INT CHECK (idade < 100)


-- Exercicio 5
ALTER TABLE CONSUMIDORES
DROP COLUMN idade;


-- Exercicio 6
DROP TABLE NEGOCIOS;

-- Exercicio 7
INSERT INTO CONSUMIDORES (CPF, nome, Cidade, Estado)
VALUES ('12345678901', 'Roberto', 'Rio de Janeiro', 'RJ'),
       ('11145678901', 'Ana', 'Niterói', 'RJ'),
       ('13345678901', 'Ricardo', 'Rio de Janeiro', 'RJ'),
       ('12245678901', 'Rachel', 'Niterói', 'RJ'),
       ('16645678901', 'Ninho', 'Niterói', 'RJ');

INSERT INTO REVENDEDORAS (CNPJ, nome, Cidade, Estado)
VALUES ('12345678901234', 'Loja BobAuto', 'Rio de Janeiro', 'RJ'),
       ('44445678904444', 'Loja SenacAuto', 'Niterói', 'RJ');

INSERT INTO NEGOCIOS (CPF, CNPJ, Automovel, DataCompra, Preco)
VALUES ('12345678901', '12345678901234', 'Honda FIT', '2023-01-10', 80000),
       ('13345678901', '12345678901234', 'Honda CIVIC', '2023-03-10', 100000),
       ('12245678901', '44445678904444', 'Honda CRV', '2023-04-10', 130000),
       ('16645678901', '44445678904444', 'Toyota Corolla', '2023-01-15', 85000);

--Exercicio 8
UPDATE NEGOCIOS
SET Preco = 90000
WHERE CPF = '12345678901';

--Exercicio 9
DELETE FROM CONSUMIDORES
WHERE CPF = '11145678901'

