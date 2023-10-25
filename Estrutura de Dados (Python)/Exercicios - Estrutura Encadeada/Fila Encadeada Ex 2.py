"""
2. Crie uma função de busca em que o usuário insere um valor (inteiro)
e o programa retorna a sua posição na fila.
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

    def buscar(self, valor):
        corrente = self.primeiro
        posicao = 0

        while corrente is not None:
            if corrente.dado == valor:
                return posicao
            corrente = corrente.proximo
            posicao += 1

        return -1


fila = Fila()
fila.push(1)
fila.push(2)
fila.push(3)

valor = 2
posicao = fila.buscar(valor)
if posicao >= 0:
    print(f"O valor {valor} está na posição {posicao} da fila.")
else:
    print(f"O valor {valor} não foi encontrado na fila.")
