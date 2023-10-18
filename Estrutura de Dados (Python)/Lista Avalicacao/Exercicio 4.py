class Nodo:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class ListaCircularEncadeada:
    def __init__(self):
        self.cabeca = None

    def esta_vazia(self):
        return self.cabeca is None

    def adicionar(self, dado):
        novo_nodo = Nodo(dado)

        if not self.cabeca:
            novo_nodo.proximo = novo_nodo
            self.cabeca = novo_nodo
        else:
            temp = self.cabeca
            while temp.proximo != self.cabeca:
                temp = temp.proximo
            temp.proximo = novo_nodo
            novo_nodo.proximo = self.cabeca

    def remover(self, dado):
        if self.esta_vazia():
            print("A lista está vazia.")
            return

        if self.cabeca.dado == dado:
            if self.cabeca.proximo == self.cabeca:
                self.cabeca = None
            else:
                temp = self.cabeca
                while temp.proximo != self.cabeca:
                    temp = temp.proximo
                temp.proximo = self.cabeca.proximo
                self.cabeca = self.cabeca.proximo
        else:
            temp = self.cabeca
            anterior = None
            while temp.proximo != self.cabeca and temp.dado != dado:
                anterior = temp
                temp = temp.proximo

            if temp.dado == dado:
                anterior.proximo = temp.proximo
            else:
                print("Elemento não encontrado.")

    def buscar(self, dado):
        if self.esta_vazia():
            print("A lista está vazia.")
            return False

        temp = self.cabeca
        while temp.proximo != self.cabeca:
            if temp.dado == dado:
                print("Elemento encontrado.")
                return True
            temp = temp.proximo

        if temp.dado == dado:
            print("Elemento encontrado.")
            return True
        else:
            print("Elemento não encontrado.")
            return False

    def exibir(self):
        if self.esta_vazia():
            print("A lista está vazia.")
            return

        temp = self.cabeca
        while True:
            print(temp.dado, end=" ")
            temp = temp.proximo
            if temp == self.cabeca:
                break
        print()


if __name__ == "__main__":
    lista_circular = ListaCircularEncadeada()

    lista_circular.adicionar(1)
    lista_circular.adicionar(2)
    lista_circular.adicionar(3)
    lista_circular.adicionar(4)

    print("Lista circular:")
    lista_circular.exibir()

    lista_circular.buscar(3)
    lista_circular.buscar(5)

    lista_circular.remover(2)

    print("Lista circular após remoção:")
    lista_circular.exibir()
