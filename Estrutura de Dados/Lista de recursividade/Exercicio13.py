# Faça uma função recursiva que receba um número inteiro positivo N
# e imprima todos os números naturais de 0 até N em ordem decrescente.

def imprime_naturais_decrescente(n):
    if n == 0:
        return
    print(n)
    imprime_naturais_decrescente(n - 1)


imprime_naturais_decrescente(5)
