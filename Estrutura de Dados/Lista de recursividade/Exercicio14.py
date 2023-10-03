# Faça uma função recursiva que receba um número inteiro positivo par N
# e imprima todos os números pares de 0 até N em ordem crescente.

def imprime_pares_crescente(n):
    if n == 0:
        return
    if n % 2 == 0:
        imprime_pares_crescente(n - 1)
        print(n)


imprime_pares_crescente(10)
