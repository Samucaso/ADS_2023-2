"""
1. Implemente uma fila dinâmica contendo todas as funcionalidades de uma fila padrão. Para isso, resolvar:
–Crie um nó padrão da fila.
–Crie uma função de inicialização da fila vazia
–Crie uma função push que cria e insere um novo nó para o final da fila.
–Crie uma função pop que remove o primeiro elemento da fila.
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
        assert self.primeiro is not None, "Impossivel remover elemento de fila vazia"

        self.primeiro = self.primeiro.proximo

        if self.primeiro is None:
            self.ultimo = None


fila = Fila()
fila.push(1)
fila.push(2)
fila.push(3)

print(fila)

fila.pop()
print(fila)
