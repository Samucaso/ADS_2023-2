# Faça uma função recursiva que receba um número inteiro positivo par N
# e imprima todos os números pares de 0 até N em ordem decrescente.

def imprime_pares_decrescente(n):
    if n == 0:
        return
    if n % 2 == 0:
        print(n)
        imprime_pares_decrescente(n - 1)


imprime_pares_decrescente(10)
