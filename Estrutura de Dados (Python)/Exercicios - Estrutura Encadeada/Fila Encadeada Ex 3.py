"""
3. Crie uma função que percorre e imprime todos os elementos da fila.
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


fila = Fila()
fila.push(1)
fila.push(2)
fila.push(3)

print("Elementos na fila:")
fila.imprimir()

