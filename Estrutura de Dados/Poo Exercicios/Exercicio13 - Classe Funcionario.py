# codigo simples que instancia o nome e o salario de um funcionario
# e os printa a seguir
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def devolver_nome(self):
        return self.nome

    def devolver_salario(self):
        return self.salario


funcionario = Funcionario("Samuel", 3500)
print(f"O nome e o salario do funcionario sao respectivamente: "
      f"{funcionario.devolver_nome()} e {funcionario.devolver_salario()}")
