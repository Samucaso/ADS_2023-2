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

    def insere_depois(self, lista, nodo_anterior, novo_dado):
        assert nodo_anterior, "Nodo anterior precisa existir na lista"

        novo_nodo = NodoLista(novo_dado)

        novo_nodo.proximo = nodo_anterior.proximo

        nodo_anterior.proximo = novo_nodo

    def busca(self, lista, valor):
        corrente = lista.cabeca
        while corrente and corrente.dado != valor:
            corrente = corrente.proximo
        return corrente


lista = ListaEncadeada()
for i in range(8):
    lista.insere_no_inicio(lista, i)
print("Lista:", lista)

for i in range(8, -4, -2):
    elemento = lista.busca(lista, i)
    if elemento:
        print(f"Elemento {i} presente na lista!")
    else:
        print(f"Elemento {i} não encontrado!")
