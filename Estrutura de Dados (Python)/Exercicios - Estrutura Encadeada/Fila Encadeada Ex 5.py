"""
5. No seu sistema operacional ao abrir o “gerenciador de tarefas” você pode
exibir os processos que estão em execução.

Você já parou pra pensar como é possível executar todos esses aplicativos em apenas um processador?
Isso existe graças a uma funcionalidade chamada de tempo compartilhado (“time-shared”).
Essa funcionalidade mantém uma sequência de processos em uma fila, esperando para serem executados.
Modifique a fila dinâmica que você implementou anteriormente para armazenar as informações desses processos.

Seu programa deverá permitir:
–Incluir novos processos na fila de processo;
–Matar o processo com o maior tempo de espera;
–Executar um processo (remover da fila)
–Imprimir o conteúdo da lista de processos.
"""


class Nodo:
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return f"{self.dado} -> {self.proximo}"


class Processo:
    def __init__(self, pid, tempo_espera):
        self.pid = pid
        self.tempo_espera = tempo_espera

    def __repr__(self):
        return f"Processo {self.pid} (Tempo de Espera: {self.tempo_espera})"


class FilaProcessos:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __repr__(self):
        return "[" + str(self.primeiro) + "]"

    def push(self, processo):
        novo_nodo = Nodo(processo)

        if self.primeiro is None:
            self.primeiro = novo_nodo
            self.ultimo = novo_nodo
        else:
            self.ultimo.proximo = novo_nodo
            self.ultimo = novo_nodo

    def pop(self):
        assert self.primeiro is not None, "Impossível remover elemento da fila vazia"

        self.primeiro = self.primeiro.proximo

        if self.primeiro is None:
            self.ultimo = None

    def imprimir(self):
        corrente = self.primeiro

        while corrente is not None:
            print(corrente.dado, end=" ")
            corrente = corrente.proximo

    def adicionar_processo(self, pid, tempo_espera):
        processo = Processo(pid, tempo_espera)
        self.push(processo)

    def matar_processo_maior_tempo_espera(self):
        if self.primeiro:
            maior_tempo = self.primeiro.dado.tempo_espera
            processo_maior_tempo = self.primeiro

            corrente = self.primeiro
            anterior = None

            while corrente:
                if corrente.dado.tempo_espera > maior_tempo:
                    maior_tempo = corrente.dado.tempo_espera
                    processo_maior_tempo = corrente

                anterior = corrente
                corrente = corrente.proximo

            if processo_maior_tempo == self.primeiro:
                self.primeiro = self.primeiro.proximo
            else:
                anterior.proximo = processo_maior_tempo.proximo

    def executar_processo(self):
        if self.primeiro:
            processo_executado = self.primeiro
            self.pop()
            return processo_executado.dado
        return None


fila_processos = FilaProcessos()
fila_processos.adicionar_processo(1, 10)
fila_processos.adicionar_processo(2, 5)
fila_processos.adicionar_processo(3, 15)
print("Fila de processos:")
fila_processos.imprimir()

print("\nExecutando um processo:")
processo_executado = fila_processos.executar_processo()
if processo_executado:
    print("Processo executado:", processo_executado)

print("\nFila de processos após execução:")
fila_processos.imprimir()

print("\nMatando o processo com o maior tempo de espera:")
fila_processos.matar_processo_maior_tempo_espera()
print("Fila de processos após matar o processo:")
fila_processos.imprimir()
