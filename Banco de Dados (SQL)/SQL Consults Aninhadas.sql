-- Quantos médicos existem no hosital?
SELECT COUNT(*) AS 'Quantidade Medicos' FROM MEDICOS

-- Qual a idade do médicos mais velho?
SELECT MAX(idade) as MaiorIdade from Medicos

-- Qual a idade do médicos mais novo?
SELECT MIN(idade) as MenorIdade from Medicos

-- Qual a idade do oftalmo mais velho?
SELECT MAX(idade) as MaiorIdadeOftalmo from Medicos
where especialidade ='oftalmologia'

-- Qual o nome do médico mais velho?
SELECT nome, idade
from Medicos
where idade = (SELECT MAX(idade) as MaiorIdade FROM Medicos)

-- Qual a idade do pediatra mais velho?
SELECT nome, idade, especialidade
from Medicos
where idade = (SELECT MAX(idade) as MaiorIdade FROM Medicos
where especialidade='Pediatria') and especialidade='Pediatria'