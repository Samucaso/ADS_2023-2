select * from Medicos
select * from Ambulatorio

-- retornar os nomes dos medicos que atendem
-- em ambulatorios com pelo menos 20 leitos de capacidade

select nome, capacidade
from medicos m INNER JOIN Ambulatorio a ON m.nroa=a.nroa
where capacidade > 20
order by nome 

select nome, capacidade
from medicos m,Ambulatorio a
where  m.nroa=a.nroa and
	   capacidade > 20
order by nome 
