# usei essa biblioteca math pra fazer o calculo da area
import math


class Quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def mudar_valor(self, novo_valor):
        self.tamanho_lado = novo_valor

    def retornar_valor(self):
        return self.tamanho_lado

    def calcular_area(self):
        # usei o comando math.pow da biblioteca math
        return math.pow(self.tamanho_lado, 2)


square = Quadrado(5)
print(f"O tamanho dos lados do quadrado é igual a: {square.retornar_valor()}")
print(f"O valor da area do quadrado é igual a: {square.calcular_area()}")

square.mudar_valor(7)
print(f"O novo tamanho dos lados do quadrado é igual a: {square.retornar_valor()}")
print(f"O novo valor da area do quadrado é igual a: {square.calcular_area()}")
