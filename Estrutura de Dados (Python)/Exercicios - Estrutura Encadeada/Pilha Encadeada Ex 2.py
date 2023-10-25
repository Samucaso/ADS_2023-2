# 2. Utilizando uma pilha resolver o exercício a seguir:
# Dada uma sequência contendo N (N >0) números reais, imprimi-la na ordem inversa.


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

    def sequencia_inversa(self, sequencia):
        pilha = Pilha()
        for numero in sequencia:
            pilha.insere(numero)

        while pilha.topo:
            print(pilha.topo.dado, end=" ")
            pilha.remove()


pilha = Pilha()
sequencia = [1.0, 2.5, 3.3, 4.7, 5.2]
print("Sequência original:", sequencia)
print("Sequência inversa:")
pilha.sequencia_inversa(sequencia)
