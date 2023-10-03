# A multiplicação de dois números inteiros pode ser feita através de somas sucessivas.
# Proponha um algoritmo recursivo Multip_Rec(n1,n2)
# que calcule a multiplicação de dois inteiros.

def multip_rec(n1, n2):
    if n2 == 0:
        return 0
    return n1 + multip_rec(n1, n2 - 1)


resultado = multip_rec(5, 3)
print(f'O resultado da multiplicação é: {resultado}')
