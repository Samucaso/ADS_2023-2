"""
4. Escreva uma função que inverta a ordem dos elementos da fila.  Por exemplo:

[1] [4] [5] [2] → [2] [5] [4] [1]
"""

class Nodo:
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return f"{self.dado} -> {self.proximo}"


class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __repr__(self):
        return "[" + str(self.primeiro) + "]"

    def push(self, novo_dado):
        novo_nodo = Nodo(novo_dado)

        if self.primeiro is None:
            self.primeiro = novo_nodo
            self.ultimo = novo_nodo
        else:
            self.ultimo.proximo = novo_nodo
            self.ultimo = novo_nodo

    def pop(self):
        assert self.primeiro is not None, "Impossível remover elemento de fila vazia"

        self.primeiro = self.primeiro.proximo

        if self.primeiro is None:
            self.ultimo = None

    def imprimir(self):
        corrente = self.primeiro

        while corrente is not None:
            print(corrente.dado, end=" ")
            corrente = corrente.proximo

    def inverter(self):
        pilha = []
        corrente = self.primeiro

        while corrente is not None:
            pilha.append(corrente.dado)
            corrente = corrente.proximo

        self.primeiro = None
        self.ultimo = None

        while pilha:
            self.push(pilha.pop())


fila = Fila()
fila.push(1)
fila.push(4)
fila.push(5)
fila.push(2)

print("Fila original:")
fila.imprimir()

fila.inverter()

print("\nFila invertida:")
fila.imprimir()
