<<<<<<< HEAD
"""
Crie um programa em python que receba um vetor de números reais com 100 elementos.
Escreva uma função recursiva que inverta ordem dos elementos presentes no vetor.
"""


def vet(n):
    if n == 0:
        return 1
    vetor = [] * len(n)
    return vet(vetor[:-1])


print(vet(100))
=======
# Crie um programa em python que receba um vetor de números
# reais com 100 elementos. Escreva uma função recursiva
# que inverta ordem dos elementos presentes no vetor.

def inverter_vetor_recursivo(vetor, inicio, fim):
    if inicio < fim:
        vetor[inicio], vetor[fim] = vetor[fim], vetor[inicio]
        inverter_vetor_recursivo(vetor, inicio + 1, fim - 1)


# vetor com 100 elementos
vet = [float(i) for i in range(1, 101)]

# vetor antes da inversão
print("Vetor antes da inversão:")
print(vet)

# Chamando a função recursiva para inverter o vetor
inverter_vetor_recursivo(vet, 0, len(vet) - 1)

# Imprimindo o vetor após inverter
print("\nVetor após a inversão:")
print(vet)

>>>>>>> fdd40046456c1accdb1554abd4d41aea772cdab0
