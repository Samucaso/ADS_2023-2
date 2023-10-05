class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    # defini a barriga do macaco como uma lista e usei append para adicionar os alimentos nela
    def comer(self):
        alimento = input(f"Como deseja alimentar {self.nome}? ")
        self.bucho.append(alimento)

    def ver_bucho(self):
        print(f"Dentro do bucho do {self.nome} tem: {self.bucho}")

    # ao digerir, apenas zerei o numero de alimentos no bucho, associando o atributo a uma lista vaia
    def digerir(self):
        print(f"{self.nome} digeriu a comida")
        self.bucho = []


nome1 = input("Qual o nome do primeiro macaco? ")
macaco1 = Macaco(nome1)

nome2 = input("Qual o nome do segundo macaco? ")
macaco2 = Macaco(nome2)

# for feita para executar o metodo comer 3 vezes, conforme pedido no enunciado
for i in range(3):
    macaco1.comer()
    macaco1.ver_bucho()
macaco1.digerir()
macaco1.ver_bucho()

for i in range(3):
    macaco2.comer()
    macaco2.ver_bucho()
macaco2.digerir()
macaco2.ver_bucho()
