class BombaCombustivel:
    def __init__(self, tipo_combustivel=None, valor_litro=None, qtd_combustivel=0):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.qtd_combustivel = qtd_combustivel

    # metodo que abastece o carro de acordo com um valor dado peo usuario
    def abastecer_por_valor(self):
        valor = int(input("Quanto (R$) você quer abastecer? "))
        self.__alterar_qtd_combustivel(valor / self.valor_litro)

    # metodo que informa o valor a ser pago de acordo com a qtd de litros que o usuario deseja abastecer
    def abastecer_por_litro(self):
        litros = int(input("Com quantos litros você deseja que seu carro seja abastecido? "))
        print(f"O valor a ser pago é de {litros * self.valor_litro:.2f}")

    # metodo que altera o valor do litro de determinado combustivel
    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor
        if self.tipo_combustivel == "GNV":
            print(f"O novo valor do metro cúbico de {self.tipo_combustivel} é {self.valor_litro}")
        else:
            print(f"O novo valor do litro de {self.tipo_combustivel} é {self.valor_litro}")

    def alterar_combustivel(self):
        while True:
            try:
                combustivel = int(input("Escolha o combustivel que deseja: (1 = Gasolina, 2 = GNV, 3 = Alcool) "))
                if combustivel in [1, 2, 3]:
                    if combustivel == 1:
                        self.tipo_combustivel = "Gasolina"
                        self.valor_litro = 5.52
                        break
                    elif combustivel == 2:
                        self.tipo_combustivel = "GNV"
                        self.valor_litro = 4.70
                        break
                    else:
                        self.tipo_combustivel = "Etanol"
                        self.valor_litro = 4.39
                        break
                else:
                    combustivel = int(input("Digite um dos números válidos! "))
            except ValueError:
                print("Voce deve digitar um dos três números! ")

    def __alterar_qtd_combustivel(self, nova_qtd_combustivel):
        self.qtd_combustivel += nova_qtd_combustivel
        print(f"A quantidade de combustível no seu carro é de: {self.qtd_combustivel:.1f} litros")


carro = BombaCombustivel()
carro.alterar_combustivel()
carro.abastecer_por_litro()
carro.abastecer_por_valor()
