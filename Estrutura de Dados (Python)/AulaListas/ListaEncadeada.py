class Nodo:
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return f"self.dado, self.proximo"


class Pilha:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __repr__(self):
        return "[" + str(self.primeiro) + "]"

    def insere(self, novo_dado):
        novo_nodo = Nodo(novo_dado)

        if self.primeiro is None:
            self.primeiro = novo_nodo
            self.ultimo = novo_nodo

        else:
            self.ultimo.proximo = novo_nodo
            self.ultimo = novo_nodo
