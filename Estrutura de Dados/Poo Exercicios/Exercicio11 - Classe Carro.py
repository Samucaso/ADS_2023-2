class Carro:
    def __init__(self, consumo, qtd_combustivel=0):
        self.consumo = consumo
        self.qtd_combustivel = qtd_combustivel
        self.distancia = 0

    # metodo que simula o ato de andar do carro,
    # percorrendo certa distancia e gastando combustivel baseado no consumo definido pelo usuario
    def andar(self, d_percorrida):
        self.distancia += d_percorrida
        self.qtd_combustivel -= d_percorrida / self.consumo
        print(f"Voce dirigiu {d_percorrida} quilometros")

    def obter_gasolina(self):
        if self.qtd_combustivel < 0:
            self.qtd_combustivel = 0

        if self.qtd_combustivel > 0:
            print(f"Quantidade restante de gasolina: {self.qtd_combustivel}")
        else:
            print(f"Seu carro está sem combustivel!")

    def adicionar_gasolina(self):
        while True:
            try:
                add_gasolina = int(input("Quanto de gasolina deseja adicionar? "))
                self.qtd_combustivel += add_gasolina
                print(f"Voce adicionou {add_gasolina} litros de gasolina ao seu carro.")
                break
            except ValueError:
                print("Digite um numero inteiro!")


ferrari = Carro(8)
ferrari.adicionar_gasolina()
ferrari.andar(10)
ferrari.obter_gasolina()
