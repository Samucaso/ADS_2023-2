"""
2. Remova duplicatas de uma lista ordenada.
Suponha que lhe seja fornecida uma lista encadeada
armazenando números inteiros em ordem crescente.
Sua tarefa é remover todos os elementos duplicados da lista.
Por exemplo, dada a lista [0 → 1 → 1 → 5 → 7 → 10 → 10 → None],
seu programa deve retornar a lista [0 → 1 → 5 → 7 → 10 → None].
"""


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

    def remove_duplicatas(self):
        corrente = self.cabeca

        while corrente and corrente.proximo:
            if corrente.dado == corrente.proximo.dado:
                corrente.proximo = corrente.proximo.proximo
            else:
                corrente = corrente.proximo


lista = ListaEncadeada()
for i in [0, 1, 1, 5, 7, 10, 10]:
    lista.insere_no_inicio(lista, i)

print("Lista original:", lista)
lista.remove_duplicatas()
print("Lista após a remoção de duplicatas:", lista)
