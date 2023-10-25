select * from medicos
select * from Ambulatorio

-- Listar o nome do medico, o andar e n�mero de ambulat�rio
-- onde presta atendimento, ordenado por andar

select m.nome, andar, a.nroa
from medicos m INNER JOIN Ambulatorio a ON m.nroa = a.nroa
order by andar

-- Buscar o nome dos pacientes que t�m consulta marcada,
-- com a respectiva data e hora, ordenado por data/hora
select p.nome, data, hora
from Pacientes p INNER JOIN Consultas c ON p.codp = c.codp 
order by data, hora

-- Buscar o nome do m�dico, o nome do paciente e a data&hora
-- da consulta ordenado por data/hora
select m.nome, p.nome, data, hora
from Medicos m INNER JOIN Consultas c ON c.codm = m.codm
	 INNER JOIN Pacientes p ON p.codp = c.codp
order by data, hora

-- Buscar, para as consultas marcadas para o per�odo da manh�
-- (7hs-12hs) do dia 07/10/2015, o nome do m�dico,
-- o nome do paciente e a data&hora da consulta
select m.nome, p.nome, data, hora
from Medicos m INNER JOIN Consultas c ON m.codm = m.codm
	 INNER JOIN Pacientes p ON p.codp = c.codp
where hora >= '7:00' and hora <= '12:00' and data = '07/10/2015' 
order by data, hora

-- Buscar, para as consultas marcadas para o per�odo da manh� (7hs-12hs)
-- do dia 07/10/2015, o nome do m�dico, o nome do paciente e a data&hora
-- da consulta e o ambulat�rio e respectivo andar onde ser� realizada a consulta
select m.nome, p.nome, data, hora, a.nroa, andar
from Medicos m INNER JOIN Consultas c ON m.codm = m.codm
	 INNER JOIN Pacientes p ON p.codp = c.codp
	 INNER JOIN Ambulatorio a ON m.nroa = a.nroa 
where hora >= '7:00' and hora <= '12:00' and data = '07/10/2015' 
order by data, hora