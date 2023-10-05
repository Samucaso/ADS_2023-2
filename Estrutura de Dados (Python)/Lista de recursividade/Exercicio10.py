# 10) Escreva uma função recursiva que determine quantas vezes um dígito K ocorre em um número natural N.
# Por exemplo, o dígito 2 ocorre 3 vezes em 762021192.


def digito(k, n, contador):
    if len(n) == 0:
        return contador

    if n[0] == k:
        return digito(k, n[1:], contador=contador + 1)
    else:
        return digito(k, n[1:], contador)


print(digito(str(2), str(54821), 0))
