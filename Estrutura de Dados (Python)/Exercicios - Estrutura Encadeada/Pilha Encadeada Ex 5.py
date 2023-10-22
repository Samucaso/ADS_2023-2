"""
5. Implemente uma função chamada TPilha, que receba um vetor de inteiros com 15 elementos.
Para cada um deles, como segue:

Se o número for par, insira-o na pilha;
Se o número lido for ímpar, retire um número da pilha;
Ao final, esvazie a pilha imprimindo os elementos.
"""


class Nodo:
    def __init__(self, dado=0, nodo_anterior=None):
        self.dado = dado
        self.anterior = nodo_anterior

    def __repr__(self):
        return f"{self.dado} -> {self.anterior}"


class Pilha:
    def __init__(self):
        self.topo = None

    def insere(self, novo_dado):
        novo_nodo = Nodo(novo_dado)
        novo_nodo.anterior = self.topo
        self.topo = novo_nodo

    def remove(self):
        assert self.topo, "Impossivel remover valor de pilha vazia"
        self.topo = self.topo.anterior

    def tpilha(self, vetor):
        for numero in vetor:
            if numero % 2 == 0:
                self.insere(numero)
            else:
                if self.topo:
                    self.remove()

        while self.topo:
            print(self.topo.dado, end=" ")
            self.remove()


pilha = Pilha()
vetor = [1, 2, 89, 12, 34, 32, 23, 22, 98, 24]
print("Vetor original:", vetor)
print("Vetor apos TPilha:")
pilha.tpilha(vetor)
