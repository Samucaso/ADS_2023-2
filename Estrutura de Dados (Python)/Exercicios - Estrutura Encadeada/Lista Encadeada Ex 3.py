# 3. Defina as funções inserção, remoção e busca como métodos da Classe Lista.

# obs: esse eu nao entendi direito oq era preciso fazer ent so renomeei os metodos que eu ja tinha
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

    def insercao(self, lista, novo_dado):
        novo_nodo = NodoLista(novo_dado)

        novo_nodo.proximo = lista.cabeca

        lista.cabeca = novo_nodo

    def busca(self, lista, valor):
        corrente = lista.cabeca
        while corrente and corrente.dado != valor:
            corrente = corrente.proximo
        return corrente

    def remocao(self, valor):
        anterior = None
        corrente = self.cabeca

        while corrente and corrente.dado != valor:
            anterior = corrente
            corrente = corrente.proximo

        if corrente:
            if anterior is None:
                self.cabeca = corrente.proximo
            else:
                anterior.proximo = corrente.proximo
            corrente.proximo = None

        return corrente


lista = ListaEncadeada()
for i in range(8):
    lista.insercao(lista, i)
print("Lista:", lista)

for i in range(8, -4, -2):
    elemento = lista.remocao(i)
    if elemento:
        print(f"Elemento {i} removido da lista!")
    else:
        print(f"Elemento {i} não foi encontrado!")

print("Lista após as remoções:", lista)
