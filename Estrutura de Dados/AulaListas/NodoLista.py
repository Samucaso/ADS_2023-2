class NodoLista:
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo_nodo = proximo_nodo

    def __repr__(self):
        return f'{self.dado} -> {self.proximo_nodo}'


class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"

    def insere_no_inicio(self, lista, novo_dado):
        novo_nodo = NodoLista(novo_dado)
        novo_nodo.proximo_nodo = lista.cabeca
        lista.cabeca = novo_nodo
