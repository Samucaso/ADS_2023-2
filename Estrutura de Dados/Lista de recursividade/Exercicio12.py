# Faça uma função recursiva que receba um número inteiro positivo N
# e imprima todos os números naturais de 0 até N em ordem crescente.

def imprime_naturais_crescente(n):
    if n == 0:
        return
    imprime_naturais_crescente(n - 1)
    print(n)


imprime_naturais_crescente(5)
