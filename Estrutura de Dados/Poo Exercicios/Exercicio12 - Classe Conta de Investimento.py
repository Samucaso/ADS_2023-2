class ContaInvestimento:
    def __init__(self,saldo_inicial, taxa_juros):
        self.saldo_inicial = saldo_inicial
        self.taxa_juros = taxa_juros

    def adicione_juros(self):
        self.saldo_inicial += self.saldo_inicial * (self.taxa_juros / 100)


conta = ContaInvestimento(1000, 10)

for i in range(5):
    conta.adicione_juros()

print(f"O saldo com juros e de: {conta.saldo_inicial}")
