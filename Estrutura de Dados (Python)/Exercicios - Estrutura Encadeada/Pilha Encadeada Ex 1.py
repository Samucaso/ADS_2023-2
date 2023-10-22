# 1. Escrever uma função que receba como parâmetro uma pilha.
# A função deve retornar o maior elemento da pilha.

class Nodo:
    def __init__(self, dado=0, nodo_anterior=None):
        self.dado = dado
        self.anterior = nodo_anterior

    def __repr__(self):
        return f"{self.dado} -> {self.anterior}"


class Pilha:
    def __init__(self):
        self.topo = None

    def __repr__(self):
        return "[" + str(self.topo) + "]"

    def insere(self, novo_dado):
        novo_nodo = Nodo(novo_dado)

        novo_nodo.anterior = self.topo

        self.topo = novo_nodo

    def remove(self):
        assert self.topo, "Impossivel remover valor de pilha vazia"
        self.topo = self.topo.anterior

    def maior_elemento(self, pilha):
        if not pilha.topo:
            return None

        max_element = pilha.topo.dado
        corrente = pilha.topo

        while corrente:
            if corrente.dado > max_element:
                max_element = corrente.dado
            corrente = corrente.anterior

        return max_element


pilha = Pilha()
pilha.insere(3)
pilha.insere(5)
pilha.insere(1)
pilha.insere(7)
pilha.insere(2)

print(pilha)
maior_elemento = pilha.maior_elemento(pilha)
if maior_elemento is not None:
    print("Maior elemento na pilha:", maior_elemento)
else:
    print("A pilha está vazia.")