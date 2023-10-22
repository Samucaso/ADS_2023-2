"""
6. Escreva uma função chamada TPilha2 que recebe como parâmetro 2 pilhas (N e P) e um vetor de inteiros. Para cada um:

se positivo, inserir na pilha P;
se negativo, inserir na pilha N;
se zero, retirar um elemento de cada pilha.
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

    def __str__(self):
        current = self.topo
        elements = []
        while current:
            elements.append(str(current.dado))
            current = current.anterior
        return " -> ".join(elements)

    def insere(self, novo_dado):
        novo_nodo = Nodo(novo_dado)
        novo_nodo.anterior = self.topo
        self.topo = novo_nodo

    def remove(self):
        assert self.topo, "Impossivel remover valor de pilha vazia"
        self.topo = self.topo.anterior

    def tpilha2(self, pilhan, pilhap, vetor):
        for numero in vetor:
            if numero > 0:
                pilhap.insere(numero)
                print(f"Inserindo {numero} na pilha positiva")
            elif numero < 0:
                pilhan.insere(numero)
                print(f"Inserindo {numero} na pilha negativa")
            else:
                if pilhap.topo:
                    pilhap.remove()
                    print("Removendo da pilha positiva")
                if pilhan.topo:
                    pilhan.remove()
                    print("Removendo da pilha negativo")


pilha = Pilha()
pilha_N = Pilha()
pilha_P = Pilha()
vetor = [1, -2, 3, -4, 0, 5, -6, 0]
pilha.tpilha2(pilha_N, pilha_P, vetor)
print("O que sobrou da lista negativa:", pilha_N)
print("O que sobrou da lista positiva: ", pilha_P)
