"""
Faça uma função recursiva que permita inverter um número inteiro N. Ex: 123 - 321
"""


def inverte(n):
    if n < 10:
        return n

    ultimo_numero = n % 10
    primeiros_numeros = inverte(n // 10)

    numero_invertido = int(str(ultimo_numero) + str(primeiros_numeros))
    return numero_invertido


print(inverte(456))
