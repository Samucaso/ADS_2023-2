class NodoLista:
    def __init__(self, dado, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return f"{self.dado} -> {self.proximo}"


class ListaCircular:
    def __init__(self):
        self.cabeca = None

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"
