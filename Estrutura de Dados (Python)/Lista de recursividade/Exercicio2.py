"""
Faça uma função recursiva que calcule e retorne o N-ésimo termo da sequência Fibonacci.
"""


def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
