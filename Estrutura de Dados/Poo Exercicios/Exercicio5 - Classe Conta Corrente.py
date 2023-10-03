class ContaCorrente:
    # saldo iniciado como 0 para simular uma conta vazia
    def __init__(self, num_conta, nome_correntista, saldo=0):
        self.num_conta = num_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, add_saldo):
        self.saldo += add_saldo

    def saque(self, retornar_saldo):
        self.saldo -= retornar_saldo


conta = ContaCorrente(8745, "Diogo")

print(f"O nome do correntista é: {conta.nome_correntista}")
conta.alterar_nome("Diego")
print(f"O novo nome do correntista é: {conta.nome_correntista}")

print(f"Seu saldo atual é de: R$ {conta.saldo}")
dep = float(input("Quanto você quer depositar?\n"))
conta.deposito(dep)
print(f"Seu novo saldo é: R$ {conta.saldo}")

saque = float(input("Quanto você deseja sacar?\n"))

# loop feito para fazer com que o usuário não possa sacar mais do que ele possui
while saque > conta.saldo:
    print("Saldo insuficiente!")
    print(f"No momento você possui R$ {conta.saldo}")
    saque = float(input("Quanto você deseja sacar?\n"))

conta.saque(saque)
print(f"Saque realizado com sucesso!")
print(f"Seu novo saldo é de: R$ {conta.saldo}")
