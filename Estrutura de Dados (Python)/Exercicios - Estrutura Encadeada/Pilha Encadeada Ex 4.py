"""4. Construa um programa utilizando uma pilha que resolva o seguinte problema:

Armazene as placas dos carros (apenas os números)
que estão estacionadosnuma rua sem saída estreita.
Dado uma placa verifique se o carro está estacionado na rua.
Caso esteja, informe a sequência de carros que deverá ser retirada
para que o carro em questão consiga sair.
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

    def __repr__(self):
        return "[" + str(self.topo) + "]"

    def insere(self, novo_dado):
        novo_nodo = Nodo(novo_dado)

        novo_nodo.anterior = self.topo

        self.topo = novo_nodo

    def remove(self):
        assert self.topo, "Impossivel remover valor de pilha vazia"
        self.topo = self.topo.anterior

    def sequencia_para_sair(self, placa_alvo):
        pilha_temp = Pilha()
        sequencia_saida = []

        while self.topo and self.topo.dado != placa_alvo:
            carro = self.topo.dado
            sequencia_saida.append(carro)
            pilha_temp.insere(carro)
            self.remove()

        if not self.topo:
            return None

        self.remove()

        while pilha_temp.topo:
            carro = pilha_temp.topo.dado
            self.insere(carro)
            pilha_temp.remove()

        return sequencia_saida


pilha_carros = Pilha()
placas_estacionadas = [123, 456, 789, 101, 202]

for placa in placas_estacionadas:
    pilha_carros.insere(placa)

placa_alvo = 123
sequencia_saida = pilha_carros.sequencia_para_sair(placa_alvo)

if sequencia_saida is not None:
    print(f"Sequência de carros a ser retirada para que o carro {placa_alvo} saia:", sequencia_saida)
else:
    print(f"O carro {placa_alvo} não está na rua.")
