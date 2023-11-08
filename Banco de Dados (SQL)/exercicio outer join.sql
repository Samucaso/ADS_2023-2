-- 1. Listar TODOS os m�dicos e suas respectivas consultas, incluindo aqueles SEM consulta marcada
select nome, data, hora
from Medicos m full outer join Consultas c 
on m.codm = c.codm

-- 2. Listar TODOS os Pacientes e suas respectivas consultas, incluindo aqueles SEM consulta marcada
select nome, nome, data, hora
from Pacientes p full outer join Consultas c
on p.codp = c.codp

-- 3. Listar TODOS os m�dicos e TODOS os paciente e suas respectivas consultas, incluindo aqueles SEM consulta marcada
select m.nome as 'medicos', p.nome as pacientes, data, hora
from Pacientes p left outer join Consultas c
on p.codp = c.codp 
left outer join Medicos m 
on m.codm = c.codm

-- 4. Listar TODOS os m�dicos e os ambulat�rios onde atendem, inclusive aqueles que n�o tem ambulat�rio associado 
select m.nome, a.nroa as 'codigo do ambulatorio'
from Medicos m left outer join Ambulatorio a 
on m.nroa = a.nroa

-- 5. Listar Todos os ambulat�rios, inclusive aqueles vazios, isto �, que n�o tem m�dicos associados 
select a.nroa as 'codigo do ambulatorio', m.nome
from Ambulatorio a left outer join Medicos m
on a.nroa = m.nroa