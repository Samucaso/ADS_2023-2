-- 1
select * from medicos

-- 2 
select nome, especialidade
from medicos

-- 3 
select nome, idade 
from medicos
where idade > 55

-- 4 
select nome, idade 
from medicos
where especialidade = 'Ortopedia'
and idade > 55 

-- 5
select distinct especialidade
from medicos