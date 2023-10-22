# 3. Escreva uma função que receba como parâmetro duas pilhas
# e verifique de elas são iguais.
# Duas pilhas são iguais se possuem os mesmos elementos, na mesma ordem.


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

    def pilhas_iguais(self, outra_pilha):
        corrente1 = self.topo
        corrente2 = outra_pilha.topo

        while corrente1 and corrente2:
            if corrente1.dado != corrente2.dado:
                return False
            corrente1 = corrente1.anterior
            corrente2 = corrente2.anterior

        return corrente1 is None and corrente2 is None


pilha1 = Pilha()
pilha2 = Pilha()

for i in range(5):
    pilha1.insere(i)
    pilha2.insere(i)

iguais = pilha1.pilhas_iguais(pilha2)

if iguais:
    print("As pilhas são iguais.")
else:
    print("As pilhas não são iguais.")
