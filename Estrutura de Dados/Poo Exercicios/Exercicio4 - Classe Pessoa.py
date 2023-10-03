class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    # envelhece a pessoa baseado no quantidade de anos passada,
    # e aumenta sua altura em 0.5 centimetros a cada ano passado enquanto a pessoa tiver menos de 21 anos
    def envelhecer(self, anos):
        self.idade = self.idade + anos
        if self.idade < 21:
            self.altura = self.altura + (anos * 0.5)

    def engordar(self, quilos):
        self.peso = self.peso + quilos

    def emagrecer(self, quilos):
        self.peso = self.peso - quilos

    def crescer(self, centim):
        self.altura = self.altura + centim


# usando meus dados como exemplo
pessoa = Pessoa("Samuel", 18, 90, 196)

print(f"O nome da pessoa é: {pessoa.nome}")
print(f"{pessoa.nome} tem {pessoa.idade} anos")
print(f"Pesa {pessoa.peso} quilos")
print(f"E tem {pessoa.altura} cm de altura")

ano = 2
pessoa.envelhecer(ano)
pessoa.engordar(5)
print(f"{ano} anos depois, {pessoa.nome} tem {pessoa.idade} anos")
print(f"Pesa {pessoa.peso} quilos, e tem {pessoa.altura} cm de altura")

ano = 5
pessoa.envelhecer(ano)
pessoa.emagrecer(2)
pessoa.crescer(3)
print(f"Mais {ano} anos depois, {pessoa.nome} agora tem {pessoa.idade} anos")
print(f"Pesa {pessoa.peso} quilos, e tem {pessoa.altura} cm de altura")