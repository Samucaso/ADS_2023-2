# Crie uma função recursiva que receba um número inteiro positivo N
# e calcule o produtório dos números de 1 a N.

def produtorio(n):
    # Caso base:
    if n == 0 or n == 1:
        return 1
    else:
        # Chamada recursiva para calcular o produtório de (n-1)
        return n * produtorio(n - 1)


numero = 5
resultado = produtorio(numero)
print(f'O produtório de 1 a {numero} é: {resultado}')
