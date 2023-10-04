class Nodo:
    def __init__(self, dado=0, nodo_anterior=None):
        self.dado = dado
        self.anterior = nodo_anterior

    def __repr__(self):
        return f"self.dado, self.anterior"


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

        assert self.topo, "Impossivel remover valor de pilha vazia."

        self.topo = self.topo.anterior


pilha = Pilha()
print("Pilha vazia: ", pilha)

for i in range(5):
    pilha.insere(i)
    print(f"Insere o valor {i} no topo da pilha: {pilha}")

while pilha.topo is not None:
    pilha.remove()
    print("Removendo elemento que está no topo da pilha: ", pilha)
