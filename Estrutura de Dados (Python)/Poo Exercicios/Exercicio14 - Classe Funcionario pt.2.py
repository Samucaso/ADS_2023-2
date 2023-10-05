class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def devolver_nome(self):
        return self.nome

    def devolver_salario(self):
        return self.salario

    # metodo que aumenta o salario do funcionario com base no percentual passado pelo usuario
    def aumentar_salario(self, percentual):
        self.salario += self.salario * (percentual / 100)


funcionario = Funcionario("Samuel", 3500)
print(f"O nome e o salario do funcionario sao respectivamente: "
      f"{funcionario.devolver_nome()} e {funcionario.devolver_salario()}")

funcionario.aumentar_salario(20)
print(f"O novo salario de {funcionario.devolver_nome()} e de: {funcionario.devolver_salario()}")
