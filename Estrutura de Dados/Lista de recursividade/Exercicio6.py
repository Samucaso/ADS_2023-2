"""
Crie um programa em python, que contenha uma função recursiva que receba dois inteiros positivos k e n e calcule k^n.
Utilize apenas multiplicações.
O programa principal deve solicitar ao usuário os valores de k e n e imprimir o resultado da chamada da função.
"""


def calculo(k, n):
    if n == 0:
        return 1  # Qualquer número elevado a 0 é 1
    elif n > 0:
        return k * calculo(k, n - 1)  # k^n = k * k^(n-1)


valork = float(input("Digite o valor de k: "))
valorn = int(input("Digite o valor de n: "))

print(calculo(valork, valorn))
