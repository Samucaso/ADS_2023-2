"""
Faça uma função recursiva que permita somar os elementos de um vetor de inteiros.
"""


def soma_vetor(v):
    index = len(v)-1

    # caso base
    if index < 0:
        return 0

    # recursividade
    return v[index] + soma_vetor(v[:index])


vetor = [1, 2, 3]
print(soma_vetor(vetor))
