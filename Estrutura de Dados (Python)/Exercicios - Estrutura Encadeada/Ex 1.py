# 1. Implemente a função remove utilizando a função busca.

class NodoLista:
    def __init__(self, dado, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return f"{self.dado} -> {self.proximo}"


class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"

    def insere_no_inicio(self, lista, novo_dado):
        novo_nodo = NodoLista(novo_dado)

        novo_nodo.proximo = lista.cabeca

        lista.cabeca = novo_nodo

    def insere_depois(self, lista, novo_dado):
        novo_nodo = NodoLista(novo_dado)

        novo_nodo.proximo = lista.cabeca

        lista.cabeca = novo_nodo


lista = ListaEncadeada()
print("Lista vazia: ", lista)

lista.insere_no_inicio(lista, 5)
print("Lista contém um único elemento: ", lista)

lista.insere_no_inicio(lista, 10)
print("Inserindo um novo elemento: ", lista)

