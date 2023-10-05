class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    # novo valor base e novo valor altura
    def mudar_valor(self, novo_valorb, novo_valora):
        self.base = novo_valorb
        self.altura = novo_valora

    def retornar_valores(self):
        return self.base, self.altura

    # calculo da area do retangulo: base x altura
    def calcular_area(self):
        return self.base * self.altura

    # perimetro do retangulo é a soma dos lados
    def calcular_perimetro(self):
        return self.base * 2 + self.altura * 2


base = int(input("Digite a base do local: "))
altura = int(input("Digite a altura do local: "))
local = Retangulo(base, altura)
print(f"Os valores de base e altura do local são respectivamente: {local.retornar_valores()}")

baseN = int(input("Digite um novo valor para a base do local: "))
alturaN = int(input("Digite um novo valor para a altura do local: "))
local.mudar_valor(baseN, alturaN)
print(f"Os novos valores de base e altura do local são respectivamente: {local.retornar_valores()}")

area = local.calcular_area()
perimetro = local.calcular_perimetro()

print(f"A area e o perimetro desse local são respectivamente {area} e {perimetro}")

tamanho_pisos = int(input("Digite o tamanho dos pisos: "))
tamanho_rodapes = int(input("Digite o tamanho dos rodapes: "))

quant_pisos = area / tamanho_pisos
quant_rodapes = 2 * (base + altura) / tamanho_rodapes

print(f"A quantidade de pisos é igual a: {quant_pisos:.2f}")
print(f"A quantidade de rodapes é igual a: {quant_rodapes:.2f}")
